# https://school.programmers.co.kr/learn/courses/30/lessons/87389 - [ 나머지가 1이 되는 수 찾기 ]


def solution(n) -> int:
    for i in range(1, n):
        if n % i == 1:
            return i


print(solution(10))
