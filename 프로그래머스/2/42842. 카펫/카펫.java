import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int [] answer = new int[2];
        List<Integer> div = getDiv(brown+yellow);
        System.out.println(div.toString());
        for(int i = 0; i<div.size(); i+=2){
            int w = div.get(i);
            int h = div.get(i+1);
            System.out.println(w+","+h);
            if (w>=3 && h>=3 && (w-2)*(h-2)==yellow){
                answer[0] = Math.max(w,h);
                answer[1] = Math.min(w,h);
                break;
            }
        }
        return answer;
    }
    public List<Integer> getDiv(int num){
        List<Integer> div = new ArrayList<>();
        for(int i = 1; i< (int) Math.sqrt(num)+1; i++){
            if (num%i == 0){
                div.add(i);
                div.add(num/i);
            }
        }
        return div;
    }
}