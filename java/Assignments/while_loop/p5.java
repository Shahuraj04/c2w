public class p5 {
    public static void main(String[] args) {
        int row = 4;
        int n = 1;
        int i = 1;
        while (i <= row) {
            int j = 1; 
            while (j <= row) {
		if(n%2==1){
                	System.out.print(n + " ");
                }
		n+=2;
                j++;
            }
            System.out.println();
	    i++;
        }
    }
}

