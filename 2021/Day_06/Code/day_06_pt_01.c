#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define LEN 600
#define RST 6
#define NEW 8


int main(int argc, char *argv[]) {

	FILE *f;
	char input[LEN];
	int days = atoi(argv[2]);
	
	f = fopen(argv[1],"r");

	if(argv[1] == NULL) {

		puts("Inputs file path argument missing.\n"
			"\tExample usage:\n"
			"\t\tday_06_part /file/path/to/inputs number-of-days-as-integer\n");

	}

	fgets(input,LEN,f);
	
	char *cursor = input;
	int *fish_lifespan = calloc(NEW + 1,sizeof(int));

	while(cursor != input + strlen(input)) {

		int current_fish = (int)strtol(cursor,&cursor,10);

		if(*cursor == ',') {

			cursor++;
		
		}

		fish_lifespan[current_fish]++;

		if(*cursor == '\n') {

			break;

		}

	}

	int day_count = 0;

	while(day_count < days) {

		int *next_lifespan = malloc((NEW + 1) * sizeof(int));
		int *temp = NULL;
		int reproducing_fish = 0;
		int spawned_fish = 0;
		
		for(int i = 0; i < NEW + 1; i++) {

			if(i == 0) {

				spawned_fish = fish_lifespan[i];
				reproducing_fish = fish_lifespan[i];

			}
			else {

				next_lifespan[i - 1] = fish_lifespan[i];
			
			}

		}

		next_lifespan[RST] = next_lifespan[RST] + reproducing_fish;
		next_lifespan[NEW] = spawned_fish;

		temp = fish_lifespan;
		fish_lifespan = next_lifespan;
		free(temp);
		
		day_count++;

	}

	int total_fish = 0;

	for(int i = 0; i < NEW + 1; i++) {

		total_fish = total_fish + fish_lifespan[i];

	}

	printf("Total lanternfish: %i\n",total_fish);


	return 0;

}
	
