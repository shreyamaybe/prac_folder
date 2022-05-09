
#first py prog: 1
print ("hello world!")

#variables: 2
name= "Shreya" 
age= 20
is_student= True

#receiving Input: 3
name= input("what is your name? ")
print(name)

#type conversion: 4
age= input("Enter your birth year: ")
age_calc= 2022-int(age)
print("Age: " + age_calc)

#arithmetic operators: 5
  # + addition 
  # - substraction 
  # * multiplication 
  # / float division 
  # // integer division 
  # % remainder 
  # ** to the power of 

x=10
y=x+10
print(y)

#operator precedence (bodmas): 6
x= 10 +3 *2 #ans:16
y= (10+3) *2 #ans:26
print(x)
print(y)

#comparison operators: 7
x= 5>4 #ans: True
y= 10>20 #ans: False
  # >, >=, <, <=, ==(equals to), !=(not equal to)

#logical operators: 8
price=25
print(price>10 and price<30) #ans:True
print(price<10 or price<30) #ans: True
print(not price>10) #ans: False
  #and (both)
  #or(at least one)
  #not