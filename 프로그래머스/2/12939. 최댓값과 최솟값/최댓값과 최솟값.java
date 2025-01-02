import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String[] numberArray = s.split(" ");
        List<Integer> numberList = new ArrayList<>();
        
        for (String num : numberArray) {
            numberList.add(Integer.parseInt(num));
        }
    
        Collections.sort(numberList);
        int min_n = numberList.get(0);
        int max_n = numberList.get(numberList.size() - 1);
        
        String answer = String.valueOf(min_n) + " " + String.valueOf(max_n);
        return answer;
    }
}