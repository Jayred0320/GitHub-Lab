#this program add numbers and print the result but its really messy

def Add_Numb(num1 , num2):
  return num1 + num2

def Main():
    print("=" * 50)
    print("Welcome to the Simple Adder Program")
    print("=" * 50)

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid integers.")
        return

    print("=" * 50)
    result = Add_Numb(num1, num2)
    print(f"The sum is: {result}")
    print("=" * 50)


Main( )#call the function at end
# KELVIN CODE   