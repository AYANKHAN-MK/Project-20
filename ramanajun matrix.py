a = " "
while a.isnumeric() == False:
    a = input("Enter a number: ")
    if a.isnumeric() == False:
        print("Enter a number")
a = int(a)
def eggarranger(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    i = 0
    j = n//2
    for k in range(1,n**2+1):
        a[i][j] = k
        i = i-1
        j = j+1
        if k%n == 0:
            i = i+2
            j = j-1
        else:
            if i<0:
                i = n-1
            if j > n-1:
                j = 0
    return a
for i in eggarranger(a):
        print(i)




