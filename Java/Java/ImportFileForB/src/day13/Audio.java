package day13;

public class Audio implements Runnable {
	@Override
	public void run() {
		for(int i=0;i<10;i++) {
			System.out.println("����� "+(i+1)+"��");
			try {
				Thread.sleep(300);
			} 
			catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
