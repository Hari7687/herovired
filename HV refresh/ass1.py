user1=int(input())
user2=int(input())
user3=int(input())
user4=int(input())
user5=int(input())
val=[user1,user2,user3,user4,user5]
sum=0
for i in val:
    if i<=0:
        print("enter positive number")
    else:
        sum=sum+i
        v=open('result.txt','a')
        print("values are:",i,file=v)
print(sum)
print("sum",sum,file=v)


