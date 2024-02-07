""" animals = ["Zebra", "Camel", "Ape"] """
""" print(animals[0]) """
""" for animal in animals:
    print(animal) """
""" for animal in animals:
    if (animal == "Camel"):
        print("Camel") """
""" x = "Hello Eason" """
""" print(x[0])
y = x.upper()
print (y)
 """



""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") 
words_list = x.split( )
print(len(words_list)) 
"""



""" service = input("service was:")
if service == "bad":
    print("0% tip")
elif service == "okay":
    print("15% tip")
elif service == "good":
    print("20% tip")
elif service == "great":
    print("25% tip") """

""" x = input("ailsdfhgbiolsdf")
if(int(x) == ["2","4","6","8","10"]):
    print("even") """


""" num = int(input("number: "))
if (num % 2)  == 0:
    print('even')
else: 
    print('odd') """


number = int(input("number1: "))
number2 = int(input("number2: "))

""" print("Factors1: " .format(number))
for i in range(1, number + 1):
    if(number % i == 0):
        print (i)

print("Factors2: " .format(number2))
for i in range(1, number2 + 1):
    if(number2 % i == 0):
        print (i) """

def gcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller +1):
        if (x % i == 0) and (y % i == 0):
            gcf = i
    return gcf

print("GCF:", gcf(number, number2))
