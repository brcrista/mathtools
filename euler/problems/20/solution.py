from math import factorial

def factorial_digit_sum(n: int) -> int:
    return sum(int(c) for c in str(factorial(n)))

def main():
    print(factorial_digit_sum(100))

if __name__ == '__main__':
    main()

