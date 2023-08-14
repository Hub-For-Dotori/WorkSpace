package day4;

import java.util.Scanner;

public class SwitchSample {

	public static void main(String[] args) {
		//필요 변수 선언 
		Scanner scan = new Scanner(System.in);
		
		//안내 그리고 입력처리
		System.out.print("입력 : ");
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
			System.out.println("잘못된 값");	
		scan.close();
	}

}
