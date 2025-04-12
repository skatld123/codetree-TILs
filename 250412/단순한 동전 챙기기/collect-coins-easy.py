from collections import deque
n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
# 증가하면서 주워야 하고 최소 3개 주워야 함 
# 2번 이상 지나가도 되고 안주워도 됨
# 최소 이동 횟수가 구하기

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            sx = i
            sy = j

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
visited = [[False] * n for _ in range(n)]
min_move = int(1e9)

def dfs(x, y, queue, move):
    global min_move
    if grid[x][y] == 'E':
        #  최소 이동횟수 
        if len(queue) == 3:
            min_move = min(min_move, move)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 동전 주웠으면 
            if grid[nx][ny].isdigit():
                # 기존 주운 동전이 있으면
                if queue:
                    last = queue[-1]
                    # 기존보다 클 경우에만 줍기 
                    if grid[nx][ny] > last:
                        queue.append(last)
                        visited[nx][ny] = True
                        dfs(nx, ny, queue, move + 1)
                        queue.pop()
                        visited[nx][ny] = False
                    #w작으면 아무것도 하지말기
                # 없으면 일단 줍기
                else:
                    queue.append(grid[nx][ny])
                    visited[nx][ny] = True
                    dfs(nx, ny, queue, move + 1)
                    queue.pop()
                    visited[nx][ny] = False
            else:
                # 동전이 아닌경우 일단 가기
                visited[nx][ny] = True
                dfs(nx, ny, queue, move + 1)
                visited[nx][ny] = False
            
dfs(sx, sy, [], 0)
if min_move == int(1e9):
    print(-1)
else:
    print(min_move)