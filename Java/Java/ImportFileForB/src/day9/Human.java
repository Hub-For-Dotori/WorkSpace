package day9;

public class Human {
	public String name;
	public boolean gender;
	public int age;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public boolean isGender() {
		return gender;
	}
	public void setGender(boolean gender) {
		this.gender = gender;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public Human(String _name, boolean _gender, int _age) {
		name = _name;
		gender = _gender;
		age = _age;
	}

}
