package day9;

public class Account {
	
	private String bank_name;
	private String account_num;
	private String user_name;
	private int bank_balance;
	
	public Account(String _bank_name, String _account_num, String _user_name, int _bank_balance) {
		bank_name = _bank_name;
		account_num = _account_num;
		user_name = _user_name;
		bank_balance = _bank_balance;
	}

	public String getBank_name() {
		return bank_name;
	}
	public void setBank_name(String bank_name) {
		this.bank_name = bank_name;
	}
	public String getAccount_num() {
		return account_num;
	}
	public void setAccount_num(String account_num) {
		this.account_num = account_num;
	}
	public String getUser_name() {
		return user_name;
	}
	public void setUser_name(String user_name) {
		this.user_name = user_name;
	}
	public int getBank_balance() {
		return bank_balance;
	}
	public void setBank_balance(int bank_balance) {
		this.bank_balance = bank_balance;
	}
	
	
	
	public void Remittance() {
		String bank, accountNum;
		int min_money;
		System.out.println("송금 할 은행 명을 넣어주세요 : ");
		bank = Day9Main.ForStrInput();
		System.out.println("송금 할 계좌를 넣어주세요 : ");
		accountNum = Day9Main.ForStrInput();
		System.out.println("입금 할 계좌 : "+ bank + " " + accountNum);
		System.out.println("송금 할 금액을 넣어주세요 : ");
		min_money = Day9Main.ForIntInput();
		bank_balance = bank_balance - min_money;
		System.out.println("잔액 : " + bank_balance);
	}
	
	public void withdrawal() {
		int min_money;
		System.out.println("출금 금액을 입력해주세요 : ");
		min_money = Day9Main.ForIntInput();
		bank_balance = bank_balance - min_money;
		System.out.println("잔액 : " + bank_balance);
	}

}
