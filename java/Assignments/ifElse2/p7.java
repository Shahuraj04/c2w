/*7. Calculate the profit or loss.
Write a program that takes cost price and selling price(take it hardcoded) and calculates its
profit or loss.*/
class p7{
	public static void main(String[] args){
		int sP=1000;
		int cP=1200;
		int diff=sP-cP;
		if (diff>0){
			System.out.println("Profit Of "+diff);
		} else if(diff<0){
			System.out.println("Loss of :"+(-1*diff));
		} else if(sP==cP){
			 System.out.println("No profit no loss.");
		} 
	
	}

}
