# for문
for i in range(5):  # iterable객체
    print(i, end="")

print()
a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 10, 2칸씩
for i in range(1, 11, 2):
    print(i, end="")
print()

# 5 ~ 1, 거꾸로
for i in range(5, 0, -1):
    print(i, end="")
print()

# 1 ~ 10까지 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(tot)

print(sum(range(1, 11)))  # 다만 sum이라는 이름의 변수가 있을 경우 Error

s = "hi韓글🫥😍"
for c in s:
    print(c, end=" ")
print()
print(len(s))

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:<5d}", end="   ")
    print()
