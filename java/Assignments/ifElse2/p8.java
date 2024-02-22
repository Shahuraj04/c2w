/*8. Write a program to check whether the student passed with:
first class with distinction, first class, second class, pass and fail according to his percent
grades. (You have to adjust range by your own for first class, second class and for pass)*/
class p8{
	public static void main(String[] args){
		float perc=8f;
		if(perc>75f){
			System.out.println("Passed:First Class With Distinction.");
		} else if(perc>=60f && perc<=75f){
			System.out.println("Passed:First Class.");
		} else if(perc>=50 && perc<60){
			System.out.println("Passed:Second .");
		} else if(perc>=40 && perc<50){
			System.out.println("Passed:Pass Class.");
		} else{
			System.out.println("Failed.");
		}
	
	}

}
