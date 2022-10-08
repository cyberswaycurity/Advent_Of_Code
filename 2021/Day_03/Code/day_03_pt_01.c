#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_BITS 20

int main(int argc, char *argv[]) {
	
	FILE *f;
	char bit_string[MAX_BITS] = {};
	int total_bits;
	int zero_count[MAX_BITS] = {0};
	int one_count[MAX_BITS] = {0};

        if(argv[1] == NULL) {
                puts("Input file is missing as argument.\n"
                        "\tExample:\n"
                        "\t\t./day_03_pt_01_solution /path/to/input/file\n");
                exit(1);
        }	
	
        f = fopen(argv[1],"r");

        if (f == NULL) {
                puts("File failed to open. Exiting program");
                exit(1);
        }

	fgets(bit_string,MAX_BITS,f);

	total_bits = strlen(bit_string) - 1;

	for(int i = 0; i < total_bits; i++) {
		
		if(bit_string[i] == '0') {
			zero_count[i]++;
		}
		else {
			one_count[i]++;
		}
	}

	while(fgets(bit_string,MAX_BITS,f)) {

	
		for(int i = 0; i < total_bits; i++) {
			
			if(bit_string[i] == '0') {
				zero_count[i]++;
			}
			else {
				one_count[i]++;
			}
		}
	}

	fclose(f);

	int gamma = 0;
	int epsilon = 0;

	if(zero_count[0] < one_count[0]) {

		gamma = gamma ^ 1;

	}
	else{

		epsilon = epsilon ^ 1;

	}
	
	for(int i = 1; i < total_bits; i++) {

		gamma = gamma << 1;
		epsilon = epsilon << 1;

		if (zero_count[i] < one_count[i]) {
			
			gamma = gamma ^ 1;

		}
		else {

			epsilon = epsilon ^ 1;

		}

	}

	printf("Gamma: %i\nEpsilon: %i\n",gamma,epsilon);

	printf("Power consumption: %i\n",gamma*epsilon);
	
	return 0;
}
