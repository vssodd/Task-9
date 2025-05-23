rows = int(input('Enter the number of rows: '))
cols = int(input('Enter the number of columns: '))

for row in range(rows):
    for col in range(row, row + cols * 2, 2):
        print(col, end='\t')
    print()
