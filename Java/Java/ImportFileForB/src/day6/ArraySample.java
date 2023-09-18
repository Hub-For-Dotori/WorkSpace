package day6;

import java.util.Scanner;

public class ArraySample {
	public static Scanner scan;
	//맴버 변수 선언 : 맴버 변수는 선언과 동시에 초기화 하지 않음
	//맴버 변수는 자동으로 초기화 됨 => 단 해당 자료의 기본값으로 초기화 됌
	//클래스로 선언한 변수는 객체 변수라 함. => 객체 변수의 자동 초기화된 값은 NULL임. 
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		//arrayBasic();
		//arrayTest();
		//int i=0;
		int a[] =new int[3];
		//String str ="둘리";
		//func2(i);
		//System.out.println(i);
		func(a);
		System.out.println(a[0]);// call by reference : 참조에 의한 호출
		//test(str);
		//System.out.println(str);//
		//String strArray[] = new String[5];
		//for(String v : strArray) {
			//System.out.println(v);
		//}
		String strArray[] = new String[5]; //18번
		String str[] = {"둘리","고길동","홍길동","마이콜"};
		
		System.out.println("strArray[0] 주소 : "+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("원래 strArray[0]의 값 : \n"+strArray[0]+"\n\n");
		System.out.println("strTest() 실행 중..\n\n");
		
		strTest(strArray);  // 함수가 종료되고 strArray는 영향을 받지 않아야 하나 초기화를 안한 상태로 기본 값으로 주소가 null이여서 그 전에 strTest에서 만들어둔 마이콜의 주소 값을 가지게됨
		
		System.out.println("strTest() 종료\n\n");
		System.out.println("strTest를 거친 \nstrArray[0] 주소 : "+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("srtTest를 거친 \nstrArray[0]의 값 : \n"+strArray[0]); //따라서 결과 값이 변하게 된것
		
		scan.close();
		
	}
	// 위 18번 라인의 배열을 함수 strTest()의 매개변수로 전달하자!
	// 함수 내부에서 0번지 값을 마이콜로 수정하자
	// 원본에 영향을 미치는 지 확인 하자
	public static void strTest(String str[]) {
		str[0] = "마이콜";                       //strArray를 str로 명명하여 인자로 넣어주고 그 str의 배열 0번째를 마이콜이라 함. 
		System.out.println("strArray[0] 주소 : "+System.identityHashCode(str[0])+"\n\n");
	}
	// 참조형 매개변수인 String 타입의 매개변수는 원본 데이터에 영향을 안준다.
	// call by value
	public static void test(String str) {
		str = "홍길동";
	}
	// 자바의 참조에 의한 호출은 배열(객체 역시 동일)을 매개변수로 전달한 경우를 말함
	public static void func(int a[]) {
		a[0] = 100;
	}
	
	public static void arrayBasic() {
		int iSize = 5;
		// 입력 받은 크기 만큼 할당하는 경우
		//동적 할당 C언어에서 배열은 정적 할당
		int arrData[] = new int[iSize];
		
		//for 문을 이용하여 0~4번지의 값을 출력하여 확인해보자
		for(int i = 0;i<arrData.length;i++) {
			System.out.println(i+"번재 배열 값 :"+arrData[i]);
		}
		// 향상된 for 문 : 읽기 전용
		for(int v : arrData) { // (그냥 변수 : 배열)
			System.out.println(v);
			
		}
		
	}
	
	public static void arrayTest() {
		//크기 5인 배열 생성
		//각 요소를 1~5로 초기화 단 for 문 사용
		//각 요소 총합을 구하고 출력하기 단 향상된 for 문 사용
		
		int iSize = 5,sum = 0;
		int arrData[] = new int[iSize];
		for(int i = 0; i<arrData.length;i++) {
			arrData[i] = i+1;
			System.out.println(i+"번재 배열 값 :"+arrData[i]);
		} 
		for(int v : arrData) { // (변수 {메모리 주소} : 배열)
			sum = sum + v;
		}
		System.out.println("총합 : "+sum);
	}
	
	// 함수 : 4가지 유형
	// 접근 지정자 static 반환 유형 함수 이름(매게변수) {}
	// call by value :  값에 의한 호출
	public static void func2(int i) {
		i = 100;
	}
}