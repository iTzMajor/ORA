data3=(5,5,'a','b','c','a','c',5,'5','z','g','x')

def the_exorcist(data):
    for x in data:
        print(x)

"""
all = the_exorcist(data3)
print(all)
"""

def one_of_a_tuple(data):
    new_list= []

    for x in data3:
        if x not in new_list:
            new_list.append(x)

    new_list = tuple(new_list)
    return new_list

run = one_of_a_tuple(data3)

print(run)

