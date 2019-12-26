s = ""

i = 0
j = 0
k = 0

for k in range(6):

    s = ""
    
    for i in range(5-k):
        s = s + " "

    for j in range(2*k+1):
        s = s + "*"

    print(s)

    
