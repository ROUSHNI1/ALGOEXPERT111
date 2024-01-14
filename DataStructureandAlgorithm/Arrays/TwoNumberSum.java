package DataStructureandAlgorithm.Arrays;


class TwoNumberSum{
    public static int[] twoNumberSums(int[] array , int targetsum){
        for(int i = 0; i < array.length -1; i++){
            int firstNum = array[i];
            for(int j = i + 1 ;j < array.length; j++){
                int secondNum = array[j] ;
                if (firstNum + secondNum == targetsum) {
                    return new int[]{firstNum,secondNum};
                }
            }
        }
        return new int[0];
    }
    public static void main(String[] args) {
        int[] array = {3 ,5,-4 ,8, 11,1,-1 ,6};
        int targetsum = 10 ;
        System.out.println("The two numbers that add up to the given sum are: " + twoNumberSums( array, targetsum) );
    }
}