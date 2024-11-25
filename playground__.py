def top(message):
    words = list(message.split(" "))
    print(words)
    dect = {}
    for i in words:
        if i not in dect:
            dect[i] = 1
        else:
            dect[i] += 1
    print(dect)

    l = list(dect.values())
    l.sort(reverse=True)
    print(l)
    newdect = {}
    for i in l:  # values  3 2 1 1
        for key in dect:
            if dect[key] == i and key not in newdect:
                newdect[key] = i

    newdect = list(newdect.items())
    if len(newdect) > 2:
        newdect = newdect[0:2]
    return newdect