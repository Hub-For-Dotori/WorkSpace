package day9;

import java.util.Scanner;

public class Tv {
	// �Ӽ�
	public boolean isOn;
	public int ch;
	public int vol;
	
	//���
	public void power() {
		if (isOn==true) {
			isOn = false;
			System.out.println("���� ����");
		}
		else {
			isOn = true;
			System.out.println("���� ����");
		}
	}
	// ä�� �ø� ���� �Լ� �ۼ��Ͻÿ�.
	
	public void chUp() {
		if(isOn) {
			ch++;
			System.out.println("ä�� : "+ch);
		}
		
	}
	public void chDown() {
		if(isOn) {
			ch--;
			System.out.println("ä�� : "+ch);
		}
		
	}
}
