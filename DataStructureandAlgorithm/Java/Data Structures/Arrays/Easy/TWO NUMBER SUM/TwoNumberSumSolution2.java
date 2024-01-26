
import java.util.*;
public class TwoNumberSumSolution2 {
    //O(n) time | O(n) space
    public static int[] twoNumberSum(int[] array, int targetSum) {
        // Write your code here.
        //using nested for loop to check two random elment of given array sum is equal to the targetSum
        Set<Integer> nums = new HashSet<>();
        for(int num : array){
          int potentialMatch = targetSum - num ;
            if (nums.contains(potentialMatch)){
              return new int[] {potentialMatch, num};
        
            }else{
                nums.add(num);
            }
          
        }
        return new int[0];
      
    }

    public static void main(String[] args){

        int [] array = {3, 5, -4, 8, 11, 1, -1, 6};
        int targetSum = 10;
        System.out.println("The pair which is equal to target sum is : " +(Arrays.toString(twoNumberSum( array , targetSum) )) );

    }

}
