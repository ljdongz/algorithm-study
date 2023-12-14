from collections import deque

def solution(begin: str, target: str, words: list):
    answer = 0

    if target not in words:
        return 0

    visited = {}
    for word in words:
        visited[word] = False

    q = deque()
    q.append((begin, 0))

    while q:
        cur_word, count = q.popleft()

        if cur_word == target:
            answer = count

        for i in range(len(begin)):
            cur_split_word = cur_word[:i] + cur_word[i+1:]
            for word in words:
                next_split_word = word[:i] + word[i+1:]
                if cur_split_word == next_split_word and not visited[word]:
                    visited[word] = True
                    q.append((word, count + 1))

    return answer