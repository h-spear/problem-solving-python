# https://www.acmicpc.net/problem/1544


def main():
    N = int(input())
    words = []
    for _ in range(N):
        word = input()
        words.append(word + word)

    checker = [False] * N
    for i in range(N):
        if checker[i] == False:
            word = words[i][0 : len(words[i]) // 2]
            for j in range(i + 1, N):
                if len(words[i]) != len(words[j]):
                    continue
                if word in words[j]:
                    checker[j] = True

    print(N - sum(checker))


if __name__ == "__main__":
    main()
