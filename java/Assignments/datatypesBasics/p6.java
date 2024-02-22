class Calendar{
	public static void main(String[] args){
		byte date=01;
		byte month=01;
		String monthS="January";
		int year=2024;

		int secDay=60*60*24;
		int secMonth=secDay*31;
		int secYear=secMonth*12;

		System.out.println("Date is:"+date+":"+monthS+":"+year);
		System.out.println("Seconds in a Day:"+secDay);
		System.out.println("Seconds in a Month:"+secMonth);
		System.out.println("Seconds in A Year:"+secYear);	
	}

}
