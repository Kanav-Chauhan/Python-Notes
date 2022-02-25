# def max (numb1,numb2,numb3):
#     if numb1>numb2:
#         if numb1>numb3:
#             return numb1

#         else :
#             return numb3
    
#     elif numb2>numb3:
        
#         return numb2

#     else:
#         return numb3
        


# m = max(2,3,4)

# print (" The biggest no. is " ,(m))

        


# def temp (c):
#     f = (c * 9/5) + 32 
#     return f


# ctf = temp(0)
# print("The tempreture in farenheit is ",ctf)




# def ad (n):

#       if  n>1:
#              return  n + (ad (n-1)) 
#       else :
#         return 1 


# m = ad (2)
# print(" the no ", m)
   

def table (n):
    for i in range (1,11):
        y=print (f"{n} X {1} = {n*1}")
        print (f"{n} X {2} = {n*2}")
        print (f"{n} X {3} = {n*3}")
        print (f"{n} X {4} = {n*4}")
        print (f"{n} X {5} = {n*5}")
        print (f"{n} X {6} = {n*6}")
        print (f"{n} X {7} = {n*7}")
        print (f"{n} X {8} = {n*8}")
        print (f"{n} X {9} = {n*9}")
        print (f"{n} X {10} = {n*10}")
        

        return y

m = table(5)
print(m)




















