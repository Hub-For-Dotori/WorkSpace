package day3;

import java.util.Scanner;

public class work1 {
	public static void main(String[] args) {
		//과제 : 0으로 나누는 경우 오류 발생 
		//못 나누게 제어문 추가
		//작성한 소스 코드 출력 모든 라인에 주석 작성
		//단, 핸드 프린팅(손으로) 작성
		Scanner scan = new Scanner(System.in);
		int a=0, b=0;
		
		System.out.print("정수 입력: ");
		a = scan.nextInt();
		System.out.println("입력 값 : "+ a);
		
		System.out.print("정수 입력: ");
		b = scan.nextInt();
		System.out.println("입력 값 : "+ b);
		
		System.out.println("덧셈 결과: " + (a+b));
		System.out.println("뺄셈 결과: " + (a-b));
		System.out.println("곱셈 결과: " + (a*b));
		
		if(b != 0 && a !=0) System.out.println("나눗셈 결과: " +(a/b));
		else System.out.println("연산 중 입력 값 중 둘 다 또는 한 값이 \n0이 포함 되어 연산이 불가합니다.");         
		
		
		scan.close();
	}
	
}
