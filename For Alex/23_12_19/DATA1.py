data1=[1,2,3,[1,2,3,4,5,6],[[1,2],[3,4],[5,6]],((1,2),(3,4))]

def Short_lists(data):
    short_list = []
    short = len(data)

    for i in data:
        if type(i) == type(list()):
            for x in i:
                if type(x) == type(list()):
                    if len(x) < short:
                        short_list.append(x)
    return short_list

def reborn_list(data):
    newb_list = []
    for i in data:
        newb_list = newb_list + i

    return newb_list


McShorty = Short_lists(data1)
newb = reborn_list(McShorty)
print(newb)
    
#run = Short_lists(data1)


#print(run)


#i don't understand why it's only printing one group list....
# well a friend just helped it was the spaces amount in line 13
