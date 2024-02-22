class NumberGridPattern {
    public static void main(String[] args) {
        int numRows = 5;
        int numCols = 4;

        // Iterate through each row
        for (int i = 0; i < numRows; i++) {
            int currentValue = 1;

            // Iterate through each column
            for (int j = 0; j < numCols; j++) {
                System.out.print(currentValue + " ");

                // Update the current value according to the pattern logic
                currentValue += i + 1 + j * (i + 1);
            }

            // Move to the next line after printing each row
            System.out.println();
        }
    }
}

