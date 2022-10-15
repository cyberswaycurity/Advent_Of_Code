#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

#define MAX_CHAR 10000

typedef struct stacknode {

	int value;
	struct stacknode *next;

} stacknode;

typedef stacknode* stack;

void push(stack* s, int* value) {

	stacknode* node = malloc(sizeof(stacknode));

	if(node == NULL) {

		puts("Not enough memory for push.\n");
		exit(1);

	}


	node->value = *value;
	node->next = *s;
	*s = node;

	return;

}

void pop(stack* s, int* value) {

	if(s == NULL) {

		puts("Stack is empty.\n");
		return;
	
	}

	*value = (*s)->value;
	stack temp = NULL;
	temp = (*s);
	*s = (*s)->next;
	free(temp);

	return;

}
	
int absolute(int a,int b) {

	if((a - b) < 0) {

		return (b - a);

	}

	return (a - b);

}

int main(int argc, char *argv[]) {

	FILE *f;
	char c;

	if(argv[1] == NULL) {

		puts("File path argument is missing.\n"
			"\tExample:\n"
			"\t\t./day_06_pt_01 /path/to/input/file\n");

		exit(1);

	}

	f = fopen(argv[1], "r");

	char input[MAX_CHAR];
	
	fgets(input,MAX_CHAR,f);

	char *cursor = input;
	int curr_num = 0;
	int max_num = 0;

	while(cursor != cursor + strlen(input)) {

		if(*cursor == ',') {

			cursor++;

		}
		
		if(*cursor == '\n') {

			break;

		}

		curr_num = strtol(cursor,&cursor,10);

		if(curr_num > max_num) {

			max_num = curr_num;

		}

	}

	int *positions = calloc(max_num + 1,sizeof(int));
	int *crab_posit_count = calloc(max_num + 1,sizeof(int));
	int *fuel_posit_cost = calloc(max_num + 1,sizeof(int));

	cursor = input;

	int curr_posit;

	while(cursor != cursor + strlen(input)) {

		if(*cursor == ',') {
	
			cursor++;

		}

		if(*cursor == '\n') {

			break;

		}

		curr_posit = (int) strtol(cursor,&cursor,10);

		if(positions[curr_posit] == 0) {

			positions[curr_posit] = 1;

		}

		crab_posit_count[curr_posit]++;

	}

	for(int i = 0; i < max_num + 1; i++) {

		int fuel_cost = 0;

		if(positions[i] == 0) {

			continue;

		}

		for(int j = 0; j < max_num + 1; j++) {

			if(positions[j] == 0) {

				continue;

			}

			int posit_cost = absolute(j,i);

			fuel_cost = fuel_cost + (posit_cost * crab_posit_count[j]);

		}

		fuel_posit_cost[i] = fuel_cost;

	}

	stack fuel_stack = NULL;
	stack posit_stack = NULL;

	for(int i = 0; i < max_num + 1; i++) {

		if(positions[i] == 0) {

			continue;

		}

		push(&posit_stack, &i);
		push(&fuel_stack, &fuel_posit_cost[i]);
	}

	
	int min_fuel;
	int min_posit;

	pop(&fuel_stack, &min_fuel);
	pop(&posit_stack, &min_posit);

	while(fuel_stack != NULL) {

		int curr_fuel;
		int curr_posit;

		pop(&fuel_stack, &curr_fuel);
		pop(&posit_stack, &curr_posit);

		if(curr_fuel < min_fuel) {

			min_fuel = curr_fuel;
			min_posit = curr_posit;

		}

	}

	puts("Answer:");
	printf("Lowest fuel: %d, Crab position: %d\n",min_fuel,min_posit);

	return 0;

}
