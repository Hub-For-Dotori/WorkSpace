package day9;

import java.util.Scanner;

public class Day9Main {
	public static Scanner scan;
	public static void main(String[] args) {
		
		scan = new Scanner(System.in);
		// TODO Auto-generated method stub
		Student s1 = new Student("홍진호","컴퓨터공학",2);// 클래스명 객체명 = new 생성자();          객체 하나 생성
		
		
		Student s2 = new Student("임요한","컴퓨터공학",3);
	
		
		Human h1 = new Human("stella",false,21);
		Human h2 = new Human("steve",true,22);
		
		String h1gen;
		String h2gen;
		
		if (h1.gender != false) {
			h1gen = "male";
		}
		else h1gen = "female";
		
		if (h2.gender != false) {
			h2gen = "male";
		}
		else h2gen = "female";
		
		Tv t1 = new Tv();
		
		System.out.println("s1의 이름 : "+s1.name);
		System.out.println("s2의 이름 : "+s2.name);
		
		System.out.println("h1의 이름 : "+ h1.name + " h1의 성별 : "+ h1gen + " h1의 나이 : "+ h1.age);
		System.out.println("h2의 이름 : "+ h2.name + " h2의 성별 : "+ h2gen + " h2의 나이 : "+ h2.age);
		
		// 생성자 : 함수임. 객체 생성시 최초 호출되는 함수임.
		// 형식 : 접근 지정자 함수명 (){} -> 반환 유형 없음
		// 생성자의 이름은 클래스의 이름과 동일하다. -> 유일하게 대문자로 시작하는 함수이다.
		// 맴버들의 초기화 코드를 작성한다.
		// 기본 생성자(매개변수가 없는 생성자는 생략이 가능함)
		// 생략 불가한 경우도 있음.
		// 생성자 역시 함수로 오버로딩이 가능하다.
		// 생성자를 오버로딩하고 기본 생성자가 생략된 경우 기본 생성자로 객체를 생성 할 수 없다.
		// 이러한 경우 기본 생성자를 작성하거나 기본 생성자로 객체를 생성하면 안된다.
		
//		Book b1 = new Book();
//		b1.title = "해리포터";
//		b1.price = 20000;
//		System.out.println("제목 : " + b1.title);
		
		Book b2 = new Book("자바 프로그래밍",30000);
		b2.setTitle("자바응용");
		System.out.println("제목 : " + b2.getTitle());
		
		Book a[] = new Book[5];
		for(int i = 0;i<a.length;i++) {
			a[i] = new Book();
			a[i].setTitle("test"+i);
		}
		//계좌 내는 클래스 출 입 송금 만들기 ( 클래스 이용 account ): 은행 이름, 번호, 잔액
		Account a1 = new Account("KB 국민","2131321321321","권태웅",1000000);
		System.out.println(a1.getBank_name()+" : "+a1.getAccount_num()+" : "+a1.getUser_name()+" : "+a1.getBank_balance());
		a1.Remittance();
		a1.withdrawal();
		
		scan.close();
		
		
	}
	public static String ForStrInput() {
		String str;
		str = scan.nextLine();
		return str;
	}
	public static int ForIntInput() {
		int a;
		a = scan.nextInt();
		return a;
	}
}
