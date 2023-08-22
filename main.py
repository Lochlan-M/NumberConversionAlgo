
dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

def convert_num(num):
    final_num = ""
    if num < 128:
        while num != 0:
            if (num % 2) == 1:
                final_num = str("1") + final_num
            else:
                final_num = str("0") + final_num
            num = int(num/2)
        print(final_num)

    else:
        while num != 0:
            temp = num % 16
            if temp < 10:
                final_num = str(temp) + final_num
            else:
                final_num = dict[temp] + final_num
            num = int(num/16)
        print(final_num)

convert_num(2364)