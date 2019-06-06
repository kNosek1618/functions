
#function in program
def say_hi():
    print("Hello user :)")

say_hi()

print("")
#using the function
def kind_of_car(name):
    print("Name this car is " +name)

kind_of_car("Ferrari")
kind_of_car("Maserati")

print("")
#using the function 1.2
def kind_of_car(name, HP):
    print("Name this car is " +name+ " and he have " +str(HP)+ " HP.")

kind_of_car("Ferrari", 605)
kind_of_car("Maserati", 440)

print("")

def cube(num):
    return int(num)*int(num)*int(num)

print ("Enter number, I will raise it to the third power:")
result = cube(input())
print(result)

###RESULT###
