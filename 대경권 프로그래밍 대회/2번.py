""" 
문제2
문제 설명
0과 1로만 이루어진 다음과 같은 수열을 투에-모스 수열이라고 합니다.

첫 번째 수열은 0입니다.
현재 수열은 다음과 같은 과정을 통해 만듭니다.
현재 수열의 앞 절반은 바로 앞 수열과 같습니다.
현재 수열의 뒤 절반은 바로 앞 수열을 비트단위로 반전시킨 것과 같습니다.
위 과정을 반복합니다.
투에-모스 수열의 앞 몇 단계는 다음과 같습니다.

0
01
0110
01101001
0110100110010110
예를 들어 두 번째 항은 첫 항인 0과 첫 항의 비트 단위 반전인 1을 이어 붙인 01이 됩니다. 또 다른 예로 4번째 항은 3번째 항인 0110과 3번째 항의 비트 단위 반전인 1001을 이어 붙인 01101001이 됩니다.

세 수 N, x, y가 주어질 때, N번째 투에-모스 수열의 x번째 위치부터 y번째 위치까지 0과 1이 어떤 순서로 나타나는지 구해주세요.

제한사항
입력 :

표준 입력을 사용해 데이터를 입력받으세요.
테스트 케이스의 첫째 줄에 세 자연수 N, x, y가 주어집니다.
1 ≤ N ≤ 60
1 ≤ x ≤ y ≤ 2N-1
단, y - x ≤ 10,000
출력 :

표준 출력을 사용해 정답을 출력해주세요.
N번째 투에-모스 수열의 x번째 위치부터 y번째 위치까지 0과 1이 어떤 순서로 나타나는지 출력해주세요.
정확성 테스트 제한 사항
1 ≤ N ≤ 20
효율성 테스트 제한 사항
주어진 조건 외 다른 조건 없음
입출력 예
입력 #1
4 3 7

출력 #1
10100

입력 #2
5 1 16

출력 #2
0110100110010110
입출력 예 설명
입출력 예 #1

4번째 투에-모스 수열은 다음과 같습니다.

위치	1	2	3	4	5	6	7	8
수열	0	1	1	0	1	0	0	1
따라서 3번 위치부터 7번 위치까지 10100이 나타납니다.

입출력 예 #2

5번째 투에-모스 수열의 첫 번째 위치부터 마지막 위치까지 0과 1이 어떤 순서로 나타나는지 출력하면 됩니다. 따라서 0110100110010110을 출력하면 됩니다.


풀이1(오류)
코드 실행 중 오류가 발생하였습니다. 코드를 확인하세요.
Traceback (most recent call last):
  File "/solution.py", line 17, in <module>
    for i in range(len(one)/2):
TypeError: 'float' object cannot be interpreted as an integer

a, b, c = map(int, input().strip().split(' '))
n = 1
while(n <= a):
    
    if n==1:
        one = '0'
    else:
        one = two
    glue = ''
    
    # change
    if len(one) == 1:
        two = one + '1'
    else:
        for i in range(len(one)/2):
            if int(start[i]) == 0:
                glue += '1'
            else:
                glue += '0'
        two = one + glue
    n += 1

result = ''
for i in range(b+1, c+2):
    result += two[i]
    
print(result)

"""

N, x, y = map(int, input().split())

