name = input("이름은 입력하세요 : ")
age = input("나이를 입력하세요 : ")
phone = input("연락처를 입력하세요 : ")


class user:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def show_info(self):
        print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.phone}입니다.")

member = user(name, age, phone)

member.show_info()
