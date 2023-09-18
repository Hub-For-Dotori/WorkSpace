package day13;
public class Day13Main {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Video vThread = new Video();
		Audio a = new Audio();
		Thread aThread = new Thread(a);
		vThread.start();
		aThread.start();
		
	}
}

