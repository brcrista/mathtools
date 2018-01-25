from core import binomial_coefficient

def lattice_paths() -> int:
    """The number of lattice paths on a 20 x 20 grid."""
    return binomial_coefficient(40, 20)

def main():
    print(lattice_paths())

if __name__ == '__main__':
    main()
