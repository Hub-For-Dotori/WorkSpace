package day13;
public class Video extends Thread {
	
	@Override
	public void run() {
	
		for(int i=0;i<10;i++) {
				
			System.out.println("비디오 "+(i+1)+"번");
			try {
				sleep(300);
			} 
			catch (InterruptedException e) {
			// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
			
	}
}
