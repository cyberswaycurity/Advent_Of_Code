#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_CHAR 1000

int main(int argc, char *argv[]) {

	FILE *f;
	int x1;
	int y1;
	int x2;
	int y2;
	char input[MAX_CHAR];
	int line_max_x = 0;
	int max_x = 0;
	int line_max_y = 0;
	int max_y = 0;
	int line_max = 0;
	int max_size = 1;

	if(argv[1] == NULL) {

		printf("Input file name argument is missing.\n"
			"\tExample:\n"
			"\t\t./day_05_pt_01 /path/to/input/file\n");
		exit(1);

	}

	f = fopen(argv[1],"r");

	while(fgets(input,MAX_CHAR,f)) {

		sscanf(input,"%i%*c%i %*c%*c %i%*c%i",&x1,&y1,&x2,&y2);

		if(x1 >= x2) {

			line_max_x = x1;
		
		}
		else {
	
			line_max_x = x2;

		}

		if(y1 >= y2) {

			line_max_y = y1;
		
		}
		else {
	
			line_max_y = y2;

		}


		if(line_max_y >= line_max_x) {

			line_max = line_max_y;

		}
		else {

			line_max = line_max_x;

		}


		if(line_max + 1 > max_size) {


			max_size = line_max + 1;

		}

	}

	fclose(f);

	int **vents_field = malloc(max_size * sizeof(int*));

	for(int i = 0; i < max_size; i++) {

		vents_field[i] = calloc(max_size, sizeof(int));

	}

	f = fopen(argv[1],"r");

	while(fgets(input,MAX_CHAR,f)) {

		sscanf(input,"%i%*c%i %*c%*c %i%*c%i",&x1,&y1,&x2,&y2);

		if(x1 == x2 & y1 < y2) {

			for(int i = y1; i <= y2; i++) {

				vents_field[i][x1]++;

			}

		}
		else if(x1 == x2 & y2 < y1) {

			for(int i = y2; i <= y1; i++) {

				vents_field[i][x1]++;

			}

		}
		else if(y1 == y2 & x1 < x2) {

			for(int i = x1; i <= x2; i++) {

				vents_field[y1][i]++;

			}

		}
		else if (y1 == y2 & x1 > x2) {

			for(int i = x2; i <= x1; i++) {

				vents_field[y1][i]++;

			}

		}
		else {

			continue;

		}
	

	}

	fclose(f);

	int overlap_count = 0;

	for(int i = 0; i < max_size; i++) {

		for(int j = 0; j < max_size; j++) {

			if(vents_field[i][j] >= 2) {

				overlap_count++;

			}

		}

	}

	printf("Puzzle answer: %i\n",overlap_count);

	free(vents_field);

	return 0;
}
