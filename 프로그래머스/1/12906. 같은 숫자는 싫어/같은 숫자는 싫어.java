import java.util.*;
import java.io.*;

public class Solution {
    public int[] solution(int []arr) {
        Deque<Integer> answer = new ArrayDeque<>();
        for(int i=0; i<arr.length; i++){
            if (answer.isEmpty()||answer.peekLast()!=arr[i]){
                answer.addLast(arr[i]);
            }
        }
        
        int [] result = new int[answer.size()];

        int size = answer.size();
        for(int j=0; j<size; j++){
            result[j] = answer.pollFirst();
        }
        return result;
    }
}