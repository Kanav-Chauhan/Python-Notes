# n = 3
# for i in range(n):
#     print("*" * (n-i)) # Prints * n-i times


def mehod (n):
    if n >1:
     return  ("*" * int(mehod(n-1)))
     
l = mehod (4)
print(l)