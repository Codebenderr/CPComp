/*
// This exists so that 'cpcomp.py' can be run without typing 'python cpcomp.py' all the time
*/

#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {

	char final[256] = "python cpcomp.py ";
	int n = 17;

	for (int i = 1; i < argc; i++)
	{
		strcpy(final+n, argv[i]);
		n += strlen(argv[i]);
		final[n] = ' ';
		n += 1;
	}

	final[n-1] = '\0';
	system(final);

	return 0;
}