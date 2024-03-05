# Assignment
# Fares Mohammed Abdulhamid Sarhan  , ID: 20230278
# Mahmoud Mohamed El-Basel Hegazy   , ID: 20230376
# Youssef Walid Mohamed Shaker      , ID 20230517

# select the base from and the base to
def select_base(selected_before):
    # if the user selected a base before then print the convert to statement
    if selected_before:
        print("** Please select the base you want to convert a number to **")
    # if the user didn't select a base before then print the convert from statement
    else:
        print("** Please select the base you want to convert a number from **")
    # show the menu of base selection
    while True:
        print("A) Decimal")
        print("B) Binary")
        print("C) octal")
        print("D) hexadecimal")
        choice = input("")
        choice = choice.upper()
        if choice == "A":
            return "decimal"
        elif choice == "B":
            return "binary"
        elif choice == "C":
            return "octal"
        elif choice == "D":
            return "hexadecimal"
        else:
            print("Please select a valid choice")


# from decimal to base_to code
# define 'converted_number' as a string to perform concatenation on it
def from_decimal_to_binary(number):
    converted_number = ""
    while number != 0:
        converted_number = str(number % 2) + converted_number
        number = number // 2
    return converted_number


def from_decimal_to_octal(number):
    converted_number = ""
    while number != 0:
        converted_number = str(number % 8) + converted_number
        number = number // 8
    return converted_number


def from_decimal_to_hexadecimal(number):
    converted_number = ""
    while number != 0:
        if number % 16 == 10:
            converted_number = "A" + converted_number
        elif number % 16 == 11:
            converted_number = "B" + converted_number
        elif number % 16 == 12:
            converted_number = "C" + converted_number
        elif number % 16 == 13:
            converted_number = "D" + converted_number
        elif number % 16 == 14:
            converted_number = "E" + converted_number
        elif number % 16 == 15:
            converted_number = "F" + converted_number
        else:
            converted_number = str(number % 16) + converted_number
        number = number // 16
    return converted_number


def from_decimal(number, base_to):
    converted_number = ""
    # check if the provided number is a decimal
    for i in number:
        if not ("0" <= i <= "9"):
            return str(number) + " is not a valid number in base10"
    # make 'number' an integer to start the conversion
    number = int(number)
    if base_to == "decimal":
        return number

    elif base_to == "binary":
        converted_number = from_decimal_to_binary(number)

    elif base_to == "octal":
        converted_number = from_decimal_to_octal(number)

    elif base_to == "hexadecimal":
        converted_number = from_decimal_to_hexadecimal(number)

    return converted_number


# end of from decimal to base_to code block


# from binary to base_to code block
# define converted_number as integer to perform summation on it
def from_binary_to_decimal(number):
    converted_number = 0
    # convert number to a string to choose every digit in it and multiply it by 2^(weight of the bit)
    number = str(number)
    for i in range(0, len(number)):
        converted_number += int(number[i]) * (2 ** (len(number) - 1 - i))

    return converted_number


def from_binary_to_octal(number):
    converted_number = ""
    number = str(number)
    # increase the length to be a length of 3
    while len(number) % 3 != 0:
        number = "0" + number
    # select every 3 bits and convert them
    for i in range(0, len(number), 3):
        # start from the most significant bit
        sum_of_three_bits = int(number[i]) * (2 ** 2) + int(number[i + 1]) * (2 ** 1) + int(number[i + 2]) * (2 ** 0)
        converted_number += str(sum_of_three_bits)

    return converted_number


def from_binary_to_hexadecimal(number):
    converted_number = ""
    number = str(number)
    # increase the length to be a length of 4
    while len(number) % 4 != 0:
        number = "0" + number
    for i in range(0, len(number), 4):
        # start from the most significant bit
        sum_of_four_bits = (int(number[i]) * (2 ** 3) + int(number[i + 1]) * (2 ** 2) +
                            int(number[i + 2]) * (2 ** 1) + int(number[i + 3]) * (2 ** 0))
        # convert number starting from left up to right
        if sum_of_four_bits == 10:
            converted_number += "A"
        elif sum_of_four_bits == 11:
            converted_number += "B"
        elif sum_of_four_bits == 12:
            converted_number += "C"
        elif sum_of_four_bits == 13:
            converted_number += "D"
        elif sum_of_four_bits == 14:
            converted_number += "E"
        elif sum_of_four_bits == 15:
            converted_number += "F"
        else:
            converted_number += str(sum_of_four_bits)

    return converted_number


def from_binary(number, base_to):
    converted_number = 0
    # check if the provided number is a binary
    for i in number:
        if not ("0" <= i <= "1"):
            return number + "invalid number in base2"
    # make 'number' an integer to start the conversion
    number = int(number)
    if base_to == "binary":
        return number

    elif base_to == "decimal":
        converted_number = from_binary_to_decimal(number)

    elif base_to == "octal":
        converted_number = from_binary_to_octal(number)

    elif base_to == "hexadecimal":
        converted_number = from_binary_to_hexadecimal(number)
    return converted_number


# end of from binary to base_to code block


# from octal to base_to code block

def from_octal_to_decimal(number):
    converted_number = 0
    for i in range(0, len(number)):
        converted_number += int(number[i]) * (8 ** (len(number) - 1 - i))

    return converted_number


