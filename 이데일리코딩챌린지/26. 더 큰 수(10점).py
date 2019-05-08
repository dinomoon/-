# 첫째 줄에 정수 A와 B가 공백을 기준으로 입력됩니다
# A가 B보가 크다면 첫째 줄에 1을 출력하고, 그렇지 않다면 0을 출력합니다.

A,B = input().split()
A = int(A)
B = int(B)

def f(A,B):
    if A>B:
        return 1
    else:
        return 0

print(f(A,B))
