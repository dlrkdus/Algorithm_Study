import java.util.*;
import java.io.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<String> stack = new Stack<>();
        for(char a:s.toCharArray()){
            if(a=='('){
                stack.push(String.valueOf(a));
            }else{
                if (stack.isEmpty()){
                    return false;
                }else{
                    stack.pop();
                }
            }
        }
        

        return stack.isEmpty();
    }
}