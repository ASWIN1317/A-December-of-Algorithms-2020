import datetime as dt
import ast
count=0
num=int(input("Number of Ice Creams : "))
manf=ast.literal_eval(input("Manufacture Dates : "))
man_date=[]
for i in manf:
    man_date.append("-".join(i))
dates1=[dt.datetime.strptime(i, '%d-%m-%Y').date() for i in man_date]
best_bef=ast.literal_eval(input("Best Before days : "))
today=ast.literal_eval(input("Given Date : "))
today="-".join(today)
dates2=dt.datetime.strptime(today, '%d-%m-%Y').date()
no_days=[]
for i in dates1:
    no_days.append((dates2-i).days)
for i in range(len(no_days)):
    if no_days[i]>best_bef[i]:
        count+=1
print("No of ice creams spoiled: ",count)

    

