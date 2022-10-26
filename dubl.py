def count_letter(string):
    list=[]
    dublicate=[]
    k=0
    for letter in string :
        if letter in list and letter not in dublicate:
            k+=1
            dublicate.append(letter)
        else:
            list.append(letter)
    return k





def count_duplicates(string):
    return len([ch for ch in (set (string.lower())) if string.lower().count(ch)>1])

import time
def worktime(f1, f2):
    def f(string):
        initial_time = time.time()
        f1(string)
        first = time.time() - initial_time
        f2(string) 
        second = time.time() - initial_time
        print(f1.__name__ if first >= second else f2.__name__)
    return f
function = worktime(count_duplicates, count_letter)
function ('aaaBbbc')

