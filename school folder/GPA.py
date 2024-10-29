name_list=[]
book=["ریاضی","علوم","اجتماعی","فارسی","عربی","انگلیسی"]
Gpa_list=[]
total_list=[]

n=0
total=0
j=0
input1=int(input("تعداد نفرات کلاس  را مشخثص کنید ؟"))
for i in range(0,input1):
    name=input("لطفا نام را وارد کنید ")
    name_list.append(name)
while (n<input1):
    print("دانش اموز ",name_list[n])
    while (j<len(book)):
        print(("نمره درس",book[j]))
        GPA_input=int(input())
        total+=GPA_input
        if j==(len(book)-1):
            GPA=total/j
            Gpa_list.append(GPA)
            total_list.append(total)
        j+=1
    j=0
    n+=1
for i in range(0,input1):
    name=name_list[i]
    print("نام دانش اموز",name)
    GPA=Gpa_list[i]
    print("معدل",GPA)
    print("جمع نمرات دانش اموز",(total_list[i]))
print("جمع نمرات کلاس" ,(sum(total_list)))
print("معدل مدررسه",(sum(total_list)/(len(book)*input1)))

            