# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)


#     print("대기번호 : {0}".format(waiting_no))
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# import random
# cnt = 0
# for i in range(1, 51):
#     time = random.randint(5, 51)
#     if(time >= 5 and time <= 15):
#         print("[0] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt +=1
#     else:
#         print("[ ] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 {0} 분".format(cnt))


# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commision = 100
#     return money, commision, balance - money - commision

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2200)
# money, commision, balance = withdraw_night(balance, 500)

# print("{0}원을 출금하여, 수수료{1} 원이며, 잔액은 {2} 원입니다.".format(money, commision, balance))

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")

#같은 학교 같은 학년 같은 반 같은 수업.


# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 13, "나나나")


# def std_weight(height, gender):
#     if gender=="남자":
#         return (height*0.01)*(height*0.01)*22
#     elif gender=="여자":
#             return (height*0.01)*(height*0.01)*21
#     else:
#         print("올바른 성별을 입력해 주세요.")

# height = 175
# gender = "남자"
# weight = round(std_weight(height, gender),2)
# print("키 {0}cm {1} 의 표준 체중은 {2}kg 입니다".format(height, gender, weight))

# scores = {"수학":0 , "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4))

# 은행 대기순번표
# 001, 002, 003 ...
# for num in range(1,21):
#     print("대기번호: " +str(num).zfill(4))

# answer = input("아무 값이나 입력하세요: ")
# print(type(answer))
# print("입력하신 값은 "+answer+ " 입니다")

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

# print("{0:>10}".format(500))
# # 양수일 때는 +로 표시, 음수일때는 -로 표시
# print("{0:>+10}".format(500))
# # 왼쪽정렬하고, 빈칸은 _로 채움

# print("{0:_>10}".format(500))

# print("{0:,}".format(10000000000000))
# print("{0:+,}".format(10000000000000))
# print("{0:^<+30,}".format(10000000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))
# print("{0:.10f}".format(5/3))

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("\n과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.read())
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
# num = int(input())

# i = 1

# while i <= num:
#     print(i, i * i)
#     i = i + 1

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 잇는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# for i in range(1,5):
#     with open (str(i)+"주차.txt", "w", encoding = "utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")
 
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        # self.damage = damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50 , 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 메딕 : 의무병  .....