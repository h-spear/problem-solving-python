# https://leetcode.com/problems/reorder-data-in-log-files/


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        num_logs = []
        str_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                num_logs.append(log)
            else:
                str_logs.append(log)

        str_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return str_logs + num_logs


answer = Solution()
print(
    answer.reorderLogFiles(
        [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
    )
)
