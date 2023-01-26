import os
import platform
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('executable', type=str, help = 'the filename of the executable which will be executed')
args = parser.parse_args()


input_stream = ''


while True:
	inp = input()

	if inp == 'stfu':
		break
	else:
		input_stream += inp + '\n'



with open('__input_stream.txt', 'w') as f:
	f.write(input_stream)


print('-'*os.get_terminal_size()[0])


if platform.system() == 'Windows':

	os.system(args.executable + ' < __input_stream.txt')
else:

	os.system('__input_stream.txt | ' + args.executable)


os.remove('__input_stream.txt')