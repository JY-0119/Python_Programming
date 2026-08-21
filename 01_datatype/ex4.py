# 문자열 ("", '')
a = "python"
print(a, type(a))

# I'll be back
print("I'll be back")  # 홑따옴표(')가 있으므로 쌍따옴표(")로 묶기 / print('I\'ll be back')

multiline = """
Life is short
You need Python
"""  # 마찬가지로 홑따옴표 3개(''') 가능

print(multiline)


# docstring
def func():
    """이 함수는 테스트용입니다."""  # docstring - 함수 정의 첫번째 줄에만 작성 가능
    pass


print(func.__doc__)

# 문자열 연결
print("Hello" + " Python")  # 같은 형식 끼리만 더하기(+) 가능
print("10" + "2")

# 문자열 반복
print("Hello" * 10)
print("_" * 50)
