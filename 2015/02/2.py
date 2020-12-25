with open('input.txt') as file:
    f = file.read().splitlines()

    total = 0
    ribbon_total = 0
    for dims in f:
        l,w,h = [int(n) for n in dims.split('x')]
        surface = 2*l*w + 2*l*h + 2*w*h
        bow = l*w*h
 
        slack = min(l*w, l*h, w*h)
        ribbon = min(2*(l+w), 2*(l+h), 2*(w+h))

        total += surface + slack
        ribbon_total += ribbon + bow

print('Total surface: ', total)
print('Total ribbon: ', ribbon_total)
