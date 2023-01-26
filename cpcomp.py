import sys
import os
import argparse
import cursed_cpp


template_part1 = """
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <tuple>
#include <limits>

using namespace std;

typedef long long int ll;
typedef long double ld;
typedef double db;


#define loop(a) for (ll __temp_looping_var = 0; __temp_looping_var < a; __temp_looping_var++)
#define repi(a, b) for(ll i = a; i < b; i++)
#define repk(a, b) for(ll k = a; k < b; k++)
#define repj(a, b) for(ll j = a; j < b; j++)


#define nwline \n




"""


template_part2 = """
int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	solve();

	cout << flush;

	return 0;
}
"""



parser = argparse.ArgumentParser()


parser.add_argument('input_file', help = 'The name of the input file')


parser.add_argument('-c', '--compile', action='store_true', help = 'use this if the output file should be compiled with g++ afterwards')
parser.add_argument('-ccpp', '--cursed_cpp', action = 'store_true', help = 'use this if the input file is a "Cursed C++" file')

args = parser.parse_args()


with open(args.input_file, 'r') as f:
	with open(f'cpcomp_{args.input_file}', 'w') as f2:

		if args.cursed_cpp:
			f2.write( template_part1 + cursed_cpp.uncurse( f.read() ) + template_part2 )
		else:
			f2.write( template_part1 + f.read() + template_part2 )


if args.compile:
	tmp = args.input_file.split('.')[0]
	os.system(f'g++ cpcomp_{args.input_file} -o cpcomp_{tmp}')