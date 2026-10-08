import java.util.*;
class Solution {
    public String removeOuterParentheses(String s) {
        Stack<Character> stk = new Stack<>();
        StringBuilder r=new StringBuilder();
        for(int i=0;i<s.length();i++){
            if(!stk.isEmpty() && s.charAt(i)==')'){
                stk.pop();
                if(!stk.isEmpty()){
                    r.append(s.charAt(i));
                }

            }
            else if(!stk.isEmpty()){
                stk.push(s.charAt(i));
                r.append(s.charAt(i));
            }
            else{
                stk.push(s.charAt(i));
            }
        }
        return r.toString();
    }
}