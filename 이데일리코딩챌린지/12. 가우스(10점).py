# 입력 에시1
# 2
# 출력 예시1
# {2,3}
# 입력 예시2
# 4
# 출력 예시2
# {4,5,6,7}

def f(n):
    result = set()
    x = n
    while( x < n*2 ):
        result.add(x)
        x += 1
    return result

print(f(4))
