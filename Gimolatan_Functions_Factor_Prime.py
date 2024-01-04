print('CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM')
print('CREATED BY: BRANDON IAN GIMOLATAN')
print()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def smallest_factor(n):
    if n <= 1:
        return None
    for i in range(2, n+1):
        if n % i == 0:
            return i

while True:
    print("Menu:")
    print("1. Find the smallest factor of a number")
    print("2. Display prime numbers within a range")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Program terminated.")
        break
    elif choice == 1:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Enter a non-negative number.")
        else:
            factor = smallest_factor(num)
            if factor:
                print(f"The smallest factor of {num} is {factor}")
            else:
                print(f"{num} has no factors other than 1 or itself.")
    elif choice == 2:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        if start < 0:
            print("Enter a non-negative start number.")
        elif end < start:
            print(f"Enter a number greater than {start}.")
        else:
            print(f"Prime numbers within the range {start} to {end}:")
            for num in range(start, end + 1):
                if is_prime(num):
                    print(num, end=" ")
            print()
    else:
        print("Invalid choice. Please enter a valid option (0, 1, or 2).")
