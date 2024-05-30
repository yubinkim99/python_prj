from tkinter import *
import random

fu11_number = 90
list_market = ["과목1", "과목2", "과목3", "과목4", "과목5"]

# 랜덤 숫자 생성하고 라벨에 표시
def generate_random_number():
    for i in range(len(list_market)):
        random_number = random.randint(1, 180)
        output_text = f"{list_market[i]}: {random_number}/{fu11_number}"
        
        if random_number < fu11_number:
            new_label = Label(confirm_frame, text=output_text)
            new_label.pack()
        else:
            lb9.insert(END, output_text)

# 기본 창 생성
window4 = Tk()
window4.title("수강꾸러미 결과")
window4.geometry('400x600')

# 첫 번째 프레임(확정 과목)
confirm_frame = Frame(window4)
confirm_frame.pack(padx=10, pady=10)

# 수강꾸러미 확정 과목 리스트 라벨
lb6 = Label(confirm_frame, text="수강꾸러미 확정 과목")
lb6.pack(pady=10)

# 두 번째 프레임(초과 과목)
fail_frame = Frame(window4)
fail_frame.pack(padx=10, pady=10)

# 초과 과목 리스트 라벨
lb8 = Label(fail_frame, text="초과 과목")
lb8.pack(pady=10)

# 수강꾸러미 실패 과목 리스트
lb9 = Listbox(fail_frame, width=60)
lb9.pack(padx=10, pady=10)

# 프로그램 시작 시 함수 호출
generate_random_number()

# 메인 루프 실행
window4.mainloop()
