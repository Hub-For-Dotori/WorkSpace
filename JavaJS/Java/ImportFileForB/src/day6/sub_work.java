package day6;

import java.util.Scanner;

public class sub_work {
	public static Scanner scan; 
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		String strArray[] = new String[5]; 
		String str[] = {"�Ѹ�","��浿","ȫ�浿","������"};
		
		System.out.println("strArray[0] �ּ� : "+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("���� strArray[0]�� �� : \n"+strArray[0]+"\n\n");
	
		System.out.println("strTest() ���� ��\n\n");
		strTest(strArray);  
		System.out.println("strTest() ����\n\n");
		
		System.out.println("strTest�� ��ģ \nstrArray[0] �ּ� : \n"+System.identityHashCode(strArray[0])+"\n\n");
		System.out.println("srtTest�� ��ģ \nstrArray[0]�� �� : \n"+strArray[0]);
		
		scan.close();
		
	}
	public static void strTest(String str[]) {
		str[0] = "������";               
		System.out.println("strArray[0] �ּ� : \n"+System.identityHashCode(str[0])+"\n\n");
	}
	
}