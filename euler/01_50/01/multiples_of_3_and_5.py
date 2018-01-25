from core import divides

def solution(n: int) -> int:
    return sum(x for x in range(0, n) if divides(x, 3) or divides(x, 5))

def main():
    print(solution(1000))

if __name__ == '__main__':
    main()
