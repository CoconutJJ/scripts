package veeva;

import au.com.bytecode.opencsv.CSVReader;

import java.io.IOException;
import java.io.StringReader;
import java.util.HashMap;

public class CSVRecordReader implements RecordReader {

	public Record record;

	public CSVRecordReader() {

		this.record = new Record();
		
	}

	public Record toRecord() {
		return this.record;
	}

	public void ingest(String source) {

		CSVReader reader = new CSVReader(new StringReader(source));

		String[] header;

		try {
			header = reader.readNext();
		} catch (IOException e) {
			return;
		}

		String[] line;

		try {
			while ((line = reader.readNext()) != null) {

				Integer ID = -1;
				HashMap<String, String> data = new HashMap<>();

				for (int i = 0; i < line.length; i++) {

					String headerName = header[i];

					headerName = headerName.trim().toLowerCase();

					if (headerName.equals("id")) {
						ID = Integer.decode(line[i]);
					} else {
						data.put(header[i], line[i]);
					}

				}
				for (String key : data.keySet()) {
					this.record.addEntry(ID, key, data.get(key));
				}
			}
		} catch (IOException e) {
			return;
		}

	}

}
