package day3;

import java.util.Scanner;

// ctrl + shift + o
public class InputSample {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		// ���� 2���� ������ ���� �ʿ�
		int iNum1 = 0, iNum2 = 0;
		
		// �Է¾ȳ����� ���
		System.out.print("���� �Է�: ");
		// ù��° ������ ���� �Է� �޴´�.
		iNum1 = scan.nextInt();
		System.out.println("�Է� �� : "+iNum1);
		// �ι�° ������ �� �Է�
		System.out.print("���� �Է�: ");
		// �ι�° ������ ���� �Է� �޴´�.
		iNum2 = scan.nextInt();
		System.out.println("�Է� �� : "+iNum1);
		//���� : 0���� ������ ��� ���� �߻� 
		//�� ������ ��� �߰�
		//�ۼ��� �ҽ� �ڵ� ��� ��� ���ο� �ּ� �ۼ�
		//��, �ڵ� ������(������) �ۼ�
		// ��� ���
		System.out.println("���� ���: " +(iNum1 + iNum2));
		System.out.println("���� ���: " +(iNum1 - iNum2));
		System.out.println("���� ���: " +(iNum1 * iNum2));
		System.out.println("������ ���: " +(iNum1 / iNum2));
		
		
		scan.close();

	}

}
