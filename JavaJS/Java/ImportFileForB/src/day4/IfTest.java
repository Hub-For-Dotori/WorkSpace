package day4;

import java.util.Scanner;

public class IfTest {

	public static void main(String[] args) {
		// �ǽ� ���� : Ű����� ����(��������)�� �Է� �޴´�.
		// �� ���� ����� �Ǵ��Ͻÿ�. 85~89 ���� 100~95������ 94~90����
		// ���� -> �ȳ� -> �����Է� -> ����Ǵ�
		// -> �Է°� ���� ������ ���ΰ�

		// �ʿ� ���� ����
		Scanner scan = new Scanner(System.in);

		// �ȳ� �׸��� �Է�ó��
		System.out.print("�Է� : ");
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
			System.out.println("�߸��� ��");
		scan.close();
		

	}

}
