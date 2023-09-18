package day3;

public class VarSample {

	public static void main(String[] args) {
		String strName = "홍진호";
		int iYear = 2022, iMonth = 3, iDate = 22;
		
		int iAge = 22;
				
		byte bGender = 3;
		char cGender = 'F'; 
		
		boolean isMale = false;
		
		String strGender = "남자";
		
		System.out.println(strName +"는 " + iYear + "년 " +
				iMonth +"월 " + iDate +"일 현재 " + "나이: " + iAge + " 세");
		
		// 오늘의 년 월 일을 저장 가능한 변수 3개를 선언하고 초기화 하시오.
		// 실습 : 년월일 값을 출력하는데 아래와 같이 출력하시오.
		// "오늘은 2022년 3월 22일 입니다."
		System.out.println("오늘은 " + iYear + "년 " + iMonth + "월 " + iDate + "일입니다.");

		// 학번을 저장할 변수를 선언하고 초기화 하시오.

		int iStudentNum = 2021181976;
		String StrGender = "남자";
		System.out.println("학번이 " + iStudentNum + "인 사람의 성별은 " + StrGender + "입니다.");

		System.out.println("코드 : "+ bGender);
		
		if (bGender == 1 || bGender == 3) {
			System.out.println("남자");
		} 
		else if (bGender == 2 || bGender == 4){
			System.out.println("여자");
		}
		else System.out.println("오류");
		
		
		
		
		
	}

}
