limit = int(input("enter limit:"))
f = 0
s = 1
print(f , s)
for i in range(limit+1):
    ans = f + s
    print(ans)
    f = s
    s = ans
