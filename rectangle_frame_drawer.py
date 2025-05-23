hor_line = int(input('Enter the width of the frame: '))
ver_line = int(input('Enter the height of the frame: '))

for hor in range(hor_line):
    for ver in range(ver_line):
        if hor == 0 or hor == hor_line - 1:
            print('-', end='')
        elif ver == 0 or ver == ver_line - 1:
            print('|', end='')
        else:
            print(' ', end='')
    print()
