# n=int(input("enter the number :"))
# a1=0;a2=1
# print(a1,a2,end='')
# for x in range(n-2):
#     sum=a1=a2
#     print(sum,end='')
#     a1,a2=a2,sum

# 

for i in range (5):
    for j in range (5-i):
      print(" ",end=" ")
    for k in range(2 * i - 1):
      print("*",end=" ")
    print()
for i in range (4,0,-1):
    for j in range (5-i):
      print(" ",end=" ")
    for k in range(2 * i - 1):
      print("*",end=" ")
    print()