import math
from module_y import calculate_y

def calculate_z(m):

    try:
        z = math.sqrt((m + 3) / (m - 3))
        return z
    except ZeroDivisionError:
        return "Error: division by zero"
    except ValueError:
        return "Error: invalid value for the root"





def main():

    m = float(input("Enter value m: "))
    z_result = calculate_z(m)
    print(f"Value z: {z_result}")


    n = int(input("Enter value n: "))
    y_result = calculate_y(n)
    print(f"Value y: {y_result}")



if __name__ == "__main__":
    main()