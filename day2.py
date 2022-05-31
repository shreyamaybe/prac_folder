#if statements: 9
temp= 25
if temp>30:
    print("Its hot out there.")
elif temp>20:  #(20, 30]
    print("Its a good weather.")
else:
    print("Its a cold weather.")


#use {} to represent a block of code

#while loop: 10
i=1
while i<=5:
    print(i)
    i=i+1
j=1
while j<=10:
    print(j * "*")
    j=j+1

#lists: 11
fruits= ["apple", "banana", "orange", "berry"]
print(fruits[0]) #ans: apple
print(fruits[-1]) #ans: berry
print(fruits[0:2]) #ans: apple, banana, orange
fruits[1]= "grapes" #replaces banana with grapes
del(fruits[2]) #deletes orange


#list methods: 12
num=[1, 2, 4, 5]
num.append(6)
num.insert(2,3)
num.remove(6)
print(num)
print(len(num)) #length of the list
print(1 in num) #ans: True (if 1 is in the list)
num.clear() #clears all
print(num)


#for loops: 13                      #using while: i=0
nums=[1, 2, 3, 4]                   #             while i<len(nums):
for items in nums:                  #                print(nums[i])
    print(items)                    #                i=i+1



#range function:14
for numbers in range(1, 10, 2): #(start, end, step)
    print(numbers)

#tuples: 15
numbers= (1, 2, 3, 4)
#unchangable kinda


#dictionaries: 16
monthConversion= {
    "jan": "january",
    "feb": "february",
    "mar": "march"
}
print(monthConversion["mar"])
print(monthConversion.get("mar"))