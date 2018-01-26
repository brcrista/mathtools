from core import fibonacci_numbers

def index_of_first_thousand_digit_fibonacci_number() -> int:
    # problem is defined with F_1 = 1, F_2 = 1, ..., so add 2 to the index
    return next(i + 2 for i, fib in enumerate(fibonacci_numbers()) if len(str(fib)) == 1000)

def main():
    print(index_of_first_thousand_digit_fibonacci_number())

if __name__ == '__main__':
    main()
