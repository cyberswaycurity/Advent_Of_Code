#include<stdio.h>
#include<stdlib.h>
#define MAX_LEN 10

int main(int argc, char *argv[]) {
	FILE *f;
	int prev_depth;
	int curr_depth;
	int count = 0;
	char line[MAX_LEN];
	

	if(argv[1] == NULL) {
		puts("Input file is missing as argument.\n"
			"\tExample:\n"
			"\t\t./day_01_pt_01_solution /path/to/input/file\n");
		exit(1);
	}

	f = fopen(argv[1],"r");

	if (f == NULL) {
		printf("Could not open file. Try again.");
		exit(1);
	}

	fgets(line,MAX_LEN,f);

	prev_depth = atoi(line);

	while(fgets(line,MAX_LEN,f)) {
		curr_depth = atoi(line);
		if (curr_depth > prev_depth) {
			count = count + 1;
		}
		prev_depth = curr_depth;
	}

	fclose(f);

	printf("Puzzle answer is %i\n",count);

	return 0;
}
