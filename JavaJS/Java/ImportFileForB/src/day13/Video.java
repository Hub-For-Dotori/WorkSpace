package day13;
public class Video extends Thread {
	
	@Override
	public void run() {
	
		for(int i=0;i<10;i++) {
				
			System.out.println("���� "+(i+1)+"��");
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
