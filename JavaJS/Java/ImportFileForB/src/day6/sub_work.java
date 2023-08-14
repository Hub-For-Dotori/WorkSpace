package day6;

import java.util.Scanner;

public class sub_work {
	public static Scanner scan; 
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		String strArray[] = new String[5]; 
		String str[] = {"둘리","고길동","홍길동","마이콜"};
		
		System.out.println("strArray[0] 주소 : "+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("원래 strArray[0]의 값 : \n"+strArray[0]+"\n\n");
	
		System.out.println("strTest() 실행 중\n\n");
		strTest(strArray);  
		System.out.println("strTest() 종료\n\n");
		
		System.out.println("strTest를 거친 \nstrArray[0] 주소 : \n"+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("srtTest를 거친 \nstrArray[0]의 값 : \n"+strArray[0]);
		
		scan.close();
		
	}
	public static void strTest(String str[]) {
		str[0] = "마이콜";               
		System.out.println("strArray[0] 주소 : \n"+System.identityHashCode(str[0])+"\n\n");
	}
	
}