from decimal import Decimal
def CodesConverter(code):
    code_parts = code.split('-')
    int_code = ''.join(code_parts)
    return int(int_code)

def Codes_Generator(first, last):
    print('***Generator Kodow***')
    first = CodesConverter(first)
    last = CodesConverter(last)
    for code in range(first, last+1):
        part1 = code // 1000
        part2 = code % 1000
        print('{:02}-{:03}'.format(part1, part2))

def MissingElements(value_list, value):
    print('***Brakujace Elementy***')
    miss_values=[]
    for x in range (1,value+1):
        if x not in value_list:
            miss_values.append(x)
    print(miss_values)

def NumbersGenerator(start=2, stop=5.5):
    print('***Generator Liczb***')
    while start<stop:
        print(Decimal(start))
        start=start+0.5


Codes_Generator('79-900', '80-155')
MissingElements([2,3,7,4,9], 10)
NumbersGenerator()