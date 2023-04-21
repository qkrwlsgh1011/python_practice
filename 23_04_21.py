from collections import deque
def solution(maps):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or nx >=5 or ny < 0 or ny >=5:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
        return maps[4][4]
    answer = bfs(0,0)
    return -1 if answer == 1 else answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))