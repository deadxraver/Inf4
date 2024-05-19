with open('schedule.xml', 'r', encoding="utf-8") as r:
    x = r.readlines()[1:]
s = ''
k = 0
print(x)
for i in range(len(x)):
    a = x[i].strip().replace('<', '>').split('>')[1:-1]
    print(a)
    if len(a) > 2:
        a = a[:-1]
    if len(a) == 1:
        if a[0][0] == '/':
            k -= 1
        else:
            s += '  ' * k + a[0] + ":" + '\n'
            k += 1
    else:
        if len(a) == 0:
            a = ""
        else:
            s += '  ' * k + a[0] + ': ' + a[1] + '\n'
with open('schedule.yaml', 'w', encoding="utf-8") as w:
    w.write(s)
