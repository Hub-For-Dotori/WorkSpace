package day3;

public class VarSample {

	public static void main(String[] args) {
		String strName = "ȫ��ȣ";
		int iYear = 2022, iMonth = 3, iDate = 22;
		
		int iAge = 22;
				
		byte bGender = 3;
		char cGender = 'F'; 
		
		boolean isMale = false;
		
		String strGender = "����";
		
		System.out.println(strName +"�� " + iYear + "�� " +
				iMonth +"�� " + iDate +"�� ���� " + "����: " + iAge + " ��");
		
		// ������ �� �� ���� ���� ������ ���� 3���� �����ϰ� �ʱ�ȭ �Ͻÿ�.
		// �ǽ� : ����� ���� ����ϴµ� �Ʒ��� ���� ����Ͻÿ�.
		// "������ 2022�� 3�� 22�� �Դϴ�."
		System.out.println("������ " + iYear + "�� " + iMonth + "�� " + iDate + "���Դϴ�.");

		// �й��� ������ ������ �����ϰ� �ʱ�ȭ �Ͻÿ�.

		int iStudentNum = 2021181976;
		String StrGender = "����";
		System.out.println("�й��� " + iStudentNum + "�� ����� ������ " + StrGender + "�Դϴ�.");

		System.out.println("�ڵ� : "+ bGender);
		
		if (bGender == 1 || bGender == 3) {
			System.out.println("����");
		} 
		else if (bGender == 2 || bGender == 4){
			System.out.println("����");
		}
		else System.out.println("����");
		
		
		
		
		
	}

}
