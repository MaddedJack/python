#puzzzle monkey game

x = 5
y = 3
ht = 21
at = 0
mi = 0
while(at != ht):
    mi = mi+1
    if(mi %2 ==0):
        at = at-y
    else:
        at = at+x
print(mi)
