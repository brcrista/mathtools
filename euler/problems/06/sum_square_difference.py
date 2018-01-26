def square_of_sum(n: int) -> int:
    return sum(range(1, n + 1)) ** 2

def sum_of_squares(n: int) -> int:
    return sum(x ** 2 for x in range(1, n + 1))

def solution(n: int) -> int:
    return square_of_sum(n) - sum_of_squares(n)

def main():
    print(solution(100))

if __name__ == '__main__':
    main()
