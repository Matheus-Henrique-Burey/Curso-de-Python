from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valore sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
print(f'\nO maior numero foi {max(num)}')
print(f'O menor numero foi {min(num)}')
