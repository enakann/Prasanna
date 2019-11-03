i=0
while i < 4:
    j=0
    while j < 7:
        print((i,j),end='')
        j+=1
    print("\n")
    i+=1

n=3
for i in range(1,n+1):
	print((n-i)*' '+i*'* ')