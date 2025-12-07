
for row in range(1, 6):
    for col in range(1, 6):
        product = row*col
        print(f'{product:3}', end='')
    print()

print('')

for row in range(5):
    for col in range(5):
        print(f'Row {row}, Column {col}')