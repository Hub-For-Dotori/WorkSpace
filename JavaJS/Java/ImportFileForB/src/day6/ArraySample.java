package day6;

import java.util.Scanner;

public class ArraySample {
	public static Scanner scan;
	//�ɹ� ���� ���� : �ɹ� ������ ����� ���ÿ� �ʱ�ȭ ���� ����
	//�ɹ� ������ �ڵ����� �ʱ�ȭ �� => �� �ش� �ڷ��� �⺻������ �ʱ�ȭ ��
	//Ŭ������ ������ ������ ��ü ������ ��. => ��ü ������ �ڵ� �ʱ�ȭ�� ���� NULL��. 
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		//arrayBasic();
		//arrayTest();
		//int i=0;
		int a[] =new int[3];
		//String str ="�Ѹ�";
		//func2(i);
		//System.out.println(i);
		func(a);
		System.out.println(a[0]);// call by reference : ������ ���� ȣ��
		//test(str);
		//System.out.println(str);//
		//String strArray[] = new String[5];
		//for(String v : strArray) {
			//System.out.println(v);
		//}
		String strArray[] = new String[5]; //18��
		String str[] = {"�Ѹ�","��浿","ȫ�浿","������"};
		
		System.out.println("strArray[0] �ּ� : "+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("���� strArray[0]�� �� : \n"+strArray[0]+"\n\n");
		System.out.println("strTest() ���� ��..\n\n");
		
		strTest(strArray);  // �Լ��� ����ǰ� strArray�� ������ ���� �ʾƾ� �ϳ� �ʱ�ȭ�� ���� ���·� �⺻ ������ �ּҰ� null�̿��� �� ���� strTest���� ������ �������� �ּ� ���� �����Ե�
		
		System.out.println("strTest() ����\n\n");
		System.out.println("strTest�� ��ģ \nstrArray[0] �ּ� : "+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("srtTest�� ��ģ \nstrArray[0]�� �� : \n"+strArray[0]); //���� ��� ���� ���ϰ� �Ȱ�
		
		scan.close();
		
	}
	// �� 18�� ������ �迭�� �Լ� strTest()�� �Ű������� ��������!
	// �Լ� ���ο��� 0���� ���� �����ݷ� ��������
	// ������ ������ ��ġ�� �� Ȯ�� ����
	public static void strTest(String str[]) {
		str[0] = "������";                       //strArray�� str�� ����Ͽ� ���ڷ� �־��ְ� �� str�� �迭 0��°�� �������̶� ��. 
		System.out.println("strArray[0] �ּ� : "+System.identityHashCode(str[0])+"\n\n");
	}
	// ������ �Ű������� String Ÿ���� �Ű������� ���� �����Ϳ� ������ ���ش�.
	// call by value
	public static void test(String str) {
		str = "ȫ�浿";
	}
	// �ڹ��� ������ ���� ȣ���� �迭(��ü ���� ����)�� �Ű������� ������ ��츦 ����
	public static void func(int a[]) {
		a[0] = 100;
	}
	
	public static void arrayBasic() {
		int iSize = 5;
		// �Է� ���� ũ�� ��ŭ �Ҵ��ϴ� ���
		//���� �Ҵ� C���� �迭�� ���� �Ҵ�
		int arrData[] = new int[iSize];
		
		//for ���� �̿��Ͽ� 0~4������ ���� ����Ͽ� Ȯ���غ���
		for(int i = 0;i<arrData.length;i++) {
			System.out.println(i+"���� �迭 �� :"+arrData[i]);
		}
		// ���� for �� : �б� ����
		for(int v : arrData) { // (�׳� ���� : �迭)
			System.out.println(v);
			
		}
		
	}
	
	public static void arrayTest() {
		//ũ�� 5�� �迭 ����
		//�� ��Ҹ� 1~5�� �ʱ�ȭ �� for �� ���
		//�� ��� ������ ���ϰ� ����ϱ� �� ���� for �� ���
		
		int iSize = 5,sum = 0;
		int arrData[] = new int[iSize];
		for(int i = 0; i<arrData.length;i++) {
			arrData[i] = i+1;
			System.out.println(i+"���� �迭 �� :"+arrData[i]);
		} 
		for(int v : arrData) { // (���� {�޸� �ּ�} : �迭)
			sum = sum + v;
		}
		System.out.println("���� : "+sum);
	}
	
	// �Լ� : 4���� ����
	// ���� ������ static ��ȯ ���� �Լ� �̸�(�ŰԺ���) {}
	// call by value :  ���� ���� ȣ��
	public static void func2(int i) {
		i = 100;
	}
}