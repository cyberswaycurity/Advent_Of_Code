#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_CHAR 200
#define ONE 2
#define FOUR 4
#define SEVEN 3
#define EIGHT 7
#define SEGM 10

int main(int argc, char *argv[]) {

	FILE *f;
	char input[MAX_CHAR];

	f = fopen(argv[1],"r");

	if(argv[1] == NULL) {

		puts("File imput argument missing.\n"
			"\tExample:\n"
			"\t\t./day_08_pt_01 /path/to/input/file\n");
		exit(1);

	}

	int easy_count = 0;

	while(fgets(input,MAX_CHAR,f)) {

		char one_digit[SEGM];
		char two_digit[SEGM];
		char three_digit[SEGM];
		char four_digit[SEGM];

		sscanf(input,"%*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*c %s %s %s %s",one_digit,two_digit,three_digit,four_digit);

		if( strlen(one_digit) == ONE || strlen(one_digit) == FOUR || strlen(one_digit) == SEVEN || strlen(one_digit) == EIGHT) {

			easy_count++;

		}		
		if( strlen(two_digit) == ONE || strlen(two_digit) == FOUR || strlen(two_digit) == SEVEN || strlen(two_digit) == EIGHT) {

			easy_count++;

		}		
		if( strlen(three_digit) == ONE || strlen(three_digit) == FOUR || strlen(three_digit) == SEVEN || strlen(three_digit) == EIGHT) {

			easy_count++;

		}		
		if( strlen(four_digit) == ONE || strlen(four_digit) == FOUR || strlen(four_digit) == SEVEN || strlen(four_digit) == EIGHT) {

			easy_count++;

		}		
	}

	printf("Answer: %d\n",easy_count);

	
	return 0;
}
