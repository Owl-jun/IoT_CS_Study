import core
import data_io
import random

data = data_io.load_data()
f_names = ['강','김','구','이','황','최','하','진','임','왕','오','정']
s_names = ['석','호','준','주','오','민','지','자','영','소','이','정','식','동','팔','춘','구','찬','청','희','하','수']

def make_num(num):
    result = ''
    if num < 10:
        result = "000" + str(num)
    elif num < 100:
        result = "00" + str(num)
    elif num < 1000:
        result = "0" + str(num)
    elif num == 0:
        result = "0000"
    else: result = str(num)
    return result

def make_test():
    for _ in range(10000):
        name = random.choice(f_names) + ''.join(random.sample(s_names,2)) 
        f_num = make_num(random.randint(0,10000))    
        l_num = make_num(random.randint(0,10000))    
        phone = "010-" + f_num + "-" + l_num
        core.add_contact(data,name,phone)

    data_io.save_data(data)
