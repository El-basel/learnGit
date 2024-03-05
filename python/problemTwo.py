# Assignment
# Fares Mohammed Abdulhamid Sarhan  , ID: 20230278
# Mahmoud Mohamed El-Basel Hegazy   , ID: 20230376
# Youssef Walid Mohamed Shaker      , ID 20230517



def number_input(selected_before):
	# Create a loop for inserting a number
	while True:
		if selected_before:
			number = input("Please insert a binary number: ")
		else:
			number = input("Please insert a second binary number: ")
			
		# check if the input is a binary number or not
		binary_check = True
		valid_numbers = ["1" , "0"]

		for i in number:
			if i not in valid_numbers:
				binary_check = False

		if not binary_check:
			print("please insert a valid binary number")
		else:
			return number


def operation():
	
	while True:
		
		print ("** please select the operation**")
		print ("A) Compute one's complement")
		print ("B) Compute two's complement")
		print ("C) addition")
		print ("D) subtraction")
		operation_choice = input("").upper()
		if operation_choice == "A":
			return "one's complement"
		elif operation_choice == "B":
			return "two's complement"
		elif operation_choice == "C":
			return "add"
		elif operation_choice == "D":
			return "subtract"
		else:
			print("Please select a valid choice")

def onescomplement(number):
	ones_complement = ""

	#Start counting from LSB to the MSB
	i = len(number) - 1

	#Create a loop to convert every 1 to 0 and every 0 to 1
	while i>=0:
		if number[i] == "0":
			ones_complement = "1" + ones_complement
		elif number[i] == "1":
			ones_complement = "0" + ones_complement
		i = i-1
	return ones_complement

def twoscomplement(number):
	twos_complement = ""

	#To start counting from LSB to the MSB
	i = len(number) - 1

	#Create loop to locate the right most 1 in the number
	while i >= 0 and number[i] != "1":
		twos_complement = "0" + twos_complement
		i -= 1

	#to add the 1 we found
	twos_complement = "1" + twos_complement

	#to start the index after the 1 we found
	i -= 1
	
	#loop to convert every 1 to 0 and every 0 to 1
	while i >= 0:
			if number[i] == "0":
					twos_complement = "1" + twos_complement
			elif number[i] == '1':
					twos_complement = "0" + twos_complement
			i -= 1
	return twos_complement

def sum(first_number , second_number):
	#define index of first and second number for looping
	i = len(first_number) - 1
	j = len(second_number) - 1

	#create string values for carry and result
	carry = 0
	result = ""

	#create loop for adding according to index value or if carry has a number
	while i >= 0 or j >= 0 or carry:
		total = carry
		
		if i >= 0:
			total += int(first_number[i])
			i -= 1
			
		if j >= 0:
			total += int(second_number[j])
			j -= 1
			
		result = str(total % 2) + result
		carry = total // 2
		
	return result


def subtract(first_number , second_number):
	# Find the maximum length of the binary numbers
	max_length = max(len(first_number), len(second_number))
	
	# add zeros to the numbers for them to have equal lengths
	first_number = "0" * (max_length - len(first_number)) + first_number
	second_number = "0" * (max_length - len(second_number)) + second_number
	
	# create strings to represent result and borrow
	borrow = 0
	result = ""
	
	# create loop such that the index moves from left to right with 1 step at a time and stops at index = 0
	for i in range(max_length - 1, -1, -1):
		index_of_first_number = int(first_number[i])
		index_of_second_number = int(second_number[i])
	
		# subtract the borrow from the first number if there is a borrow from a past operation
		index_of_first_number -= borrow
	
		# reset borrow
		borrow = 0
	
		# create if statement for borrowing
		if index_of_first_number < index_of_second_number:
			index_of_first_number += 2
			borrow = 1
	
		result = str(index_of_first_number - index_of_second_number) + result
	
	return result


def main():
	# Print the starting screen
	print("** binary calculator **")

	# Create Start screen loop
	while True:
		print("A) Insert new numbers")
		print("B) Exit")
		choice = input().upper()

		# If the user chooses B, terminate the program
		if choice == "B":
			print ("Exiting")
			return

		elif choice == "A":
			first_number = number_input(True)

			# Ask user for operation
			operation_choice = operation()
	
			if operation_choice == "one's complement":
				result = onescomplement(first_number)
				print (result)
	
			elif operation_choice == "two's complement":
				result = twoscomplement(first_number)
				print (result)
	
			elif operation_choice == "add":
				second_number = number_input(False)
				result = sum(first_number, second_number)
				print(result)
	
			elif operation_choice == "subtract":
				second_number = number_input(False)
				result = subtract(first_number, second_number)
				print(result)

		else:
			print("please select a valid choice")


main()
