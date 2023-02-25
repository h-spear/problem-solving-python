# https://leetcode.com/problems/word-search/


class Solution:
    answer = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        def back_tracking(x, y, curr, idx):
            if self.answer:
                return

            if curr[idx] != word[idx]:
                return

            if curr == word:
                self.answer = True
                return

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                _next = curr + board[nx][ny]

                visited[nx][ny] = 1
                back_tracking(nx, ny, _next, idx + 1)
                visited[nx][ny] = 0

        def handler():
            for i in range(m):
                for j in range(n):
                    visited[i][j] = 1
                    back_tracking(i, j, board[i][j], 0)
                    visited[i][j] = 0

            return self.answer

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for _ in range(m)]

        # counter
        w_counter = Counter(word)
        b_counter = defaultdict(int)

        for i in range(m):
            for j in range(n):
                b_counter[board[i][j]] += 1

        for k in w_counter:
            if w_counter[k] > b_counter[k]:
                return False

        return handler()
