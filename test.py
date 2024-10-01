
# # cits = 5
# # ievade = int(input("ievadiet skaitli"))
# # print(ievade)
# # Lielaks = ievade + 1
# # print("skaitlis, kas ir lielaks par 1 :",Lielaks)
# print(6<1)

# number = int(input("Give me a number!: "))
# if(number>=10):
#     print("big nigga")
# elif(number<5):
#     print("small nigga")
# elif(number>10 and number<20):
#     print("medium nigga")
# else:
#     print("average nigga")

def calculate(num1, num2):
    reiz = num1*num2
    if (reiz<=20):
        return reiz
    return num1+num2
for i in range(10):
    print (calculate(3,i))

answ = "y"
while(answ == "y"):
    print(calculate(int(input("Give me a first number!: ")),int(input("Give me a second number!: "))))
    answ = input("Vai velaties turpinat? (ievadiet 'y'): ")