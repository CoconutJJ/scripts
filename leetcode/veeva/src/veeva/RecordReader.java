package veeva;

public interface RecordReader {
	
	public Record toRecord();
	public void ingest(String source);
	
}


