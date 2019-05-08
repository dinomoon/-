# 년도와 달을 입력하면 일수를 알려주는 함수

def findDays(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if year % 4 == 0 and month == 2:
        return 29
    return 28

print(findDays(2013,2))
