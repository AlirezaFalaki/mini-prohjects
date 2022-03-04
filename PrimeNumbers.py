# this program show you prime numbers between two number without considering these two numbers

n1=int(input())
n2=int(input())

list=[]
num=0

for i in range(n1+1,n2,1):
    for j in range(2,int(i/2)+1):
        if i % j == 0:
            num+=1
    if num==0:
        list.append(i)
    num=0

print(list)