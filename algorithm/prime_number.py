n=int(input())
num_list=list(map(int,input().split()))
alone=[]
count=0
for i in num_list:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    # print(cnt)
    if cnt==2:
        count+=1
print(count)