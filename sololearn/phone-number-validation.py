import re

def check_Phone(number):
    check_reg = r"^(1|8|9)\d{7}$"
    reg_number = re.match(check_reg, number)
    if reg_number:
        print("Valid")
    else:
        print("Invalid")
    



def main():
    number = input()
    x=""
    while x != "n":
        number = input()
        check_Phone(number)
        x = input("repetir teste? (s/n)")
 
        
if __name__ == "__main__":
    main()