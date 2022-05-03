# for num in range(10):
#     print(num)

# for num in range(1, 11):
#     print(num)

# for num in range(0, 11, 2):
#     print(num)

# for digit in range(1,6):
#     print(digit)

# for digit in range (-0,101):
#     print(digit)

# for digit in range(-0,101, 5):
#     print(digit)

# numbers = [10,20,30,40]
# # print(numbers[0])
# # print(numbers[1])
# # print(numbers[2])
# # print(numbers[3])
# for number in numbers:
#     print(number)



# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# # for item in range(len(chilli_wishlist)):
# #     print(chilli_wishlist[item])

# for item in chilli_wishlist:
#     print(item)


# chilli_wishlist = [["igloo"],["donut toy", "tennis ball", "crocodile toy"],["chicken", "peanut butter"],["cardboard box", "kong", "dig mat"]]

# for category in chilli_wishlist:
#     for item in category:
#         print(item)


# guess = " "
# while guess != "a":
#     guess = input("Guess a letter: ")


# counter = 10
# while counter <= 10:
#     print(counter)
#     counter = counter + 1

# num = 1
# while num > 0:
#     print("Hi")



# for num in range(3):
#     print(num)



groceries = [ ["Baby Spinach", 2.78], ["Hot Chocolate", 3.70], ["Crackers", 2.10], ["Bacon", 9.00], ["Carrots", 0.56], ["Oranges", 3.08] ]

# for item in range(len(groceries)):
#     print(groceries)

# for category in groceries:
#     for item in category:
#         print(item)



# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")

def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
 
n = 5
pypart(n)


def triangle(n):
	
	k = n - 1

	for i in range(0, n):
	
		for j in range(0, k):
			print(end=" ")
	

		k = k - 1

		for j in range(0, i+1):
		
			print("* ", end="")
	
		print("\r")

n = 5
triangle(n)


number = int(input("Enter a number: "))

for i in range(1,number+1):
    print(f"{number} * {i} = {number * i}")



474
















