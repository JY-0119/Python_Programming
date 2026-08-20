# 파이썬 자료형
# 1. 기본 자료형: 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합

# 숫자형(정수형)
# C언어: character, short, int, long, long long
# 파이썬: int class

a = 10
print(a, type(a))  # -> 10 <class 'int'> == a는 int의 객체

# 2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))  # 진수를 표시하기 위해 각각 0b,0o,0x가 앞에 붙음
print(ord("A"), chr(65))

# 정수형의 데이터 표현 범위
x = 10**100
print(x)  # 내부적으로 c의 배열로 저장 -> int의 표현범위는 제한 없음

# 오버플로우
a = 2**31 - 1
a += 1
print(a)  # 오버플로우가 없음

# 숫자형(실수형)
# 파이썬에선 float 하나밖에 없음
b = 3.14
print(b, type(b))  # 3.14 <class 'float'>

# 실수형의 표현범위
b = 1 / 3
print(b)  # 부동소수점(64bit = 1bit(부호)+11bit(지수부)+52bit(가수부)) 방식으로 저장 => 오차 발생
import sys

print(sys.float_info.min)
print(sys.float_info.max)
a = 1.7e308
b = 1.8e308
print(a, b)  # inf = 범위를 벗어남

# 실수의 오차
