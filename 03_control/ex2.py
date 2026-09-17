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
