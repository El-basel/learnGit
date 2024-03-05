def decimal_to_binary(decimal):
    decimal = int(decimal)
    bin = ""
    while decimal >= 1 :
        remainder = decimal % 2
        bin = str(remainder) + bin
        decimal = decimal // 2
    return bin
def bin_to_dec(bin):
    i = len(bin) - 1
    dec = 0
    p = 0
    while i >= 0 :
        if bin[i] == "1" :
            dec = 2 ** p + dec
        p += 1
        i -= 1
    return dec
def octa_to_dec(octa):
    i = len(octa) - 1
    p = 0
    dec = 0
    while i >= 0:
        dec += int(octa[i]) * 8**p
        p += 1
        i -= 1
    return dec
def hexa_to_decimal(hexa):
    hexa = hexa.upper()
    i = len(hexa) - 1
    p = 0
    dec = 0
    while i >= 0:
        if hexa[i] == "A":
            dec += 10 * 16**p
        elif hexa[i] == "B":
            dec += 11 * 16**p
        elif hexa[i] == "C":
            dec += 12 * 16**p
        elif hexa[i] == "D":
            dec += 13 * 16**p
        elif hexa[i] == "E":
            dec += 14 * 16**p
        elif hexa[i] == "F":
            dec += 15 * 16**p
        else:
            dec += int(hexa[i]) * 16 **p
        p += 1
        i -= 1
        if p > 4:
            p = 0
    return dec
def dec_to_octal(dec):
    octal = ""
    dec = int(dec)
    while dec >= 1:
        remainder = dec % 8
        octal = str(remainder) + octal
        dec = dec // 8
    return octal
def dec_to_hexa(dec) :
    dec = int(dec)
    hexa = ""
    while dec >= 1 :
        if dec %16 == 10 :
            hexa = "A" + hexa
        elif dec %16 == 11 :
            hexa = "B" + hexa
        elif dec %16 == 12 :
            hexa = "C" + hexa
        elif dec %16 == 13 :
            hexa = "D" + hexa
        elif dec %16 == 14 :
            hexa = "E" + hexa
        elif dec %16 == 15 :
            hexa = "F" + hexa
        else :
            remainder = dec % 16
            hexa = str(remainder) + hexa
        dec = dec // 16
    return hexa
def bin_to_octal(bin):
    dec = bin_to_dec(bin)
    octal = dec_to_octal(dec)
    return octal
def bin_to_hexa(bin):
    dec = bin_to_dec(bin)
    hexa = dec_to_hexa(dec)
    return hexa
def octal_to_bin(octal):
    dec = octa_to_dec(octal)
    bin = decimal_to_binary(dec)
    return bin
def hexa_to_bin(hexa):
    dec = hex_to_dec(hexa)
    bin = decimal_to_binary(dec)
    return bin
def hexa_to_octal(hexa):
    dec = hex_to_dec(hexa)
    octal = dec_to_octal(dec)
    return octal
def octal_to_hexa(octal):
    dec = octa_to_dec(octal)
    hexa = dec_to_hexa(dec)
    return hexa
def base_from():
    print("*what base do you want to convert from*")
    print("A)decimal\nB) binary\nC) hexadecimal\nD) octal")
    choice1 = input("")
    choice1 = choice1.upper()
    if choice1 not in ["A", "B", "C", "D"]:
        print("Invalid")
    else : return choice1
def base_to():
    print("*what base do you want to convert to*")
    print("A)decimal\n B) binary\n C) hexadecimal\n D) octal")
    choice2 = input("")
    choice2 = choice2.upper()
    if choice2 not in ["A", "B", "C", "D"]:
        print("Invalid")
    else : return choice2
def convert(choice1, choice2, user):
    if choice1 == "A" and choice2 == "B" :
        print(decimal_to_binary(user))
    elif choice1 == "A" and choice2 == "C" :
        print(decimal_to_hexa(user))
    elif choice1 == "A" and choice2 == "D" :
        print(decimal_to_octal(user))
    elif choice1 == "B" and choice2 == "A" :
        print(binary_to_decimal(user))
    elif choice1 == "B" and choice2 == "C" :
        print(binary_to_hexa(user))
    elif choice1 == "B" and choice2 == "D" :
        print(binary_to_octal(user))
    elif choice1 == "C" and choice2 == "A" :
        print(hexa_to_decimal(user))
    elif choice1 == "C" and choice2 == "B" :
        print(hexa_to_bin(user))
    elif choice1 == "C" and choice2 == "D" :
        print(hexa_to_octal(user))
    elif choice1 == "D" and choice2 == "A" :
        print(octa_to_dec(user))
    elif choice1 == "D" and choice2 == "B" :
        print(octal_to_bin(user))
    elif choice1 == "D" and choice2 == "C" :
        print(octa_to_hexa(user))
    else: print("Invalid")
def main():
    while True:
        print("A) insert a new number \nB) Exit ")
        choice = input("")
        choice = choice.upper()
        if choice == "A":
            user = input("Enter a number: ")
            choice1 = base_from()
            choice2 = base_to()
            convert(choice1, choice2, user)
        elif choice == "B":
            return
        else: print("enter an invalid choice")


main()
