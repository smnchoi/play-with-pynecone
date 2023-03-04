""" 
[신성욱을 위한 파이썬 썡기초 레슨]
데이터타입 - 조건문 - 함수 - 클래스
"""


# 데이터 타입
asahi = "I am a best beer"  # 문자열 string
# _float = 2.213213213213213213 # 소수 float
# _integer = 25 # 정수 int (integer)
number = 10.0  #
_bool = True  # 불리언 (T/F)
_bool2 = False


# age = 25

# # 조건문
# if age < 20:
#     print("이새끼 이거 미성년자네")
# elif 20 <= age < 25:
#     print("어 동생이네 ㅎㅇ")
# elif age == 25:
#     print("마 친구네")
# else:
#     print("성인 ㅎㅇ")


# 함수 -> 중,고등학교에서 배운 수학적의미의 함수가 아님.
# 함수의 3요소: 1. 인풋: def 함수이름(인풋)
#               2. 무언가일어남: def 블럭 안에있는 문장
#               3. 아웃풋: return 키워드
# 이 3요소 중 무엇이라도 생략될 수 있음!
def age_printer(age):  # <- age 인풋
    # 여기서부터 "무언가일어남"
    if age < 20:
        print("이새끼 이거 미성년자네")
    elif 20 <= age < 25:
        print("어 동생이네 ㅎㅇ")
    elif age == 25:
        print("마 친구네")
    else:
        print("성인 ㅎㅇ")

    # 아웃풋
    return str(age * 12) + "개월"


# 나는아웃풋이야 = age_printer(100)
# print(나는아웃풋이야)


# 파이썬 내장함수들
# 나는숫자 = 120
# 나는숫자일까 = str(나는숫자)

# print(나는숫자)
# print(나는숫자일까)

# print(type(나는숫자))
# print(type(나는숫자일까))


# 클래스 / 인스턴스
class 사람:
    def __init__(self, name, age, gender, nat):
        self.name = name
        self.age = age
        self.gender = gender
        # self.nat = "KOREAN"
        self.nat = nat

    def 자기소개(self):
        print("나의 이름은", self.name, "이고요, 나이는", self.age, "입니다. 성별은 ", self.gender, "입니다.")
        print(self.nat)


신성욱 = 사람("신성욱", 25, "남성", "자랑스러운한국인")
최수민 = 사람("수미니", 23, "남성", "미필한국인")

신성욱.자기소개()
최수민.자기소개()
