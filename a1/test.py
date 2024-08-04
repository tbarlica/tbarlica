s = '+93'

if s[0] in '-+0123456789':
    for i in s[1:]:
        if i not in '0123456789':
            print('not ok')
            break
        else:
            print('ok')
            break
else:
    print('not ok')