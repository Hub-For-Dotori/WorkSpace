package day4;

import java.util.Scanner;

public class IfSample {

	public static void main(String[] args) {
		//필요 변수 선언 
		Scanner scan = new Scanner(System.in);
		
		//안내 그리고 입력처리
		System.out.print("입력 : ");
		int iNum1=scan.nextInt();
		
//		if(iNum1>0) {
//			if(iNum1%2==0) {
//				System.out.println("짝수");
//			}
//			else {
//				System.out.println("홀수");
//			}
//		}
//		else if(iNum1<0) {
//			System.out.println("음수는 불가능");				
//		}
//		else {
//			System.out.println("0은 불가능");
//		}
		
		if(iNum1<=0) {
			if(iNum1==0) {
				System.out.println("0");
			}
			else {
				System.out.println("음수");
			}
		}
		else if(iNum1%2==0) {
			System.out.println("짝수");				
		}
		else {
			System.out.println("홀수");
		}
		
		scan.close();
	}

}
