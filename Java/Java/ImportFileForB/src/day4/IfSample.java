package day4;

import java.util.Scanner;

public class IfSample {

	public static void main(String[] args) {
		//�ʿ� ���� ���� 
		Scanner scan = new Scanner(System.in);
		
		//�ȳ� �׸��� �Է�ó��
		System.out.print("�Է� : ");
		int iNum1=scan.nextInt();
		
//		if(iNum1>0) {
//			if(iNum1%2==0) {
//				System.out.println("¦��");
//			}
//			else {
//				System.out.println("Ȧ��");
//			}
//		}
//		else if(iNum1<0) {
//			System.out.println("������ �Ұ���");				
//		}
//		else {
//			System.out.println("0�� �Ұ���");
//		}
		
		if(iNum1<=0) {
			if(iNum1==0) {
				System.out.println("0");
			}
			else {
				System.out.println("����");
			}
		}
		else if(iNum1%2==0) {
			System.out.println("¦��");				
		}
		else {
			System.out.println("Ȧ��");
		}
		
		scan.close();
	}

}
