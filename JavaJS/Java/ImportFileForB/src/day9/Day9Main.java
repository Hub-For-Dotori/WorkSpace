package day9;

import java.util.Scanner;

public class Day9Main {
	public static Scanner scan;
	public static void main(String[] args) {
		
		scan = new Scanner(System.in);
		// TODO Auto-generated method stub
		Student s1 = new Student("ȫ��ȣ","��ǻ�Ͱ���",2);// Ŭ������ ��ü�� = new ������();          ��ü �ϳ� ����
		
		
		Student s2 = new Student("�ӿ���","��ǻ�Ͱ���",3);
	
		
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
		
		System.out.println("s1�� �̸� : "+s1.name);
		System.out.println("s2�� �̸� : "+s2.name);
		
		System.out.println("h1�� �̸� : "+ h1.name + " h1�� ���� : "+ h1gen + " h1�� ���� : "+ h1.age);
		System.out.println("h2�� �̸� : "+ h2.name + " h2�� ���� : "+ h2gen + " h2�� ���� : "+ h2.age);
		
		// ������ : �Լ���. ��ü ������ ���� ȣ��Ǵ� �Լ���.
		// ���� : ���� ������ �Լ��� (){} -> ��ȯ ���� ����
		// �������� �̸��� Ŭ������ �̸��� �����ϴ�. -> �����ϰ� �빮�ڷ� �����ϴ� �Լ��̴�.
		// �ɹ����� �ʱ�ȭ �ڵ带 �ۼ��Ѵ�.
		// �⺻ ������(�Ű������� ���� �����ڴ� ������ ������)
		// ���� �Ұ��� ��쵵 ����.
		// ������ ���� �Լ��� �����ε��� �����ϴ�.
		// �����ڸ� �����ε��ϰ� �⺻ �����ڰ� ������ ��� �⺻ �����ڷ� ��ü�� ���� �� �� ����.
		// �̷��� ��� �⺻ �����ڸ� �ۼ��ϰų� �⺻ �����ڷ� ��ü�� �����ϸ� �ȵȴ�.
		
//		Book b1 = new Book();
//		b1.title = "�ظ�����";
//		b1.price = 20000;
//		System.out.println("���� : " + b1.title);
		
		Book b2 = new Book("�ڹ� ���α׷���",30000);
		b2.setTitle("�ڹ�����");
		System.out.println("���� : " + b2.getTitle());
		
		Book a[] = new Book[5];
		for(int i = 0;i<a.length;i++) {
			a[i] = new Book();
			a[i].setTitle("test"+i);
		}
		//���� ���� Ŭ���� �� �� �۱� ����� ( Ŭ���� �̿� account ): ���� �̸�, ��ȣ, �ܾ�
		Account a1 = new Account("KB ����","2131321321321","���¿�",1000000);
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
