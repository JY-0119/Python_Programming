# 반복문: while문, for문

# while문
# 1~10까지의 반복 출력
from sklearn.preprocessing import TargetEncoder

i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break
else:  # 조건식이 False가 되어 정상적으로 종료가 될 때 수행(break 등의 경우엔 불가)
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print(f"{target} found.")
        break
    i += 1
else:
    print(f"{target} not found")  # if not found: print(f"{target} not found")


# 1 ~ 10까지의 합
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
print(tot)

# 1 ~ 10중 짝수의 합
i = 2
tot = 0
while i <= 10:
    tot += i
    i += 2
print(tot)

i = 0
tot = 0
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += i
print(tot)

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
