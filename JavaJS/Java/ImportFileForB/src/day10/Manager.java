package day10;

// 알아둬야 하는 디자인 패턴 종류 : 싱글턴, 팩토리, 스테이트, 스트레티지 ( 공부하기 노트에 정리 : 과제 ) 

public class Manager {
	private String strName;
	private static Manager m; // 자동 초기화 : null (최초 1회)
	
	public String getName() { //외부에서 값 가져 올 때 사용
		return strName;
	}
	
	private Manager() {
		
	}
	
	private Manager(String name) {
		strName = name;
	} // 오버로딩하여 외부값을 넣어 초기화 해줌
	
	public static Manager getInstance(String name) {
		if (m == null) { // 한 개만 생성 하게 조건을 만듦.
			m = new Manager(name); // 객체 생성
		}// 생성한 것이 있으면 생성 안함.  
		return m;
	}

	
}
