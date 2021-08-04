file = open('usuarios.txt', 'r')
newfile = open('relatorio.txt', 'w')

names = []
mb = []
num_of_lines = 0

for lines in file:
    names.append(lines.split()[0])
    mb.append(lines.split()[1])
    num_of_lines += 1

newfile.write(f'ACME. Inc. Uso do espaço em disco pelos usuários\n------------------------\n')

for num in range(1, num_of_lines+1):
    newfile.write(str(num) + ' ' + names[num-1].capitalize() 
        + ' ' + mb[num-1] + '\n')

file.close()
newfile.close()