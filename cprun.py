import sys
import os
import platform

args = sys.argv[1:]



if len(args) == 1:

	input_stream = ''

	while True:
		inp = input()

		if inp == 'stfu':
			break
		else:
			input_stream += '\n' + inp


	with open('__input_stream.txt', 'w') as f:
		f.write(input_stream)

	print('\r' + '-'*os.get_terminal_size()[0])

	if platform.system() == 'Windows':
		os.system('__input_stream.txt > ' + args[0])

	elif platform.system() in ('Darwin', 'Linux'):
		os.system('__input_stream.txt | ' + args[0])


	os.remove('__input_stream.txt')

else:

	print('\u001b[31m' + '\n[!] Invalid number of arguments [!]' + '\u001b[0m')