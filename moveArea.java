public class moveArea {
    public static void main(String[] args) {
        int[][] land = { { 1, 4, 8, 10 }, { 5, 5, 5, 5 }, { 10, 10, 10, 10 }, { 10, 10, 10, 20 } };
        int height = 3;

        int[][] visit = new int[land.length][land[0].length];
        for (int[] v_line : visit) {
            for (int v : v_line) {
                System.out.print(v);
            }
            System.out.println();
        }
        return;
    }

    public static void dfs(int[][] land, int[][] visit) {

    }
}
