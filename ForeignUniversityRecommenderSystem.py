from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import os
root = Tk()
List=[]


class University:
    def __init__(self, name, gre_score_requirement, toefl_score_requirement, location, coursename, workexperience):
        self.name = name
        self.gre_score_requirement = gre_score_requirement
        self.toefl_score_requirement = toefl_score_requirement
        self.location = location
        self.coursename = coursename
        self.workexperience = workexperience



Harvard = University("Harvard", 335, 118, "USA", [
                     "Electrical Engineering", "Computer Engineering", "Data Analytics", "Machine Learning"], 2)
List.append(Harvard)
Berkley = University("UC Berkley", 332, 115, "USA", [
                     "Electrical Engineering", "Computer Engineering", "Data Analytics", "VLSI Design"], 1)
List.append(Berkley)
MIT = University("MIT", 338, 119, "USA", [
                 "Mechanical engineering", "Computer Engineering", "Data Analytics", "VLSI Design"], 2)
List.append(MIT)
Princeton = University("Princeton", 335, 118, "USA", [
                       "Electrical Engineering", "Computer Engineering", "Data Analytics", "Machine Learning"], 2)
List.append(Princeton)
Columbia = University("Columbia", 330, 115, "USA", [
                      "Computer Science", "Data Science", "Machine Learning"], 2)
List.append(Columbia)
Stanford = University("Stanford", 340, 120, "USA", [
                      "Computer Science", "Electrical Engineering", "Biological Sciences"], 5)
List.append(Stanford)
Yale = University("Yale", 330, 115, "USA", [
                  "Computer Science", "Mechanical Engineering", "Data Analytics"], 2)
List.append(Yale)
Caltech = University("Caltech", 335, 120, "USA", [
                     "Electrical Engineering", "Mechanical Engineering", "Physics"], 1)
List.append(Caltech)
Cornell = University("Cornell", 330, 115, "USA", [
                     "Computer Engineering", "Electrical Engineering", "Data Analytics"], 1)
List.append(Cornell)
Brown = University("Brown", 305, 115, "USA", [
                   "Computer Science", "Biomedical Engineering", "Machine Learning"], 2)
List.append(Brown)
Penn = University("University of Pennsylvania", 309, 118, "USA", [
                  "Mechanical Engineering", "Data Analytics"], 0)
List.append(Penn)
Illinois = University("University of Illinois", 304, 105, "USA", [
                      "Computer Engineering", "Data Analytics", "Machine Learning"], 0)
List.append(Illinois)
Michigan = University("University of Michigan", 300, 110, "USA", [
                      "Electrical Engineering", "Computer Engineering", "VLSI Design"], 0)
List.append(Michigan)
Texas = University("University of Texas at Austin", 326, 104, "USA", [
                   "Computer Science", "Biomedical Engineering", "Data Analytics"], 0)
List.append(Texas)
GeorgiaTech = University("Georgia Institute of Technology", 308, 115, "USA", [
                         "Electrical Engineering", "Machine Learning"], 0)
List.append(GeorgiaTech)
Northwestern = University("Northwestern", 330, 115, "USA", [
                          "Computer Science", "Data Science", "VLSI Design"], 0)
List.append(Northwestern)
Duke = University("Duke University", 330, 110, "USA", [
                  "Computer Engineering", "Mechanical Engineering", "Data Analytics"], 16)
List.append(Duke)
UCLA = University("UCLA", 328, 108, "USA", [
                  "Electrical Engineering", "Computer Engineering", "Machine Learning"], 17)
List.append(UCLA)
UCSD = University("UC San Diego", 328, 114, "USA", [
                  "Computer Science", "Biomedical Engineering", "VLSI Design"], 18)
List.append(UCSD)
HarveyMudd = University("Harvey Mudd College", 335, 120, "USA", [
                        "Computer Science", "Data Analytics"], 19)
List.append(HarveyMudd)
TUDelft = University("TU Delft", 332, 109, "Netherlands", [
                     "Computer Science", "Data Analytics"], 1)
List.append(TUDelft)
Oxford = University("University of Oxford", 330, 110, "United Kingdom", [
                    "Computer Science", "Engineering", "Data Science"], 1)
List.append(Oxford)
Cambridge = University("University of Cambridge", 335, 115, "United Kingdom", [
                       "Computer Science", "Electrical Engineering"], 2)
List.append(Cambridge)
Imperial = University("Imperial College London", 328, 113, "United Kingdom", [
                      "Electrical Engineering", "Mechanical Engineering", "Data Analytics"], 3)
List.append(Imperial)
ETHZurich = University("ETH Zurich", 325, 105, "Switzerland", [
                       "Computer Engineering", "Data Science", "Machine Learning"], 1)
