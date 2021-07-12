num = input(':')

for a in num:
	if a == '.':
		decimal = True
		continue

	if decimal:
		cont += 1

print(cont)


