package day9;

public class Book {
	private String title;
	private int price;
	public Book() {
		title = "";
		price = 0;
	}
	// this 객체 : 자신의 맴버를 참조하는 참조 변수
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	public Book(String _title, int _price) {
		title = _title;
		price = _price;
	}

}
