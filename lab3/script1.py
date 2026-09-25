# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

k = int(input("Integer k:"))
n = int(input("Integer n:"))

if n > 0:
    print("The square of k to the n is ", k**2 )
    print("The multiplication of k and n is ", k*n)
    print("The division of k and n is  ", round(k/n) )
    print("The integer division of k and n is ", k//n)
    print("The modular of k and n is ", k%n)
    print("The addition of k and n is ", k +n )
    print("The substraction of k and n is",k-n )
else:
    print("The value of n is less than or equal to zero")


a = int(input("Integer a:"))
b = int(input("Integer b:"))
c = int(input("Integer c:"))

root1 = ((-b) + ((b**2) - (4*a*c)**1/2))/(2*a)
root2= ((-b) - ((b**2) - (4*a*c)**1/2))/(2*a)

print("root1:",root1)
print("root2:",root2)
