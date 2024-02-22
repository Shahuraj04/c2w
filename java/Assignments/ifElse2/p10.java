/*10. Write a program, where you have to write a real time example.(It should be unique and
thought by your own)*/
class p10{
	public static void main(String[] args){
		int target=320;
		int score=319;
		int overs=50;
		int overs_rem=0;
		int need=target-score;
		int rem= overs-overs_rem;
		int balls=rem*6;
		if (target>score && overs_rem!=0){
			System.out.println("Need "+ need +" in "+balls+" balls.");
		} else if(score==320){
			System.out.println("Won match with "+ balls +" balls remaining.");
		} else if(overs_rem==0 && overs_rem!=0){
			System.out.println("Lost match with "+ need +" runs");		
		} else if(score== target - 1 && overs_rem==0 ){
			System.out.println("Match Tied.");
		}
	
	}

}
