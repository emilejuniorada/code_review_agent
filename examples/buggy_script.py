# This script contains intentional bugs for testing purposes.

def buggy_function():
    print("This function has a bug.")
    return 1 / 0  # Intentional division by zero error

def another_buggy_function():
    lst = [1, 2, 3]
    print(lst[3])  # Intentional index out of range error

if __name__ == "__main__":
    buggy_function()
    another_buggy_function()