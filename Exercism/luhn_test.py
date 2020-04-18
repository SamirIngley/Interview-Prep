from luhn import luhn_check

def test_normal_invalid():
    input = '8273 1232 7352 0569'
    luhn_check(input)

def test_normal_valid():
    input = '4539 1488 0343 6467'
    luhn_check(input)

