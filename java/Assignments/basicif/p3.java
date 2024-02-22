class p3{
	public static void main(String[] args){
		int num1=13;
		int num2=8;
		int num3=10;

		if(num1%2==1 && num2>10) {
			System.out.println(num1+" is an odd Number and greater than 10.");
		} else {
			System.out.println(num1+" is an Even Number & less than 10.");
		}

		if(num2%2==0 && num2<10) {
			System.out.println(num2+" is Even number & less than 10.");
		}

		if(num3%2==0 && num3==10) {
			System.out.println(num3+" is an Even Number & equal to 10");
		}
	}
}
