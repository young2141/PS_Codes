package sol;

import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int[] dy = {-1,0,1,0};
    public int[] dx = {0,1,0,-1};
    public boolean[][] visit;

    public int solution(int[][] land, int height) {
        int answer = 0;

        int h = land.length, w = land[0].length,area = 0;
        visit = new boolean[h][w];

        for(int i=0;i<h;++i)
            for(int j=0;j<w;++j)
                if(!visit[i][j]){
                    area++;
                    dfs(land,i,j,height);
                }

        return area;
    }

    public void dfs(int[][] land, int i, int j,int height){
        int h = land.length, w = land[0].length;
        Queue<Point> q = new LinkedList<Point>();
        q.add(new Point(i,j));
        visit[i][j] = true;

        while(!q.isEmpty()){
            int y = q.peek().y;
            int x = q.peek().x;
            q.remove();

            for(int k=0;k<4;++k){
                int ny = y + dy[k];
                int nx = x + dx[k];
                if(ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
                if(!visit[ny][nx] && Math.abs(land[ny][nx] - land[i][j])<= height ) {
                    visit[ny][nx] = true;
                    dfs(land, ny,nx, height);
                }
            }
        }
    }
}