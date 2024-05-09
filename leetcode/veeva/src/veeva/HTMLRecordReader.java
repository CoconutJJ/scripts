package veeva;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class HTMLRecordReader implements RecordReader {

	Record map;

	public HTMLRecordReader() {
		this.map = new Record();

	}

	public void ingest(String source) {

		Document doc = Jsoup.parse(source);

		Elements tableHeaders = doc.select("table th");

		List<String> headers = new ArrayList<String>();

		for (Element e : tableHeaders) {

			headers.add(e.text());

		}
		
		Elements tableRows = doc.select("table tr");

		for (Element row : tableRows) {

			Elements entries = row.select("td");

			if (entries.size() == 0) {
				continue;
			}

			int idx = 0;

			HashMap<String, String> data = new HashMap<>();
			Integer ID = -1;
			for (Element entry : entries) {

				String headerName = headers.get(idx);

				headerName = headerName.trim().toLowerCase();

				if (headerName.equals("id")) {
					ID = Integer.decode(entry.text());
				} else {
					data.put(headers.get(idx), entry.text());
				}

				idx++;

				if (idx == headers.size()) {
					break;
				}

			}
			
			for (String header : data.keySet()) {
				
				this.map.addEntry(ID, header, data.get(header));
				
			}
			
			

		}

	}

	public Record toRecord() {
		return this.map;
	}

}
