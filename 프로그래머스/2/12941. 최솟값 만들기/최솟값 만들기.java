import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;

        List<Integer> A_list = new ArrayList<>();
        for (int num : A) {
            A_list.add(num);
        }
        
        List<Integer> B_list = new ArrayList<>();
        for (int num : B) {
            B_list.add(num);
        }
        Collections.sort(A_list);
        Collections.sort(B_list);
        Collections.reverse(B_list);
        
        for (int i = 0; i < A_list.size(); i++) {
            answer += A_list.get(i) * B_list.get(i);
        }

        return answer;
    }
}