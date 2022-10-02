import random
import os
os.chdir("D:\python")


def result(number):     #等式生成函数
    numbers=[2,3]
    dict_allresult={}     #等式为key，答案为value的字典
    list_allnum2=[]     #2运算数储存
    list_allnum3=[]     #3运算数储存
    count=0
    while count<number:
        num_decide = random.choice(numbers)     #随机决定运算数的数量（或运算符的数量）
        num_1 = random.randrange(1, 100)
        num_2 = random.randrange(-num_1, 100)
        num_3= random.randrange(-num_1-num_2,100)
        if num_2!=0 and num_3!=0:     #在第二第三个数不为0的条件下
            if num_decide==2:     #运算数为2的条件下
                answer=num_1+num_2     #求和
                if num_2<0:
                    equation=str(num_1)+str(num_2)+'='
                else:
                    equation=str(num_1)+'+'+str(num_2)+'='
                list_num=sorted([num_1,num_2])     #将生成的运算数按降序打包成列表，再装入总列表中方便后续判断是否出现重复题
                if list_num not in list_allnum2:     #如果总列表中没有该运算数列表，则表示不为重复题，即可进行该题的纳入
                    list_num.append(list_allnum2)
                    dict_allresult[equation]=answer
                    count+=1
                else:
                    continue
            if num_decide==3:     #运算数为3时
                answer=num_1+num_2+num_3
                if num_2>0:
                    if num_3>0:
                        equation=str(num_1)+'+'+str(num_2)+'+'+str(num_3)+'='
                    else:
                        equation=str(num_1)+'+'+str(num_2)+str(num_3)+'='
                else:
                    if num_3 > 0:
                        equation=str(num_1)+str(num_2)+'+'+str(num_3)+'='
                    else:
                        equation=str(num_1)+str(num_2)+str(num_3)+'='
                list_num=sorted([num_1,num_2,num_3])
                if list_num not in list_allnum3:     #运算数列表判断
                    list_num.append(list_allnum3)
                    dict_allresult[equation] = answer
                    count += 1
                else:
                    continue
        else:
            continue
    return dict_allresult

number=int(input("请输入需要生成题目的数量："))
result=result(number)

file_exercise=open("Exercise.txt",'w')
count_exercise=0
for items in result.keys():     #遍历所生成的算术题
    count_exercise += 1     #计数
    file_exercise.write("{},{}\n".format(count_exercise,items))
file_exercise.close

count_answer=0
file_answer=open("Answer.txt",'w')
for items in result.values():
    count_answer+=1
    item="{},{}\n".format(count_answer,items)
    file_answer.write(item)
file_answer.close