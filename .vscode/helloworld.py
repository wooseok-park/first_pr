# weather = input("오늘날씨는?")
# if weather == "비" or weather == "눈":
#     print("우산")
# elif weather =="먼지":
#     print("마스크챙기세유")
# else:
#     print("필요없음")


# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1,5):
#     print("대기번호 : {0}".format(waiting_no))
#  customer = "토르"
#  person = "Unknown"
#  while person != customer : 
#      print("{0}, 커피가 준비되었습니다." .format(customer))
#      person = input("이름이 어떻게 되세요?")


def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")