List.append(ETHZurich)
Toronto = University("University of Toronto", 330, 115, "Canada", [
                     "Computer Science", "Mechanical Engineering", "VLSI Design"], 4)
List.append(Toronto)
McGill = University("McGill University", 328, 113, "Canada", [
                    "Computer Engineering", "Biomedical Engineering", "Data Analytics"], 5)
List.append(McGill)
Sydney = University("University of Sydney", 330, 110, "Australia", [
                    "Computer Science", "Electrical Engineering", "Machine Learning"], 3)
List.append(Sydney)
Melbourne = University("University of Melbourne", 332, 112, "Australia", [
                       "Computer Science", "Data Science", "VLSI Design"], 1)
List.append(Melbourne)
NUSingapore = University("National University of Singapore", 330, 112, "Singapore", [
                         "Computer Science", "Computer Engineering", "Data Analytics"], 1)
List.append(NUSingapore)
NTU = University("Nanyang Technological University", 328, 110, "Singapore", [
                 "Computer Engineering", "Mechanical Engineering", "Machine Learning"], 2)
List.append(NTU)
HKUST = University("Hong Kong University of Science and Technology", 325, 110, "Hong Kong", [
                   "Electrical Engineering", "Computer Engineering", "Data Science"], 1)
List.append(HKUST)
TUMunich = University("Technical University of Munich", 330, 115, "Germany", [
                      "Computer Science", "Electrical Engineering", "Biomedical Engineering"], 2)
List.append(TUMunich)
EPFL = University("EPFL", 332, 115, "Switzerland", [
                  "Computer Science", "Data Analytics", "Machine Learning"], 2)
List.append(EPFL)
UCLondon = University("University College London", 328, 113, "United Kingdom", [
                      "Computer Engineering", "Electrical Engineering", "Data Analytics"], 2)
List.append(UCLondon)
KTHStockholm = University("KTH Royal Institute of Technology", 330, 115, "Sweden", [
                          "Computer Science", "Computer Engineering", "Data Analytics"], 0)
List.append(KTHStockholm)
KITKarlsruhe = University("Karlsruhe Institute of Technology", 328, 110, "Germany", [
                          "Electrical Engineering", "Mechanical Engineering", "VLSI Design"], 0)
List.append(KITKarlsruhe)
LSE = University("London School of Economics and Political Science", 328, 113,
                 "United Kingdom", ["VLSI Design", "Computer  Science", "Data Analytics"], 2)
List.append(LSE)
KISeoul = University("Korea University", 325, 110, "South Korea", [
                     "Computer Science", "Mechanical Engineering", "Data Analytics"], 0)
List.append(KISeoul)
UAMadrid = University("Universidad Autónoma de Madrid", 330, 115, "Spain", [
                      "Computer Engineering", "Electrical Engineering", "Data Analytics"], 0)
List.append(UAMadrid)
Helsinki = University("University of Helsinki", 332, 112, "Finland", [
                      "Computer Science", "Biomedical Engineering", "Machine Learning"], 1)
List.append(Helsinki)



def gradestudents(selected_degree, gre, toefl, workex):

    Lists = []

    for u in List:
        marks = 0
        if selected_degree in u.coursename:
            if gre >= u.gre_score_requirement:
                marks += 4
            if toefl >= u.toefl_score_requirement:
                marks += 2
            if workex > 0 and workex >= u.workexperience:
                marks += 4
            u.m = marks
            Lists.append(u)

    result_text = "UNIVERSITY RECOMMENDATIONS:\n \n"
    flag = 0
    for l in Lists:
        if l.m >= 8:
            flag = 1
            result_text += f"Your grade: {l.m}\nSafety university: {l.name}\n================================ \n"
        elif 5 <= l.m < 8:
            flag = 1
            result_text += f"Your grade: {l.m}\nMedium university: {l.name}\n=================================\n"
        elif 0 < l.m < 5:
            flag = 1
            result_text += f"Your grade: {l.m}\nAmbitious university: {l.name}\n==============================\n"

    if flag == 0:
        result_text += "No appropriate University for your choices and profile"


    output_text.config(state="normal")
    output_text.delete(1.0, END)
    output_text.insert(END, result_text)

    output_text.config(state="disabled")



output_text = Text(height=50, width=60,bg='#D7BFDC')
output_text.pack(side=RIGHT)
output_text.config(state="disabled")
Label(root, text="UNIVERSITY RECOMMENDER SYSTEM", justify=CENTER,font=10, anchor=CENTER, bg="#502380",fg="white").place(x=550, y=20)



