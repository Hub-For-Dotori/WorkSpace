package day11_abstract;

public class Triangle extends Shape implements Figure{
	private int width, height;
	public Triangle(int w, int h) {
		width = w;
		height = h;
	}
	@Override
	
	public void getArea() {
		// TODO Auto-generated method stub
		System.out.println(width + "*" + height + "=" + (width * height));
	}

	@Override
	public void draw() {
		// TODO Auto-generated method stub
		System.out.println("일을 냈지 난 그림 그리기 직전의");
	}
}
