package day4;

import java.util.Scanner;

public class SwitchSample {

	public static void main(String[] args) {
		//�ʿ� ���� ���� 
		Scanner scan = new Scanner(System.in);
		
		//�ȳ� �׸��� �Է�ó��
		System.out.print("�Է� : ");
		int iNum1=scan.nextInt();
			
		if (iNum1 <= 100 && iNum1 >= 0) {			
			switch(iNum1/10) {
			case 10:
				System.out.print("A+");
				break;			
			case 9:
				System.out.print("A");
				break;
			case 8:
				System.out.print("B");
				break;
			case 7:
				System.out.print("C");
				break;
			case 6:
				System.out.print("D");
				break;
			default:
				System.out.print("F");
				break;
			}
			if (iNum1 % 10 >= 5 && iNum1 >= 60 )
				System.out.println("+");
		} 
		else
			System.out.println("�߸��� ��");	
		scan.close();
	}

}
