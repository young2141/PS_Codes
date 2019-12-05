import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

public class findprime {
    public static int MAX = 9999999;

    public static void main(String[] args) {
        String numbers = "17";

        int answer = 0;
        ArrayList<String> result = new ArrayList<String>();
        boolean[] visit = new boolean[numbers.length()];
        Arrays.fill(visit, false);
        HashSet<Integer> set = new HashSet<Integer>();
        boolean[] prime = new boolean[MAX];
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;

        seive(prime);
        for (int i = 1; i <= numbers.length(); ++i) {
            permutation(numbers, 0, result, "", visit, i);
        }

        for (String s : result) {
            // System.out.println(s);
            set.add(Integer.parseInt(s));
        }
        for (int s : set) {
            if (prime[s]) {
                System.out.println(s);
                ++answer;
            }
        }
        System.out.println(answer);
    }

    private static void permutation(String numbers, int depth, ArrayList<String> ret, String cur, boolean[] visit,
            int pick) {
        if (cur.length() == pick) {
            ret.add(cur);
            return;
        }
        for (int i = 0; i < numbers.length(); ++i) {
            if (!visit[i]) {
                visit[i] = true;
                permutation(numbers, depth + 1, ret, cur + numbers.charAt(i), visit, pick);
                visit[i] = false;
            }
        }
    }

    private static void seive(boolean[] prime) {
        for (int i = 2; (i * i) <= MAX; ++i) {
            if (prime[i]) {
                for (int j = i * i; j < MAX; j = j + i) {
                    prime[j] = false;
                }
            }
        }
    }
}