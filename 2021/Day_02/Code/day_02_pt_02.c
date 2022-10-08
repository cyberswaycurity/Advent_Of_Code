#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_CHAR 30

int main(int argc, char *argv[]) {

	FILE *f;
	char direction[MAX_CHAR] = {};
	int value = 0;
	int horizontal = 0;
	int depth = 0;
	int aim = 0;
	int solution = 0;

        if(argv[1] == NULL) {
                puts("Input file is missing as argument.\n"
                        "\tExample:\n"
                        "\t\t./day_02_pt_02_solution /path/to/input/file\n");
                exit(1);
        }

	f = fopen(argv[1],"r");

	if (f == NULL) {
		puts("File failed to open. Exiting program");
		exit(1);
	}

	while(fscanf(f,"%s %i",direction, &value) != EOF) {
		
		if(!strcmp(direction,"forward")) {

			horizontal += value;
			depth += (aim * value);

		}
		else if(!strcmp(direction,"down")) {

			aim += value;

		}
		else {

			aim -= value;

		}		

	}

	solution = horizontal * depth;

	printf("Answer is %d\n",solution);	

	return 0;
}

	
