from collections import deque

N, r, c, d = map(int, input().split())

r -= 1
c -= 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

convert = {
    1: 0,
    2: 2,
    3: 3,
    4: 1
}

d = convert[d]

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
visited[r][c] = True

answer = [(r, c)]

def first_step(r, c, d):
    dirs = [
        d,
        (d + 3) % 4,
        (d + 1) % 4,
        (d + 2) % 4
    ]

    for nd in dirs:
        nr = r + dr[nd]
        nc = c + dc[nd]

        if (
            0 <= nr < N
            and 0 <= nc < N
            and board[nr][nc] == 0
            and not visited[nr][nc]
        ):
            visited[nr][nc] = True
            return nr, nc, nd

    return None

def find_target(r, c):
    q = deque([(r, c)])

    dist = [[-1] * N for _ in range(N)]
    dist[r][c] = 0

    candidates = []

    while q:
        cr, cc = q.popleft()

        for nd in range(4):
            nr = cr + dr[nd]
            nc = cc + dc[nd]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if board[nr][nc] == 1:
                continue

            if dist[nr][nc] != -1:
                continue

            dist[nr][nc] = dist[cr][cc] + 1
            q.append((nr, nc))

            if not visited[nr][nc]:
                candidates.append(
                    (dist[nr][nc], nr, nc)
                )

    if not candidates:
        return None

    _, tr, tc = min(candidates)

    return tr, tc

def make_dist_map(tr, tc):
    q = deque([(tr, tc)])

    dist = [[-1] * N for _ in range(N)]
    dist[tr][tc] = 0

    while q:
        cr, cc = q.popleft()

        for nd in range(4):
            nr = cr + dr[nd]
            nc = cc + dc[nd]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if board[nr][nc] == 1:
                continue

            if dist[nr][nc] != -1:
                continue

            dist[nr][nc] = dist[cr][cc] + 1
            q.append((nr, nc))

    return dist

while True:
    result = first_step(r, c, d)

    if result is not None:
        r, c, d = result
        answer.append((r, c))
        continue

    target = find_target(r, c)

    if target is None:
        break

    tr, tc = target

    dist = make_dist_map(tr, tc)

    move_order = [3, 2, 1, 0]

    while (r, c) != (tr, tc):
        for nd in move_order:
            nr = r + dr[nd]
            nc = c + dc[nd]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if dist[nr][nc] == dist[r][c] - 1:
                r, c = nr, nc
                d = nd

                if not visited[r][c]:
                    visited[r][c] = True
                    answer.append((r, c))

                break

for r, c in answer:
    print(r + 1, c + 1)