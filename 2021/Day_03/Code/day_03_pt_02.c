#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_BITS 20

int main(int argc, char *argv[]) {
	
	FILE *f;
	int index = 0;
	int matrix_rows = 1;
	int file_rows = 1;
	char **matrix = malloc(sizeof(char*)*matrix_rows);
	char bit_string[MAX_BITS] = {};
	int total_bits;
	
        if(argv[1] == NULL) {
                puts("Input file is missing as argument.\n"
                        "\tExample:\n"
                        "\t\t./day_03_pt_02_solution /path/to/input/file\n");
                exit(1);
        }	
	
        f = fopen(argv[1],"r");

        if (f == NULL) {
                puts("File failed to open. Exiting program");
                exit(1);
        }

	fgets(bit_string,MAX_BITS,f);

	total_bits = strlen(bit_string) - 1;

	matrix[index] = malloc(total_bits*sizeof(char));

	for(int i = 0; i < total_bits; i++) {
		
		matrix[index][i] = bit_string[i];

	}

	while(fgets(bit_string,MAX_BITS,f)) {

		index++;
		file_rows++;
	
		if(matrix_rows < file_rows) {

			matrix_rows = matrix_rows * 2;

			matrix = realloc(matrix,matrix_rows*sizeof(char*));

		}

		matrix[index] = malloc(total_bits*sizeof(char));

		for(int i = 0; i < total_bits; i++) {
			
			matrix[index][i] = bit_string[i];

		}
	}

	fclose(f);

	int generator_rows = file_rows;
	char **generator = malloc(file_rows*sizeof(char*));
	memcpy(generator,matrix,sizeof(char*)*file_rows);

	free(matrix);

	int scrubber_rows = file_rows;
	char **scrubber = malloc(file_rows*sizeof(char*));
	memcpy(scrubber,generator,sizeof(char*)*file_rows);

// *********************************************************************
//                GENERATOR RATING CALCULATION PART
// *********************************************************************

	for(int i = 0; i < total_bits; i++) {
		
		char **generator_final = NULL;
		int zero_count = 0;
		int one_count = 0;
		char common_bit = '1';
		int generator_final_rows = 0;

		for(int j = 0; j < generator_rows; j++) {

			if(generator[j][i] == '0') {

				zero_count++;

			}
			else {

				one_count++;

			}

		

		}

		if(zero_count > one_count) {

			common_bit = '0';
			generator_final_rows = zero_count;

		}
		else {

			common_bit = '1';
			generator_final_rows = one_count;

		}

		generator_final = malloc(generator_final_rows*sizeof(char*));

		int gen_final_index = 0;


		for (int j = 0; j < generator_rows; j++) {

			if(generator[j][i] == common_bit) {

				generator_final[gen_final_index] = malloc(total_bits*sizeof(char));
				generator_final[gen_final_index] = generator[j];
				gen_final_index++;
			}

			if(gen_final_index == generator_final_rows) {

				break;

			}

		}

		generator_rows = generator_final_rows;
		generator = generator_final;
		generator_final = NULL;
		free(generator_final);

				
		if(generator_rows == 1) {

			break;

		}
		
	}

	int generator_rating = 0;

	if(generator[0][0] == '1') {

		generator_rating = generator_rating ^ 1;

	}

	for(int i = 1; i < total_bits; i++) {

		generator_rating = generator_rating << 1;

		if(generator[0][i] == '1') {

			generator_rating = generator_rating ^ 1;

		}


	}

	free(generator);

// *********************************************************************
//                      SCRUBBER RATING CALCULATION
// *********************************************************************

	for(int i = 0; i < total_bits; i++) {
		
		char **scrubber_final = NULL;
		int zero_count = 0;
		int one_count = 0;
		char common_bit = '1';
		int scrubber_final_rows = 0;

		for(int j = 0; j < scrubber_rows; j++) {

			if(scrubber[j][i] == '0') {

				zero_count++;

			}
			else {

				one_count++;

			}

		

		}

		if(zero_count > one_count) {

			common_bit = '1';
			scrubber_final_rows = one_count;

		}
		else {

			common_bit = '0';
			scrubber_final_rows = zero_count;

		}

		scrubber_final = malloc(scrubber_final_rows*sizeof(char*));

		int scrub_final_index = 0;

		for (int j = 0; j < scrubber_rows; j++) {

			if(scrubber[j][i] == common_bit) {

				scrubber_final[scrub_final_index] = malloc(total_bits*sizeof(char));
				scrubber_final[scrub_final_index] = scrubber[j];
				scrub_final_index++;
			}

			if(scrub_final_index == scrubber_final_rows) {

				break;

			}

		}

		scrubber_rows = scrubber_final_rows;
		scrubber = scrubber_final;
		scrubber_final = NULL;
		free(scrubber_final);

		if(scrubber_rows == 1) {

			break;

		}
		
	}

	int scrubber_rating = 0;

	if(scrubber[0][0] == '1') {

		scrubber_rating = scrubber_rating ^ 1;

	}

	for(int i = 1; i < total_bits; i++) {

		scrubber_rating = scrubber_rating << 1;

		if(scrubber[0][i] == '1') {

			scrubber_rating = scrubber_rating ^ 1;

		}


	}

	free(scrubber);

// *********************************************************************
//                      SCRUBBER RATING CALCULATION
// *********************************************************************

	printf("Generator rating: %i\n",generator_rating);
	printf("Scrubber rating: %i\n",scrubber_rating);
	printf("Life support rating: %i\n",generator_rating*scrubber_rating);

	return 0;
}
