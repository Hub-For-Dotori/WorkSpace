package day6;

import java.util.Scanner;

public class WhileSample {
	public static Scanner scan;
	//맴버 변수 선언 : 맴버 변수는 선언과 동시에 초기화 하지 않음
	//맴버 변수는 자동으로 초기화 됨 => 단 해당 자료의 기본값으로 초기화 됌
	//클래스로 선언한 변수는 객체 변수라 함. => 객체 변수의 자동 초기화된 값은 NULL임. 
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		whilebasic();
		dowhilebasic();
		infiniteWhile();
		scan.close();
	}
	
	public static void whilebasic() {
		int iNum = 1;
		while(iNum != 0) {
			System.out.print("입력 : ");
			iNum =scan.nextInt();
			System.out.println("값 : "+iNum);	
		}
		System.out.println("0값 입력 : 함수 종료");
	}
	public static void dowhilebasic() {
		int iNum = 1;
		
		do {
			System.out.print("입력 : ");
			iNum =scan.nextInt();
			System.out.println("값 : "+iNum);	
		} while(iNum != 0);
		
		System.out.println("0값 입력 : 함수 종료");
	}
	public static void infiniteWhile() {
		int iNum =0;
		while (true) {
			System.out.print("입력 : ");
			iNum =scan.nextInt();
			System.out.println("값 : "+iNum);
			if(iNum == 0) break; 
			// 즉시 자신이 속한 블럭을 벗어나는 코드
		}
		System.out.println("반복 종료");
	}

}