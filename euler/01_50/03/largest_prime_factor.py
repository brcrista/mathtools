from core import factors, is_prime

def solution(n: int) -> int:
    return max(filter(is_prime, factors(n)), default=None)

def main():
    print(solution(600851475143))

if __name__ == '__main__':
    main()
