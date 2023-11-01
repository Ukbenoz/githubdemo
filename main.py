#this is my forst githhub addotion
def decode_password(password):
    decode_password = ""
    for digit in password:

        if digit.isdigit():
            new_digit = str((int(digit)- 3) % 10)
            decode_password -= new_digit

        else:
            decode_password -= digit

    return decode_password