def students():


    root.configure(bg="#B452CD")


    bg=PhotoImage(file="project.png")

   #width=root.winfo_screenwidth()
  # height=root.winfo_screenheight()
   #root.resizable(False,False)

   #root.geometry("%dx%d" % (width,height))
    label1=Label(root,image=bg,height=800,width=380)
    #label1.pack(side=LEFT,ipady=700)
    label1.place(x=0,y=0)


    label = Label(root, text="Choose the Masters degree that you want to pursue :",font=40,bg="#D02090").place(x=400, y=100)

    var = StringVar()
    selected_degree = StringVar()  # Variable to store the selected degree

    r1 = Radiobutton(root, text="Electrical Engineering", variable=var,
                     value="Electrical Engineering",bg='#D7BFDC').place(x=430, y=140)
   # r1.pack()
    r2 = Radiobutton(root, text="Computer Enginnering", variable=var,
                     value="Computer Engineering",bg='#D7BFDC').place(x=430, y=180)
    # r2.pack()

    r3 = Radiobutton(root, text="Data Analytics", variable=var,
                     value="Data Analytics",bg='#D7BFDC').place(x=430, y=220)
    # r3.pack()

    r4 = Radiobutton(root, text="Machine Learning", variable=var,
                     value="Machine Learning",bg='#D7BFDC').place(x=430, y=260)
    # r4.pack()

    r5 = Radiobutton(root, text="VLSI Design", variable=var,
                     value="VLSI Design",bg='#D7BFDC').place(x=430, y=300)
    # r5.pack()

    r6 = Radiobutton(root, text="Mechanical Engineering", variable=var,
                     value="Mechanical Engineering",bg='#D7BFDC').place(x=430, y=340)
    # r6.pack()

    r7 = Radiobutton(root, text="Biomedical Engineering", variable=var,
                     value="Biomedical Engineering",bg='#D7BFDC').place(x=430, y=380)
    # r7.pack()

    r8 = Radiobutton(root, text="Computer Science", variable=var,
                     value="Computer Science",bg='#D7BFDC').place(x=430, y=420)


    selected_degree = var




    gre_label = Label(root, text="Enter GRE Score:",font=10,bg="#D02090")
    gre_label.place(x=400, y=460)
   # gre_label.pack(ipadx=30)

    gre_entry = Entry(root)
    gre_entry.place(x=750, y=460)
    #gre_entry.pack(ipadx=30,padx=600,pady=700)

    toefl_label = Label(root, text="Enter TOEFL Score:",font=10,bg="#D02090")
    toefl_label.place(x=400, y=510)
    toefl_entry = Entry(root)
    toefl_entry.place(x=750, y=510)

    workex_label = Label(root, text="Enter Work Experience (in years):",font=10,bg="#D02090")
    workex_label.place(x=400, y=560)
    workex_entry = Entry(root)
    workex_entry.place(x=750, y=560)

    def select_degree():

        selected_degree.set(var.get())
        gre_score = gre_entry.get()
        min=260
        max=340
        flag=0
        try:
            gre_score = int(gre_score)


        except ValueError:

                error_label=Label(root,text="Invalid!",fg='red')

                error_label.place(x=750,y=460)



                return
        try:
            if(gre_score<260 or gre_score>340):
                raise ValueError



        except ValueError:
            error_label=Label(root,text="Range Error!",fg='red')

            error_label.place(x=750,y=460)
            return









        toefl_score = toefl_entry.get()
        try:
           toefl_score = int(toefl_score)
        except ValueError:
          error_label=Label(root,text="Invalid!",fg='red')

          error_label.place(x=750,y=510)

          return
        try:
           if(toefl_score<0 or toefl_score>120):
               raise ValueError



        except ValueError:
           error_label=Label(root,text="Range Error!",fg='red')

           error_label.place(x=750,y=510)
           return


        work_experience = workex_entry.get()

        try:
           work_experience = int(work_experience)
        except ValueError:
          error_label=Label(root,text="Invalid!",fg='red')

          error_label.place(x=750,y=560)

          return
        try:
           if(int(work_experience)<0 ):
               raise ValueError
        except ValueError:
           error_label=Label(root,text=" Range Error!",fg='red')

           error_label.place(x=750,y=560)
           return







        gradestudents(selected_degree.get(), int(gre_entry.get()),
                      int(toefl_entry.get()), int(workex_entry.get()))
        display_recommendations()

    submit_button = Button(root, text="SUBMIT",
                           command=select_degree,bg="white").place(x=520, y=650)
    def clear():
        output_text.config(state="normal")
        output_text.delete(1.0, "end")
        output_text.config(state="disabled")
        students()



    clear_button=Button(root,text="CLEAR",command=clear,bg="white").place(x=520,y=750)
    root.mainloop()
    return


students()
