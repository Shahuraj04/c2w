/*6. Write a program to verify the age of the voter where the age should be positive. (that
means no negative values are allowed, take hardcoded values).*/
class p6{
	public static void main(String[] args){
		byte age = -98;
		if (age>=18){
			System.out.println("Valid Age for Voting.");
		} else if(age<=18 && age>=0){
			System.out.println("Invalid Age for Voting.");
		} else if(age<0){
			System.out.println("Invalid AGE.");
		}
	
	
	}


}
