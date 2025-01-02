class Solution {
    public String solution(String s) {
        StringBuilder jc = new StringBuilder();
        boolean checkNext = true;

        for (Character c : s.toCharArray()) {
            if (Character.isWhitespace(c)) {
                jc.append(c);
                checkNext = true;
            } else {
                if (checkNext) {
                    jc.append(Character.toUpperCase(c));
                    checkNext = false;
                } else {
                    jc.append(Character.toLowerCase(c));
                }
            }
        }
        
        String answer = jc.toString();
        return answer;
    }
}