package day3;

import java.util.Scanner;

public class work1 {
	public static void main(String[] args) {
		//���� : 0���� ������ ��� ���� �߻� 
		//�� ������ ��� �߰�
		//�ۼ��� �ҽ� �ڵ� ��� ��� ���ο� �ּ� �ۼ�
		//��, �ڵ� ������(������) �ۼ�
		Scanner scan = new Scanner(System.in);
		int a=0, b=0;
		
		System.out.print("���� �Է�: ");
		a = scan.nextInt();
		System.out.println("�Է� �� : "+ a);
		
		System.out.print("���� �Է�: ");
		b = scan.nextInt();
		System.out.println("�Է� �� : "+ b);
		
		System.out.println("���� ���: " + (a+b));
		System.out.println("���� ���: " + (a-b));
		System.out.println("���� ���: " + (a*b));
		
		if(b != 0 && a !=0) System.out.println("������ ���: " +(a/b));
		else System.out.println("���� �� �Է� �� �� �� �� �Ǵ� �� ���� \n0�� ���� �Ǿ� ������ �Ұ��մϴ�.");         
		
		
		scan.close();
	}
	
}
