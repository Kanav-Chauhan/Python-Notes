# Problem No.1
# n1 = int(input("Enter Number 1 \n"))
# n2 = int(input("Enter Number 2 \n"))
# n3 = int(input("Enter Number 3 \n"))
# n4 = int(input("Enter Number 4 \n"))

# if n1>n2:
#  f1=n1
# else :
#  f1 = n2

# if n3>n4:
#  f2=n3
# else: 
#  f2= n4

# if f1>f2:
#     print(f1)

# else :
#     print(f2)

# Problem No.2
# m1 = int(input("English Marks\n"))
# m2 = int(input("Maths Marks\n"))
# m3 = int(input("Hindi Marks\n"))

# if (m1 or m2 or m3)<33 :
#     print ("You are fail")

# elif ((m1+m2+m3)/3)<40:
#     print(" You are failed due to low percentage ")

# elif ((m1 and m2 and m3)>=33) and (((m1+m2+m3)/3)>40) and (((m1+m2+m3)/3)<=100):
#     print ("You are passed") 
# else :
#     print("Kindly Enter the Correct Marks")

# Problem No.3

# comment = input("Enter Your Comment\n")

# if ("make a lot of money" in comment):
#     print ("This is a spam" )
# elif ("Buy now" in comment):
#     print ("This is a spam" )
# elif ("subscribe this" in comment):
#     print ("This is a spam" )
# elif ("click this" in comment):
#     print ("This is a spam" )
# else:
#     print("This is a valid comment")

# Problem No.4

# username = input("Enter your username\n")

# if len(username)<10:
#     print("The username can't be assigned due to less than 10 characters")

# else:
#     print ("Your username contain 10 or more characters  ") 


# Problem No.5

# names = ["raju","rahul","anagha","sakti","sanjana","harsh","kanav","vishal","sidhaart"]
# print(names)

# finder = input("Enter the name to find \n")

# if (finder in names):
#     print ("Name Present") 

# else :
#     print("Name is not in the list ")


# Problem NO.6

# marks = int(input("How much you score\n"))

# if (marks>90) and (marks<=100):
#     print("Excellent")

# elif (marks>80) and (marks<=90):
#     print("A")

# elif (marks>70) and (marks<=80):
#     print("B")

# elif (marks>60) and (marks<=70):
#     print("C")

# elif (marks>=50) and (marks<=60):
#     print("D")

# elif (marks<50):
#     print("F")

# else :
#     print ("Enter the Valid marks")

# Problem No.7

# post = "hArry is a good boy"

# if ("harry" in post):
#     print("This post is talking about harry")
# elif ("Harry" in post):
#     print("This post is talking about harry")
# elif ("HARRY" in post):
#     print("This post is talking about harry")
# elif ("hArry" in post):
#     print("This post is talking about harry")
# elif ("haRry" in post):
#     print("This post is talking about harry")
# elif ("harRy" in post):
#     print("This post is talking about harry")
# elif ("harrY" in post):
#     print("This post is talking about harry")
# else:
#     print("Harry is not is the post")






a = ["hero","leo","dick","ass"]

f = input("enter the name to be found\n" )

if f in a :
    print (" name found")

else :
    print("name not found")