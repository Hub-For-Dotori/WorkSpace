package day4;

import java.util.Scanner;

public class IfTest {

	public static void main(String[] args) {
		// 실습 문제 : 키보드로 정수(정수형태)를 입력 받는다.
		// 그 값의 등급을 판단하시오. 85~89 비플 100~95에이플 94~90에이
		// 보관 -> 안내 -> 실제입력 -> 등급판단
		// -> 입력값 기준 적절한 값인가

		// 필요 변수 선언
		Scanner scan = new Scanner(System.in);

		// 안내 그리고 입력처리
		System.out.print("입력 : ");
		int iNum1 = scan.nextInt();

		if (iNum1 <= 100 && iNum1 >= 0) {
			if (iNum1 >= 90)
				System.out.print("A");
			else if (iNum1 >= 80)
				System.out.print("B");
			else if (iNum1 >= 70)
				System.out.print("C");
			else if (iNum1 >= 60)
				System.out.print("D");
			else
				System.out.print("F");
			if (iNum1 % 10 >= 5 && iNum1 >= 60 || iNum1 == 100)
				System.out.println("+");
		} else
			System.out.println("잘못된 값");
		scan.close();
		

	}

}
