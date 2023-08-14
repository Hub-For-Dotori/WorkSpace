package day13;

public class Audio implements Runnable {
	@Override
	public void run() {
		for(int i=0;i<10;i++) {
			System.out.println("오디오 "+(i+1)+"번");
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
