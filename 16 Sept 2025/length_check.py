postCode = input("Enter the postcode")
try:
    postCode_num = int(postCode)
    length = len(postCode)
    if length >= 6 and length <= 8:
        print("Valid")

        if postCode_num > 111001:
            #reterive township names from another array
            print("This post code is greater than 111001")
        else:
            print("This post code is less than 111001")
    else:
        print("Invalid")
except ValueError as e:
    print(f"Error: {e}")

