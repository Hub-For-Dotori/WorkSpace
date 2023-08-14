package day10;

// �˾Ƶ־� �ϴ� ������ ���� ���� : �̱���, ���丮, ������Ʈ, ��Ʈ��Ƽ�� ( �����ϱ� ��Ʈ�� ���� : ���� ) 

public class Manager {
	private String strName;
	private static Manager m; // �ڵ� �ʱ�ȭ : null (���� 1ȸ)
	
	public String getName() { //�ܺο��� �� ���� �� �� ���
		return strName;
	}
	
	private Manager() {
		
	}
	
	private Manager(String name) {
		strName = name;
	} // �����ε��Ͽ� �ܺΰ��� �־� �ʱ�ȭ ����
	
	public static Manager getInstance(String name) {
		if (m == null) { // �� ���� ���� �ϰ� ������ ����.
			m = new Manager(name); // ��ü ����
		}// ������ ���� ������ ���� ����.  
		return m;
	}

	
}
