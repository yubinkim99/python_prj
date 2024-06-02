from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


def open_cart_page(master):
    window2 = Toplevel(master)
    window2.title("장바구니")
    window2.geometry('400x600+10+10')

    lb2 = Listbox(window2, width=60)        #lb2 : 장바구니 목록 출력

    list1 = ["과목1", "과목2", "과목3", "과목4", "과목5", "과목6"]
    list2 = ["0012", "0023", "0034", "0045", "0056", "0067"]
    list3 = ["배주화", "이찬수", "유제혁", "이경미", "유견아", "유제혁"]
    list4 = ["01", "02", "01", "03", "02", "01"]
    list_final = [1,2,3,4,5,6]
    for i in range(len(list1)):
        list_final[i] = list1[i] + " // 과목코드: " + list2[i] + " // 교수명: " + list3[i] + " [" + list4[i] + "]"


    def lookup(list1):      #리스트 확인
        for i in range (len(list1)):
            lb2.insert(END, list_final[i])

    # frame = Frame(window2)
    # frame.pack(side=TOP)
    lb1 = Label(window2, text="장바구니", command=lookup(list_final))     #lb1 : 장바구니

    lb1.pack(side=TOP, padx=10, pady=10)


    lb2.config(selectmode="single")         #lb2 : 장바구니 목록 출력
    lb2.config(height=10)
    lb2.pack(padx=10)

    list_market = []            #수강 꾸러미 목록

    def btnpress():     # 입력창의 내용을 리스트 박스 마지막에 추가
        num = lb2.curselection()   
        num = int(num[0])
        #print(lb2.curselection())          
        lb.insert(END, list_final[num]) 
        list_market.append(list_final[num])
        print(list_market)
        lb2.delete(lb2.curselection())
        list_final.remove(list_final[num])
        
    def btnpress1():              # 리스트 박스 중 선택된 값 삭제  
        #lb.delete(lb.curselection())  
        #lb2.insert(END, list_market[int(lb.curselection()[0])])
        #print(lb.curselection())

        #print(lb.curselection())
        # lb2.insert(END, list_market[int(lb.curselection()[0])])
        # list_market.remove(list_market[int(lb.curselection()[0])])
        # lb.delete(lb.curselection())  # 리스트 박스 중 선택된 값 삭제
        # print(list_market)

        print(lb.curselection())
        lb2.insert(END, list_market[int(lb.curselection()[0])])
        list_final.append(list_market[int(lb.curselection()[0])])
        list_market.remove(list_market[int(lb.curselection()[0])])
        lb.delete(lb.curselection())  # 리스트 박스 중 선택된 값 삭제
        print(list_final)

    def complete():     
        global newWindow, new_lbox , finish_label, fail_label
        full_number=50     # 새 창 띄우기, 최종 과목명 출력 리스트박스
        newWindow = Toplevel()
        newWindow.title("수강 꾸러미 결과")
        newWindow.geometry("500x600+10+10")

        finish_label = Label(newWindow, text='수강 꾸러미 확정 과목') #수꾸 확정 과목 리스트 라벨
        finish_label.pack(side=TOP, pady=10)
        new_lbox = Listbox(newWindow, width=50) #수꾸 확정 과목 리스트
        new_lbox.config(selectmode="none")
        new_lbox.config(height=6)
        new_lbox.pack(padx=10, pady=5)

        fail_label=Label(newWindow, text="초과 과목") #초과 과목 리스트 라벨
        fail_label.pack()
        fail_lbox = Listbox(newWindow, width=50) #수꾸 확정 과목 리스트
        fail_lbox.config(selectmode="none")
        fail_lbox.config(height=6)
        fail_lbox.pack(padx=10, pady=5)

        for i in range(len(list_market)):
         random_number = random.randint(1, 100) #랜덤으로 수꾸 신청 인원 발생
         output_text = f"{list_market[i]}: {random_number}/{full_number}"
        
         if random_number < full_number: 
              new_lbox.insert(END, output_text)
         else:
             fail_lbox.insert(END, output_text)

        def PieChart():
            plt.rcParams['font.family'] = "Malgun Gothic"
            plt.rcParams['axes.unicode_minus']=False  ### 원형차트 한글 인코딩
    
            member=random.randint(1,5)
            X = [member,5-member]
            labels=["수강꾸러미\n신청인원", "수강꾸러미\n남은인원"]
            explode = [0,0.1]
            colors = ["r","b"]
    
            # 파이차트 그리기
            fig, ax = plt.subplots()
            ax.pie(X, labels=labels, explode=explode, colors=colors, autopct='%1.1d명', startangle=140)
            ax.axis('equal')  # 원형을 유지
            ax.set_title("수강 꾸러미 인원비율")  # 제목 설정
    
            # Matplotlib 그림을 Tkinter 창에 삽입
            canvas = FigureCanvasTkAgg(fig, master=graph)
            canvas.draw()
            canvas.get_tk_widget().pack()

            plt.plot(label="수강꾸러미 신청인원")
            plt.plot(label="수강꾸러미 남은인원")
            plt.legend()
            plt.title("수강꾸러미 인원비율")



        graph = Tk()
        graph.geometry('500x600+10+10')
        graph.title("파이차트 예제")

        # 파이차트 그리기
        PieChart()
        graph.mainloop()


    def detail(evnet):
        num = lb.curselection()
        if num:
            num=int(num[0])
            global detailWindow, finish_lbox       # 새 창 띄우기, 최종 과목명 출력 리스트박스(이거 고치면 됨-임시)
            detailWindow = Toplevel()
            
            detailWindow.geometry("500x600+10+10")
        ######################################### 다음 창에서는 여기부터
            finish_lbox = Listbox(detailWindow, width=50)
            finish_lbox.config(selectmode="single")
            finish_lbox.config(height=6)
            finish_lbox.pack(padx=10, pady=5)
            detailWindow.title("(데이터 시각화)" + list_market[num])
            finish_lbox.insert(END, list_market[num])
        # for i in range (len(list_market)):      # for 문으로 수꾸 리스트 출력(임시)
        #     print(list_market[i])
        #     finish_lbox.insert(END, list_market[i])
        
    def realCheck():        # 확정을 물어보는 메세지박스
        messagebox.askyesno('확인', "진짜 완료 됨??")
        complete()          # 새 창을 띄우는 함수로 넘어감

    btn = Button(window2)                
    btn.config(text= "수강 꾸러미에 추가")          # 버튼 내용 
    btn.config(width=15)              # 버튼 크기
    btn.config(command=btnpress)      # 버튼 기능 (btnpree() 함수 호출)
    btn.pack(pady=5)                        # 버튼 배치

    lb3 = Label(window2, text="수강 꾸러미")
    lb3.pack(padx=10, pady=5)

    lb = Listbox(window2, width=60)             # 수강꾸러미 리스트 생성        #lb: 수강꾸러미 리스트
    lb.config(selectmode="single")    # 리스트 박스 selectmode 설정
    lb.config(height = 6)             # 리스트 박스 높이 설정
    lb.pack(padx=10, pady=5)                         # 리스트 박스 배치
        
    lb.bind('<Double-Button-1>', detail)            # 리스트 박스 데이터시각화  ####해당 값 더블클릭 시 데이터 시각화 페이지로 이동

    # ent = Entry(window2)                 # 입력창 생성
    # ent.pack()                        # 입력창 배치


    btn1 = Button(window2)                
    btn1.config(text= "삭제")          # 삭제 버튼
    btn1.config(width=10)              # 버튼 크기
    btn1.config(command=btnpress1)     # 버튼 기능 (btnpree1() 함수 호출)
    btn1.pack(pady=5)                        # 버튼 배치

    btn2 = Button(window2)      # 완료 버튼
    btn2.config(text="완료")
    btn2.config(width=10)
    btn2.config(command=realCheck)        #버튼 기능 (completet() 함수 호출)
    btn2.pack(pady=10)

    window2.mainloop()
