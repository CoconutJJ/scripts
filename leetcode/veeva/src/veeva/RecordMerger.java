package veeva;

import java.nio.file.Files;
import java.nio.file.Path;

public class RecordMerger {

	public static final String FILENAME_COMBINED = "combined.csv";

	/**
	 * Entry point of this test.
	 *
	 * @param args command line arguments: first.html and second.csv.
	 * @throws Exception bad things had happened.
	 * 
	 * Assumptions:
	 * 
	 * - No two files will share entry with same ID and same column name. Overwrites with last file processed if so.
	 * - Every file will have an ID column.
	 * - File format matches file extension
	 * 
	 */
	public static void main(final String[] args) throws Exception {

		if (args.length == 0) {
			System.err.println("Usage: java RecordMerger file1 [ file2 [...] ]");
			System.exit(1);
		}
		

		Record record = new Record();

		for (int i = 0; i < args.length; i++) {

			String filename = args[i];
			String ext = filename.split("\\.")[1];
			

			String fileContents = Files.readString(Path.of(filename));
			RecordReader reader;

			switch (ext) {
			case "html":
				reader = new HTMLRecordReader();
				reader.ingest(fileContents);
				break;
			case "csv":
				reader = new CSVRecordReader();
				reader.ingest(fileContents);
				break;
			default:
				throw new Exception("File format not recognized");
			}

			record.merge(reader.toRecord());

		}
		
		record.exportCSV(FILENAME_COMBINED);
		
	}
}
