package day9;

public class Student {
	// �Ӽ� : �л��� ���� �� �ִ� ������
	// ���� ������ �ڷ��� ������;
	public String name; // �ɹ� ������ �ʱ�ȭ ���ʿ�! -> ��ü ������ �ڵ� �ʱ�ȭ (�⺻��)
	public String dept;
	public int degree;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getDept() {
		return dept;
	}
	public void setDept(String dept) {
		this.dept = dept;
	}
	public int getDegree() {
		return degree;
	}
	public void setDegree(int degree) {
		this.degree = degree;
	}
	public Student(String _name,String _dept, int _degree) {
		name = _name;
		dept = _dept;
		degree = _degree;
	}
}
