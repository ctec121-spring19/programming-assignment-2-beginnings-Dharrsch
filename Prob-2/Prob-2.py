# Module 2
#   Programming Assignment 2
#     Prob-2.py

# YOUR NAME

# Follow the steps below. Add your code in the blank line after each comment

# define the main function with no parameters
def main():
    # create a variable and assign it the value returned by an input function
    # that asks the user for a number. Don't forget to use the int() function.
    num= int(input("Enter a number: "))
    # print out a message that says: "The sqare of ? is ?" where the question
    # marks are replaced with the value read in from the user and its square.
    print("num", num, "num squared: ",num*num)
    # copy your input statement from above and replace "int" with "float"
    num= float(input("Enter a number: "))
    # copy the print statment from above
    print("num", num, "num squared: ",num*num)
    # copy your input statement from above and replace "int" with "eval"
    num= eval(input("Enter a number: "))
    # copy the print statment from above
    print("num", num, "num squared: ",num*num)
# call the function main
main()