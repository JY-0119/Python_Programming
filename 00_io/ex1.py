# # 입출력 처리

# # 1개 입력
a = input()
# # 정수 변환
a = int(a)
print(type(a))
# # 한번에
a = int(input())
print(type(a))

# # 실수 입력
b = float(input())
print(b, type(b))

# # 정수 2개 입력
a = int(input())
b = int(input())  # 100 200 입력 같이 띄어쓰기 구분x
print(a, b)
# # 100 200 입력
a = input().split()
print(a)

# map 사용하기
# map(함수, 리스트)
a, b, c = map(int, input().split())
print(a, b, c)
# 리스트로 변환
a = list(map(int, input().split()))
print(a)
