package day11;

public interface Move {
	public int x = 0 , y = 0;
	
	public void move(int x, int y);//abstract »ý·«
	
	default void boost(int boost) {
		System.out.println("as");
	}
	public static void jump() {
		System.out.println("sa");
	}
}
