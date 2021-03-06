# 리버스라는 보드 게임이 있다.
# 두명이서 가위바위보를 하고, 이긴 사람은 바둑판에 앞면은 검은색, 뒷면은 흰색인
# 바둑돌들을 임의로 깔아놓는다. 상대편은 바둑돌을 뒤집을 수 있는데, 한번 뒤집을 때 해당
# 열이나 행의 모든 바둑돌을 뒤집어야 한다. 예를 들어 3 X 3 형태로 바둑돌이 놓여져
# 있을 때 원하는 바둑돌 하나만 뒤집을 수는 없고, 특정한 열이나 행에 해당하는 바둑돌 3개를
# 모두 뒤집어야 한다. 게임에서 이기기 위해서는 원하는 만큼 바둑돌을 뒤집어서 위에서
# 보이는 흰색 바둑돌의 개수가 최소가 되어야 한다. 자연수 N이 주어지고, N X N 형태의
# 바둑돌들이 주어질 때 바둑돌을 뒤집는 사람이 만들 수 있는 위에서 보이는 흰색 바둑돌들의
# 최소 개수를 출력하는 프로그램을 만드세요.
#
# 입력 예시1
# 3
# BBW
# WBB
# WBW
# 출력 예시1
# 2
# 
# 입력 예시2
# 2
# BW
# WB
# 출력 예시2
# 0
