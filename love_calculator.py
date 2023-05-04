# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1=name1.lower()
# print(lower_name1)
lower_name2=name2.lower()
t=lower_name1.count("t") + lower_name2.count("t")
r=lower_name1.count("r") + lower_name2.count("r")
u=lower_name1.count("u") + lower_name2.count("u")
e=lower_name1.count("e") + lower_name2.count("e")
# print(f"{t},{r},{u},{e}")
true= t+r+u+e
# print(true)
l=lower_name1.count("l") + lower_name2.count("l")
o=lower_name1.count("o") + lower_name2.count("o")
v=lower_name1.count("v") + lower_name2.count("v")
e=lower_name1.count("e") + lower_name2.count("e")
love=l+o+v+e
# print(love)
love_value= int(str(true)+ str(love))
if (love_value<10) or (love_value>90):
    print(f"Your score is{love_value},you go together like coke and mentos") 
elif love_value>40 and love_value<50:
    print(f"Your score is{love_value},you are alright together.")
else:
    print(f"Your score is{love_value}")