def from_octal_to_binary(number):
    octal_to_binary = [
        '000',
        '001',
        '010',
        '011',
        '100',
        '101',
        '110',
        '111'
    ]
    converted_number = ""

    for i in number:
        if i == '1':
            converted_number += octal_to_binary[int(i)]
        elif i == '2':
            converted_number += octal_to_binary[int(i)]
        elif i == '3':
            converted_number += octal_to_binary[int(i)]
        elif i == '4':
            converted_number += octal_to_binary[int(i)]
        elif i == '5':
            converted_number += octal_to_binary[int(i)]
        elif i == '6':
            converted_number += octal_to_binary[int(i)]
        elif i == '7':
            converted_number += octal_to_binary[int(i)]

    return converted_number


def from_octal_to_hexadecimal(number):
    converted_number = from_octal_to_binary(number)
    return from_binary(converted_number, "hexadecimal")


def from_octal(number, base_to):
    converted_number = 0
    # check if the provided number is octal or not
    for i in number:
        if not ("0" <= i <= "7"):
            return number + " is not a valid number in base8"

    if base_to == "octal":
        return number

    elif base_to == "decimal":
        converted_number = from_octal_to_decimal(number)

    elif base_to == "binary":
        converted_number = from_octal_to_binary(number)
    elif base_to == "hexadecimal":
        converted_number = from_octal_to_hexadecimal(number)

    return converted_number


# end of from octal to base_to code block


# from hexadecimal to base_to code block

def from_hexadecimal_to_decimal(number):
    converted_number = 0
    for i in range(0, len(number)):
        if number[i] == "A":
            converted_number += 10 * (16 ** (len(number) - 1 - i))
        elif number[i] == "B":
            converted_number += 11 * (16 ** (len(number) - 1 - i))
        elif number[i] == "C":
            converted_number += 12 * (16 ** (len(number) - 1 - i))
        elif number[i] == "D":
            converted_number += 13 * (16 ** (len(number) - 1 - i))
        elif number[i] == "E":
            converted_number += 14 * (16 ** (len(number) - 1 - i))
        elif number[i] == "F":
            converted_number += 15 * (16 ** (len(number) - 1 - i))
        else:
            converted_number += int(number[i]) * (16 ** (len(number) - 1 - i))
    return converted_number


def from_hexadecimal_to_binary(number):
    hex_to_binary = [
        '0000',
        '0001',
        '0010',
        '0011',
        '0100',
        '0101',
        '0110',
        '0111',
        '1000',
        '1001',
    ]
    converted_number = ""

    for i in number:
        if i == "A":
            converted_number += "1010"
        elif i == "B":
            converted_number += "1011"
        elif i == "C":
            converted_number += "1100"
        elif i == "D":
            converted_number += "1101"
        elif i == "E":
            converted_number += "1110"
        elif i == "F":
            converted_number += "1111"
        else:
            if i == '1':
                converted_number += hex_to_binary[int(i)]
            elif i == '2':
                converted_number += hex_to_binary[int(i)]
            elif i == '3':
                converted_number += hex_to_binary[int(i)]
            elif i == '4':
                converted_number += hex_to_binary[int(i)]
            elif i == '5':
                converted_number += hex_to_binary[int(i)]
            elif i == '6':
                converted_number += hex_to_binary[int(i)]
            elif i == '7':
                converted_number += hex_to_binary[int(i)]
            elif i == '8':
                converted_number += hex_to_binary[int(i)]
            elif i == '9':
                converted_number += hex_to_binary[int(i)]

    return converted_number


def from_hexadecimal_to_octal(number):
    converted_number = from_hexadecimal_to_binary(number)
    return from_binary(converted_number, "octal")


def from_hexadecimal(number, base_to):
    converted_number = 0
    for i in number:
        if not ('A' <= i <= 'F') and not ("0" <= i <= "9"):
            return number + " is not a valid number in base16"

    if base_to == "hexadecimal":
        return number
    # convert to decimal by default
    elif base_to == "decimal":
        converted_number = from_hexadecimal_to_decimal(number)

    elif base_to == "octal":
        converted_number = from_hexadecimal_to_octal(number)
    elif base_to == "binary":
        converted_number = from_hexadecimal_to_binary(number)

    return converted_number


# end of from hexadecimal to base_to code block


# start of the program
def main():
    print("** numbering system converter **")

    while True:
        print("A) insert a new number")
        print("B) Exit program")
        choice = input("")
        choice = choice.upper()
        if choice == "B":
            print("Exiting")
            return

        elif choice == "A":
            number = input("Please insert a number: ")
            # the provided boolean argument is to check if the user chose a base before or not
            # to output a different statement
            # get the base of the user's number
            base_from = select_base(False)
            # get the base the user wants to convert the number to
            base_to = select_base(True)

            if base_from == "decimal":
                number = from_decimal(number, base_to)

            elif base_from == "binary":
                number = from_binary(number, base_to)

            elif base_from == "octal":
                number = from_octal(number, base_to)

            elif base_from == "hexadecimal":
                number = number.upper()
                number = from_hexadecimal(number, base_to)
            print(number)
        else:
            print("please insert a valid choice")


main()
