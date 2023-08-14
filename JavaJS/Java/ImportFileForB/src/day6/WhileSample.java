package day6;

import java.util.Scanner;

public class WhileSample {
	public static Scanner scan;
	//�ɹ� ���� ���� : �ɹ� ������ ����� ���ÿ� �ʱ�ȭ ���� ����
	//�ɹ� ������ �ڵ����� �ʱ�ȭ �� => �� �ش� �ڷ��� �⺻������ �ʱ�ȭ ��
	//Ŭ������ ������ ������ ��ü ������ ��. => ��ü ������ �ڵ� �ʱ�ȭ�� ���� NULL��. 
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		whilebasic();
		dowhilebasic();
		infiniteWhile();
		scan.close();
	}
	
	public static void whilebasic() {
		int iNum = 1;
		while(iNum != 0) {
			System.out.print("�Է� : ");
			iNum =scan.nextInt();
			System.out.println("�� : "+iNum);	
		}
		System.out.println("0�� �Է� : �Լ� ����");
	}
	public static void dowhilebasic() {
		int iNum = 1;
		
		do {
			System.out.print("�Է� : ");
			iNum =scan.nextInt();
			System.out.println("�� : "+iNum);	
		} while(iNum != 0);
		
		System.out.println("0�� �Է� : �Լ� ����");
	}
	public static void infiniteWhile() {
		int iNum =0;
		while (true) {
			System.out.print("�Է� : ");
			iNum =scan.nextInt();
			System.out.println("�� : "+iNum);
			if(iNum == 0) break; 
			// ��� �ڽ��� ���� ���� ����� �ڵ�
		}
		System.out.println("�ݺ� ����");
	}

}