def F(num):
    return sum([k for k in range(1,num+1) if k%2 != 0])
print(F())