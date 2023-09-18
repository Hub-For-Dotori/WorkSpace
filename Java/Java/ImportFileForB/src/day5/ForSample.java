package day5;

import java.util.Scanner;

public class ForSample {
	public static Scanner scan = new Scanner(System.in);
	public static void main(String[] args) {
		prnRightTri();
		scan.close();
	}
	
	public static void prnRightTri() {
		for(int i = 0;i<5;i++) {
			for(int j = 0;j<5;j++) {
				if((4-i-j)>0) System.out.print(" ");
				else System.out.print("*");
			}
			System.out.println("");
		}
	}

}