import java.util.*;
import java.io.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int[] rest = new int[progresses.length];
        // 각 프로세스마다 배포 며칠씩 걸리는지 추가
        for(int i=0; i<rest.length; i++){
            rest[i] = ((100-progresses[i])+speeds[i]-1)/speeds[i];
        }
        System.out.println(Arrays.toString(rest));
        int count = 1;
        int maxDay = rest[0];
        
        for(int j=1; j<rest.length; j++){
            if(rest[j]>maxDay){
                answer.add(count);
                count = 1;
                maxDay = rest[j];
            }else{
                count++;
            }
        }
        answer.add(count);
        
        System.out.println(answer);
        int[] result = new int[answer.size()];
        for(int i=0; i<answer.size(); i++){
            result[i] = answer.get(i);
        }
        return result;
        
    }
}