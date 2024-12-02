


def merge(l1, l2):
    i = 0
    j = 0
    l = []

    while len(l1) > i and len(l2) > j:
        if int(l1[i]) < int(l2[j]):
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    l.extend(l1[i:])
    l.extend(l2[j:])

    #print(l)
    return l    

def sort(list):
    if len(list) <= 1:
        return list
    
    m = int(len(list)//2)
    l1 = sort(list[:m])
    l2 = sort(list[m:])

    return merge(l1, l2)

try:
    for i in sort(input('Entre your numbers: ').split()):
        print(int(i), sep='', end=' ')

except:
    print('Next time enter you numbers correctly.')
