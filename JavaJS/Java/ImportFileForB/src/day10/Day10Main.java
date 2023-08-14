package day10;

public class Day10Main {

	public static void main(String[] args) {
		Student.iCnt = 100;
		
		Student s1 = new Student();
		s1.strName = "홍길동";
		s1.iCnt = 1;
		//Student.iCnt = 1;
		
		Student s2 = new Student();
		s2.strName = "마이콜";
		s2.iCnt = 2;
		
		System.out.println(s1.iCnt);
		System.out.println(s2.iCnt);
		// 클래스 변수는 static 맴버 변수를 말함
		// static은 메모리를 고정하고 해당 메모리를 공유해 사용.
		// 클래스 변수는 객체 생성 없이 (인스턴스 없이) 접근이 가능한 변수
		// 클래스명.클래스 변수 = 대입 값;
		
		
		Manager man = Manager.getInstance("홍길동");
		System.out.println(man.getName());
		Manager man2 = Manager.getInstance("마이콜");//Manager에서 이미 생성을 한 경우로 생성 안됨.
		System.out.println(man2.getName());
		
		
		//상속
		Dove d = new Dove();
		d.fly();
		d.fromEgg();
		d.walk();
		
		
	}

}
