# 변수
a = 2
b = 3  # a=2, b=3 과 같이 "한 줄에 작성" 불가능
# => a=(2,b)=3 로 a가 튜플 자료형으로 인식 (튜플 자료형은 소괄호 생략 가능)
# a=2; b=3 | a,b=2,3 (=> a,b=(2,3)으로 인식 -> 튜플 unpacking 작업)
print(a)
print(b)  # 자동 줄바꿈
print(a, end="")  # end 옵션 => 줄바꿈 삭제
print(b)
print(a, b)  # default로 변수 사이 공백
print(a, b, sep="")  # seperate 옵션 => 변수 사이 공백 삭제
a = b = c = 0

# 값 swap
a, b = 2, 3
# temp = a
# a = b
# b = temp
a, b = b, a
print(a, b)

# 변수명 규칙(C와 동일)
# 1. 알파벳, 숫자, 언더바(_)만 가능
# 2. 숫자로 시작 불가
# 3. 대소문자 구분
# 4. 예약어는 사용 불가
# snack_case, CamelCase 사용

# 한글 가능...
이름 = "이"
print(이름)
