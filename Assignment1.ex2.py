service = input('Enter desired auto service:\n')

if service == 'Oil change':
	print('Oil change')
	print('Cost of oil change: $35')
elif service == 'Tire rotation':
	print('Tire rotation')
	print('Cost of tire rotation: $19')
elif service == 'Car wash':
	print('Car wash')
	print('Cost of car wash: $7')
else:
	print("Sorry, I don't know that one")
