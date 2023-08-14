package day3;

import java.util.Scanner;

// ctrl + shift + o
public class InputSample {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		// 정수 2개를 저장할 변수 필요
		int iNum1 = 0, iNum2 = 0;
		
		// 입력안내문장 출력
		System.out.print("정수 입력: ");
		// 첫번째 변수에 값을 입력 받는다.
		iNum1 = scan.nextInt();
		System.out.println("입력 값 : "+iNum1);
		// 두번째 변수에 값 입력
		System.out.print("정수 입력: ");
		// 두번째 변수에 값을 입력 받는다.
		iNum2 = scan.nextInt();
		System.out.println("입력 값 : "+iNum1);
		//과제 : 0으로 나누는 경우 오류 발생 
		//못 나누게 제어문 추가
		//작성한 소스 코드 출력 모든 라인에 주석 작성
		//단, 핸드 프린팅(손으로) 작성
		// 결과 출력
		System.out.println("덧셈 결과: " +(iNum1 + iNum2));
		System.out.println("뺄셈 결과: " +(iNum1 - iNum2));
		System.out.println("곱셈 결과: " +(iNum1 * iNum2));
		System.out.println("나눗셈 결과: " +(iNum1 / iNum2));
		
		
		scan.close();

	}

}
