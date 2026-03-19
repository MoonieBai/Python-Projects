#Creating a small python project that keeps only the even numbers
#Even numbers are exactly divisble by 2

#Step1- Create a list of 10 numbers
nums = [2,5,7,55,66,77,88,99,100,1]
#Step2- write a for loop! for loops can be used when the no
#of values is known else you can use a while loop to loop over if you don't know

even_numbers = []

for num in nums:
    if num % 2 == 0:
        print("This is an even number: ", num)
        even_numbers.append(num)

print(even_numbers)
       
   
