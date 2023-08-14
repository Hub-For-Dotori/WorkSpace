package day9;

import java.util.Scanner;

public class Tv {
	// 속성
	public boolean isOn;
	public int ch;
	public int vol;
	
	//기능
	public void power() {
		if (isOn==true) {
			isOn = false;
			System.out.println("전원 꺼짐");
		}
		else {
			isOn = true;
			System.out.println("전원 켜짐");
		}
	}
	// 채널 올림 내림 함수 작성하시오.
	
	public void chUp() {
		if(isOn) {
			ch++;
			System.out.println("채널 : "+ch);
		}
		
	}
	public void chDown() {
		if(isOn) {
			ch--;
			System.out.println("채널 : "+ch);
		}
		
	}
}
