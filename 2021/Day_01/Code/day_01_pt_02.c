#include<stdio.h>
#include<stdlib.h>
#define MAX_CHAR 10

int main(int argc, char *argv[]) {
	FILE *f = NULL;
	int line_count = 0;
	char line[MAX_CHAR] = {};
	int* depths = NULL;
	int arr_length = 10;
	int* all_windows = NULL;
	int window_count = 0;

        if(argv[1] == NULL) {
                puts("Input file is missing as argument.\n"
                        "\tExample:\n"
                        "\t\t./day_01_pt_02_solution /path/to/input/file\n");
                exit(1);
        }

	f = fopen(argv[1],"r");

	if(f == NULL) {
		puts("File failed to open");
		exit(1);
	}

	fgets(line,MAX_CHAR,f);

	line_count++;

	depths = malloc(arr_length*sizeof(int));
	depths[line_count - 1] = atoi(line);

	while(fgets(line,MAX_CHAR,f)) {

		line_count++;

		if(arr_length <= line_count) {

			arr_length = arr_length * 2;
			depths = realloc(depths,arr_length*sizeof(int));

		}

		depths[line_count - 1] = atoi(line);

	}

	fclose(f);

	all_windows = malloc(line_count*sizeof(int));

	for(int i = 0; i < (line_count - 2); i++) {

		int window = 0;
		
		for(int j = 0; j < 3; j++) {

			window = window + depths[i+j];

		}

		all_windows[i] = window;
	}
	
	int prev_window = all_windows[0];

	int curr_window = 0;

	for(int i = 1; i < (line_count - 2); i++) {

		curr_window = all_windows[i];

		if(curr_window > prev_window) {

			window_count++;
		}

		prev_window = curr_window;

	}

	free(all_windows);
	free(depths);

	printf("Answer is %d.\n",window_count);
		
	return 0;
}
