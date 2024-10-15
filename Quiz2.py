message = input("메세지를 입력하십시오 : ")
def check_length_of_message(message):
    if len(message) <=20:
        return 50
    else:
        return 100

money = check_length_of_message(message)

print(f"메세지의 요금은 {money} 원 입니다.")