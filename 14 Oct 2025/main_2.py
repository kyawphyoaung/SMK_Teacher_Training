area = 99

def rectangle(length,width):
    area = length*width
    circumference = (2* length)+(2*width)
    return area,circumference

area_result,cf = rectangle(10,20)
print("The area of the rectangle is",area_result)
print("Area global variable",area)
print("This is circumference",cf)