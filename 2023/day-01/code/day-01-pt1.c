#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_CHAR 50

int main(int argc,char *argv[]){

	FILE *f = NULL;
	char line[MAX_CHAR];
	int calibration_sum_value = 0;
	
	if(argv[1] == NULL) {

		puts("Input file is missing as argument."
				"\tExample:\n"
				"\t\t./day-01-pt1-solution /path/to/input/file\n");
		exit(1);

	}

	f = fopen(argv[1],"r");

	if(f == NULL) {

		puts("File failed to open.\n");
		exit(1);

	}

	while(fscanf(f,"%s",line) == 1) {

		int size = strlen(line);
		int first_number;
		int second_number;

		for(int i = 0; i < size;i++) {

			char c = line[i];

			if(c >= '0' && c <= '9') {

				first_number = (c - '0') * 10;
				break;

			}

		}

		for(int i = size - 1; i > -1; i--) {

			char c = line[i];

			if(c >= '0' && c <= '9') {

				second_number = (c - '0');
				break;

			}

		}

		calibration_sum_value = calibration_sum_value + first_number + second_number;

	}

	printf("%d",calibration_sum_value);

}
