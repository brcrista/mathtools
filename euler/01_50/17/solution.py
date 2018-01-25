from typing import overload

ones = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

teens = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

tens = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

#pylint: disable=unused-argument,function-redefined
@overload
def to_english(numeral: int) -> int:
    pass

@overload
def to_english(numeral: str) -> int:
    pass

def to_english(numeral) -> str:
    """Get the English word or phrase for a numeral between '1' and '1000'."""
    if isinstance(numeral, int):
        return to_english(str(numeral))

    if not numeral:
        return ''
    elif numeral[0] == '0':
        return to_english(numeral[1:])
    elif len(numeral) == 1:
        return ones[numeral]
    elif len(numeral) == 2:
        if numeral in teens:
            return teens[numeral]
        else:
            result = tens[numeral[0]]
            if numeral[1] == '0':
                return result
            else:
                return result + ' ' + to_english(numeral[1])
    elif len(numeral) == 3:
        result = ones[numeral[0]] + ' hundred'
        if all(c == '0' for c in numeral[1:]):
            return result
        else:
            return result + ' and ' + to_english(numeral[1:])
    elif len(numeral) == 4:
        return 'one thousand'
    else:
        raise ValueError(f'numeral not recognized: {numeral}')
#pylint: enable=unused-argument,function-redefined

def number_letter_counts(n: int) -> int:
    words = [to_english(i) for i in range(1, n + 1)]
    return sum(len([c for c in word if c != ' ']) for word in words)

def main():
    print(number_letter_counts(1000))

if __name__ == '__main__':
    main()
