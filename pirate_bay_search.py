from urllib.parse import urlencode, quote_plus
from requests import get
from textual.app import App
from textual.widgets import (
    Input,
    Label,
    DataTable,
    Header,
    Footer,
    DirectoryTree,
    Button,
)
from textual.containers import Horizontal, Vertical
from textual import on
import libtorrent as lt
import asyncio
from textual_fspicker import SelectDirectory
from pathlib import PosixPath


class DirectorySelector(DirectoryTree):

    def __init__(self, path, *, name=None, id=None, classes=None, disabled=False):
        super().__init__(path, name=name, id=id, classes=classes, disabled=disabled)

    def filter_paths(self, paths):

        filtered_paths = []

        for p in paths:
            filtered_paths.append(p.parent)

        return p


class PirateBaySearch(App):
    CSS = """
    PirateBaySearch {
        overflow-y: scroll;
    }
    #app {
        overflow-y: scroll;
    }
    DataTable {
        overflow-y: scroll;
        height: 80%;
    }
    Input {
        margin-top: 1;

        width: 100%;
    }
    #left {
        margin-left: 1;
        margin-right: 1;  
  
    }
    #right {
        margin-top: 1;
        margin-left: 1;
        margin-right: 1;    
    }
    #select-dir {
        height: 3;
        margin-top: 1;
        margin-bottom: 1;
    }
    Footer {
        dock: bottom;
    }
    Button {
        background: green;
        color: white;
        margin-right: 1;
    }
    Label {
        margin-top: 1;
    }

    """

    TITLE = "Pirate Bay Search Tool"

    def __init__(
        self, driver_class=None, css_path=None, watch_css=False, ansi_color=False
    ):
        super().__init__(driver_class, css_path, watch_css, ansi_color)
        self.column_keys = None
        self.key_log = Label()
        self.table = DataTable()
        self.search = Input(id="search-bar", placeholder="Search")
        self.header = Header()
        self.footer = Footer()
        self.select_dir_btn = Button("Select Output Directory")
        self.select_dir_label = Label("No directory selected.")
        self.download_tasks = set()
        self.output_dir = None

    async def torrent(self, magnet_link, row_key):

        status_column = self.column_keys["Status"]
        upload_column = self.column_keys["Up"]
        download_column = self.column_keys["Down"]
        peers_column = self.column_keys["Peers"]
        state_column = self.column_keys["State"]

        ses = lt.session({"listen_interfaces": "0.0.0.0:6881"})
        params = {"save_path": str(self.output_dir)}

        h = lt.add_magnet_uri(ses, magnet_link, params)
        s = h.status()

        while not s.is_seeding:
            s = h.status()

            self.table.update_cell(
                row_key, status_column, f"In Progress ({s.progress * 100:.2f})"
            )

            download_rate, download_unit = self.convert_size_to_human_readable(
                s.download_rate
            )
            self.table.update_cell(
                row_key,
                download_column,
                f"{download_rate} {download_unit}/s",
                update_width=True,
            )

            upload_rate, upload_unit = self.convert_size_to_human_readable(
                s.upload_rate
            )
            self.table.update_cell(
                row_key,
                upload_column,
                f"{upload_rate} {upload_unit}/s",
                update_width=True,
            )

            self.table.update_cell(
                row_key, peers_column, s.num_peers, update_width=True
            )
            self.table.update_cell(row_key, state_column, s.state, update_width=True)

            await asyncio.sleep(1)

        self.table.update_cell(row_key, status_column, "Complete")

    def convert_size_to_human_readable(self, size: int) -> tuple[int, str]:

        units = ["B", "KB", "MB", "GB", "TB", "PB"]
        i = 0
        while size >= 1000:
            size = size / 1000
            i += 1

        return (size, units[i])

    def build_torrent_magnet_link(self, name, hash):

        return f"magnet:?xt=urn:btih:{hash}&" + urlencode(
            {
                "tr": [
                    "udp://tracker.opentrackr.org:1337",
                    "udp://open.stealth.si:80/announce",
                    "udp://tracker.torrent.eu.org:451/announce",
                    "udp://tracker.bittor.pw:1337/announce",
                    "udp://public.popcorn-tracker.org:6969/announce",
                    "udp://tracker.dler.org:6969/announce",
                    "udp://exodus.desync.com:6969",
                    "udp://open.demonii.com:1337/announce",
                ],
                "dn": name,
            },
            doseq=True,
            quote_via=quote_plus,
        )

    def search_torrents(self, query: str):

        r = get(
            "https://apibay.org/q.php",
            params={"q": query},
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0",
                "Referer": "https://thepiratebay.org/",
            },
        )

        data = []

        for t in r.json():
            data.append(
                {
                    **t,
                    "magnet": self.build_torrent_magnet_link(t["name"], t["info_hash"]),
                }
            )

        return data

    def compose(self):
        with Vertical(id="app"):
            yield self.header
            with Horizontal(id="body"):

                with Vertical(id="left"):
                    yield self.search

                    with Horizontal(id="select-dir"):
                        yield self.select_dir_btn
                        yield self.select_dir_label

                    yield self.table

            yield self.footer

        columns = [
            "Name",
            "Size",
            "Seeders",
            "Leechers",
            "# Files",
            "Uploaded By",
            "Status",
            "Up",
            "Down",
            "Peers",
            "State",
        ]

        self.column_keys = {
            k: v for k, v in zip(columns, self.table.add_columns(*columns))
        }

    def create_download_task(self, routine: asyncio.coroutines):

        download_task = asyncio.create_task(routine)
        self.download_tasks.add(download_task)
        download_task.add_done_callback(self.download_tasks.discard)

    def set_output_directory(self, dir: PosixPath):
        self.output_dir = dir
        self.select_dir_label.update(str(dir))

    @on(Button.Pressed)
    def on_directory_select(self):

        self.push_screen(SelectDirectory("./"), callback=self.set_output_directory)

    @on(DataTable.RowSelected)
    async def on_download(self):
        row_key, _ = self.table.coordinate_to_cell_key(self.table.cursor_coordinate)
        download_routine = self.torrent(row_key.value, row_key)
        self.create_download_task(download_routine)

    @on(Input.Submitted, "#search-bar")
    def on_search(self):
        data = self.search_torrents(self.search.value)

        self.table.clear()

        for i, row in enumerate(data):
            size, unit = self.convert_size_to_human_readable(int(row["size"]))
            size_label = f"{size:.2f} {unit}"
            self.table.cursor_type = "row"
            self.table.add_row(
                row["name"],
                size_label,
                row["seeders"],
                row["leechers"],
                row["num_files"],
                row["username"],
                "No Action",
                label=i + 1,
                key=row["magnet"],
            )


if __name__ == "__main__":

    app = PirateBaySearch().run()
