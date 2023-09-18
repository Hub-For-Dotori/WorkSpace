package day9;

public class Student {
	// 속성 : 학생이 갖을 수 있는 정보들
	// 접근 제어자 자료형 변수명;
	public String name; // 맴버 변수는 초기화 불필요! -> 객체 생성시 자동 초기화 (기본값)
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
