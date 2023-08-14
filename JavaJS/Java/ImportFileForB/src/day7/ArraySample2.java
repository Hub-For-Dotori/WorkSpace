package day7;

import java.util.Random;
import java.util.Scanner;

public class ArraySample2 {
	public static Scanner scan;
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		doublearray();
		pickLotto();
		System.out.print("\n");
		pickLotto1();
		scan.close();
	}
	
	public static void doublearray() {
		int arr[][] = new int[3][3];
		int iNum =0;
		for(int i = 0;i<arr.length;i++) {
			for(int j =0;j<arr[i].length;j++) {
				arr[i][j] = ++iNum;
				System.out.print(arr[i][j]+"\t");
			}
			System.out.print("\n");
		}
	};
	public static void pickLotto() {
		int a[] = new int[6];
		//자바 난수 발생 기능 클래스 (Random , Math)
		//Random 클래스는 new 방식 사용
		//Math 메모리 생성 없이 직접 사용가능
		
		//overload(과적하다) : 하나의 클래스 내에 같은 이름의 함수를 여러개 만들수 있는 기능
		//조건 : 접근 지정장 반환 유형과는 관계 없음
		//매개 변수의 이름과는 상관 없음
		//매개 변수의 개수와 타입이 달라야함
		//상속의 경우 override 라는 기술이 있음.
		
		//override (덮어쓰다, 우선하다)
		Random rand = new Random();
		for(int i=0;i<a.length;i++) {
			a[i]=rand.nextInt(45) + 1;
			
			for(int j=0;j<i;j++) {
				if (a[j] == a[i]) {
					i--;
					break;
				}
			}
		}
		for(int v : a) {
			System.out.print(v+"\t");
		}
	};
	public static void pickLotto1() {
		int a[] = new int[6];
		//자바 난수 발생 기능 클래스 (Random , Math)
		//Random 클래스는 new 방식 사용
		//Math 메모리 생성 없이 직접 사용가능
		
		for(int i=0;i<a.length;i++) {
			a[i]=(int)(Math.random()*45+1);
			for(int j=0;j<i;j++) {
				if (a[j] == a[i]) {
					i--;
					break;
				}
			}
		}
		for(int v : a) {
			System.out.print(v+"\t");
		}
	};

}
