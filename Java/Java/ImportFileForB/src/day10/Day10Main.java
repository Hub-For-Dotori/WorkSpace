package day10;

public class Day10Main {

	public static void main(String[] args) {
		Student.iCnt = 100;
		
		Student s1 = new Student();
		s1.strName = "ȫ�浿";
		s1.iCnt = 1;
		//Student.iCnt = 1;
		
		Student s2 = new Student();
		s2.strName = "������";
		s2.iCnt = 2;
		
		System.out.println(s1.iCnt);
		System.out.println(s2.iCnt);
		// Ŭ���� ������ static �ɹ� ������ ����
		// static�� �޸𸮸� �����ϰ� �ش� �޸𸮸� ������ ���.
		// Ŭ���� ������ ��ü ���� ���� (�ν��Ͻ� ����) ������ ������ ����
		// Ŭ������.Ŭ���� ���� = ���� ��;
		
		
		Manager man = Manager.getInstance("ȫ�浿");
		System.out.println(man.getName());
		Manager man2 = Manager.getInstance("������");//Manager���� �̹� ������ �� ���� ���� �ȵ�.
		System.out.println(man2.getName());
		
		
		//���
		Dove d = new Dove();
		d.fly();
		d.fromEgg();
		d.walk();
		
		
	}

}
