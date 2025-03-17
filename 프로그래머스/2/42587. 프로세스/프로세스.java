import java.util.*;
import java.io.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Deque<List<Integer>> deque = new ArrayDeque<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for (int i=0; i<priorities.length; i++){
            deque.addLast(Arrays.asList(i,priorities[i]));
            pq.add(priorities[i]);
        }
        while (!deque.isEmpty()){
            List<Integer> process = deque.pollFirst();
            if (process.get(1)==pq.peek()){
                pq.poll();
                answer++;
                if (process.get(0) == location){
                    return answer;
                }
            }else{
                deque.addLast(process);
            }
        }
        return answer;
    }
}