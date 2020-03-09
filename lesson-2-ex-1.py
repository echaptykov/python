'''
    Урок 2 Задание 1
'''
def print_type_script (in_list):
    in_list_len = len (in_list)
    for i in range(in_list_len):
        print(f"Тип данных {type(in_list[i])} : {in_list[i]}")

ls_tuple = (1,2)
ls_list_1 = [1,2,"3"]
ls_list = [1,"Василий",3.4, [2,4,6], True, ls_tuple, -3.9, ls_list_1]
print_type_script(ls_list)