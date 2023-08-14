package day7;

import java.util.Random;
import java.util.Scanner;

public class ArraySample2 {
	public static Scanner scan;
	public static void main(String[] args) {
		scan = new Scanner(System.in);
		doublearray();
		pickLotto();
		System.out.print("\n");
		pickLotto1();
		scan.close();
	}
	
	public static void doublearray() {
		int arr[][] = new int[3][3];
		int iNum =0;
		for(int i = 0;i<arr.length;i++) {
			for(int j =0;j<arr[i].length;j++) {
				arr[i][j] = ++iNum;
				System.out.print(arr[i][j]+"\t");
			}
			System.out.print("\n");
		}
	};
	public static void pickLotto() {
		int a[] = new int[6];
		//�ڹ� ���� �߻� ��� Ŭ���� (Random , Math)
		//Random Ŭ������ new ��� ���
		//Math �޸� ���� ���� ���� ��밡��
		
		//overload(�����ϴ�) : �ϳ��� Ŭ���� ���� ���� �̸��� �Լ��� ������ ����� �ִ� ���
		//���� : ���� ������ ��ȯ �������� ���� ����
		//�Ű� ������ �̸����� ��� ����
		//�Ű� ������ ������ Ÿ���� �޶����
		//����� ��� override ��� ����� ����.
		
		//override (�����, �켱�ϴ�)
		Random rand = new Random();
		for(int i=0;i<a.length;i++) {
			a[i]=rand.nextInt(45) + 1;
			
			for(int j=0;j<i;j++) {
				if (a[j] == a[i]) {
					i--;
					break;
				}
			}
		}
		for(int v : a) {
			System.out.print(v+"\t");
		}
	};
	public static void pickLotto1() {
		int a[] = new int[6];
		//�ڹ� ���� �߻� ��� Ŭ���� (Random , Math)
		//Random Ŭ������ new ��� ���
		//Math �޸� ���� ���� ���� ��밡��
		
		for(int i=0;i<a.length;i++) {
			a[i]=(int)(Math.random()*45+1);
			for(int j=0;j<i;j++) {
				if (a[j] == a[i]) {
					i--;
					break;
				}
			}
		}
		for(int v : a) {
			System.out.print(v+"\t");
		}
	};

}
