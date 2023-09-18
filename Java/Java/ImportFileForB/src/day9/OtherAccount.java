package day9;

public class OtherAccount {
	
	private String other_b_n;
	private String other_a_n;
	private String other_u_n;
	private int other_b_b;
	
	public OtherAccount(String _other_b_n, String _other_a_n, String _other_u_n, int _other_b_b) {
		other_b_n = _other_b_n;
		other_a_n = _other_a_n;
		other_u_n = _other_u_n;
		other_b_b = _other_b_b;
	}


	public String getOther_b_n() {
		return other_b_n;
	}
	public void setOther_b_n(String other_b_n) {
		this.other_b_n = other_b_n;
	}
	public String getOther_a_n() {
		return other_a_n;
	}
	public void setOther_a_n(String other_a_n) {
		this.other_a_n = other_a_n;
	}
	public String getOther_u_n() {
		return other_u_n;
	}
	public void setOther_u_n(String other_u_n) {
		this.other_u_n = other_u_n;
	}
	public int getOther_b_b() {
		return other_b_b;
	}
	public void setOther_b_b(int other_b_b) {
		this.other_b_b = other_b_b;
	}


	
	
	public void Remittance() {
		System.out.println("송금 할 은행 명을 넣어주세요 : ");
		
	}
	
	public void withdrawal() {
		System.out.println("출금 금액을 입력해주세요 : ");
	}
	
}
