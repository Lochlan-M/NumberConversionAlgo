
dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

def convert_num(num):
    final_num = ""
    num_list = []

    if num < 128:
        while num != 0:
            if (num % 2) == 1:
                num_list.append(1)
            else:
                num_list.append(0)
            num = int(num/2)

        temp = len(num_list)
        while len(num_list) < 8:
            num_list.append(0)

        num_list = num_list[::-1]

        for i in range(len(num_list)):
            if num_list[i] == 0:
                num_list[i] = 1
            else:
                 num_list[i]= 0

        temp_boolean  = False
        temp2 = 7

        while temp_boolean == False:
            if num_list[temp2] == 0:
                num_list[temp2] = 1
                temp_boolean = True
            else:
                num_list[temp2] = 0
            temp2 -= 1

        print(num_list)

    else:
        while num != 0:
            temp = num % 16
            if temp < 10:
                final_num = str(temp) + final_num
            else:
                final_num = dict[temp] + final_num
            num = int(num/16)
        print(final_num)

convert_num(10)