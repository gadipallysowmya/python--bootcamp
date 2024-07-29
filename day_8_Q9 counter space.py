n=int(input())
arr=list(map(int,input().split()))
product=int(input())
count=0
for i in range(1,n-2):
    for j in range(i+1,n-1):
        for k in range(i+2,n):
            if i*j*k > product or i*j*k < product:
                j+=1
                k+=1
        else:
            i+=1
            count+=1
print(count//3)
