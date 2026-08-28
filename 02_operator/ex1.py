# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a**b)

# 복합 대입 연산자
a = 0
a += 4  # 증감 연산자(++,--) 없음
print(a)
a -= 2
print(a)

# 비교 연산자
print(3 == 3.0)
print(3 != 4)
print("apple" < "apble")
print(1 < 2 < 3)  # 1 < 2 and 2 < 3
print(1 < 3 < 2)

# 논리 연산자 (and, or, not)
a = True
b = False

print(a and b)
print(a or b)
print(not b)

# Short-circuit
a = 10
b = 0

if a > b or a / b:
    print("yes")  # print(a / b)
else:
    print("no")
