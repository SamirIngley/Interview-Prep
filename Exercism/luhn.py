''' Given a number determine whether or not it is valid per the
Luhn formula. Is a checksum used to validate ID#s like credit cards etc.. 
Check if string is valid '''

def luhn_check(num):


    if len(num) < 2:
        print('Not valid')
        return 

    num_copy = num
    num_str = ''


    if ' ' in num_copy:
        num_copy = num_copy.split(' ')
        for i in num_copy:
            num_str += (i)
    
    counter = 0
    rev_doubled = ''
    reversedstr = ''.join(reversed(num_str))
    summed = 0
    for char in reversedstr:
        # print(char)
        counter += 1
        if counter % 2 == 0:
            double = int(char)*2
            if double > 9:
                double = double-9
            rev_doubled += str(double)
            summed += int(double)
        else:
            rev_doubled += char 
            summed += int(char)

    if summed % 10 == 0:
        print('valid')
        return True
    else:
        print('invalid')
        return False

if __name__ == "__main__":

    input = '12 34 5'
    luhn_check(input)
