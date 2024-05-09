package veeva;

import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import com.google.common.collect.HashBasedTable;
import au.com.bytecode.opencsv.CSVWriter;

public class Record {

	HashBasedTable<Integer, String, String> map;

	public Record() {
		this.map = HashBasedTable.create();
	}

	public void addEntry(Integer id, String column, String value) {

		this.map.put(id, column, value);

	}

	public void merge(Record record) {

		for (Integer key : record.map.rowMap().keySet()) {
			Map<String, String> data = record.map.row(key);

			for (String column : data.keySet()) {
				this.addEntry(key, column, data.get(column));
			}
		}

	}

	public void exportCSV(String filename) {
		try {
			CSVWriter writer = new CSVWriter(new FileWriter(filename));

			List<String> header = new ArrayList<>();

			header.add("ID");

			for (String col : this.map.columnKeySet()) {
				header.add(col);
			}
			String[] raw_headers = new String[header.size()];

			raw_headers = header.toArray(raw_headers);

			writer.writeNext(raw_headers);
			
			List<Integer> orderedIDs = new ArrayList<>();
			
			for (Integer ID: this.map.rowMap().keySet()) {
				orderedIDs.add(ID);
			}
			
			Collections.sort(orderedIDs);
			
			
			for (Integer ID : orderedIDs) {
				Map<String, String> data = this.map.row(ID);

				List<String> row = new ArrayList<>();
				row.add(ID.toString());
				
				for (String h : header) {

					if (h.equals("ID")) {
						continue;
					}
					if (data.containsKey(h)) {
						row.add(data.get(h));
					} else {
						row.add("");
					}

				}

				String[] raw = new String[header.size()];

				raw = row.toArray(raw);

				writer.writeNext(raw);
			}
			writer.close();
		} catch (Exception e) {
			System.out.print(e.getMessage());
			return;
		}
	}

}