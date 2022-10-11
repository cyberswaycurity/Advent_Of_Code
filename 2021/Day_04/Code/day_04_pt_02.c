#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

#define GRID_SIZE 5
#define DRAWS 2000

int main(int argc, char *argv[]) {

	FILE *f;
	char line_input[DRAWS] = {};
	char delimiter;
	int num_index = 0;
	int num_count = 1;
	int arr_length = 1;
	int *numbers_list = malloc(arr_length*sizeof(int));
	int drawn_number = 0;
	

	if(argv[1] == NULL) {
		puts("Input file is missing as argument.\n"
			"\tExample:\n"
			"\t\t./day_04_pt_01 /path/to/input/file\n");

		exit(1);

	}

	f = fopen(argv[1],"r");

//***********************************************************************************************************************************
//				READ NUMBERS LIST
//***********************************************************************************************************************************

	fgets(line_input,DRAWS,f);

	char *cursor = line_input;

	while (cursor != line_input + strlen(line_input)) {

		if(num_count >= arr_length) {

			arr_length = 2 * arr_length;
			numbers_list = realloc(numbers_list,arr_length*sizeof(int));

		}

		numbers_list[num_index] = (int)strtol(cursor,&cursor,10);

		if(*cursor == ',') {
		
			cursor++;

		}

		if(*cursor == '\n') {

			break;
		}

		num_count++;
		num_index++;
		
	}

//***********************************************************************************************************************************
//				READ BINGO CARDS
//***********************************************************************************************************************************

	arr_length = 1;
	int bingo_cards_index = 0;
	int ***bingo_cards_rows = malloc(arr_length * sizeof(int**));
	int rows_arr_index = 0;

	fgets(line_input,DRAWS,f);

	bingo_cards_rows[bingo_cards_index] = malloc(GRID_SIZE * sizeof(int*));


	while(fgets(line_input,DRAWS,f)) {
		

		if(line_input[0] == '\n') {

			bingo_cards_index++;

			rows_arr_index = 0;

			if((bingo_cards_index + 1) >= arr_length) {

				arr_length = 2 * arr_length;

				bingo_cards_rows = realloc(bingo_cards_rows,arr_length * sizeof(int**));
				
			}

			
			bingo_cards_rows[bingo_cards_index] = malloc(GRID_SIZE * sizeof(int*));

			continue;

		}

		cursor = line_input;

		bingo_cards_rows[bingo_cards_index][rows_arr_index] = malloc(GRID_SIZE * sizeof(int));

		int col_arr_index = 0;

		while(cursor != line_input + strlen(line_input)) {

			if(*cursor == '\n') {

				break;

			}


			bingo_cards_rows[bingo_cards_index][rows_arr_index][col_arr_index] = (int)strtol(cursor,&cursor,10);

			col_arr_index++;
		}
			

		rows_arr_index++;
	}


	fclose(f);


//***********************************************************************************************************************************
//				CREATE 2D ARRAYS TO TRACK DRAWN NUMBERS
//***********************************************************************************************************************************

	int bingo_cards_rows_win_check[bingo_cards_index + 1][GRID_SIZE];
	memset(bingo_cards_rows_win_check,0,(bingo_cards_index + 1) * GRID_SIZE * sizeof(int));

	int bingo_cards_cols_win_check[bingo_cards_index + 1][GRID_SIZE];
	memset(bingo_cards_cols_win_check,0,(bingo_cards_index + 1) * GRID_SIZE * sizeof(int));

	char bingo_cards_num_tracker[bingo_cards_index + 1][GRID_SIZE][GRID_SIZE];
	memset(bingo_cards_num_tracker,'-',(bingo_cards_index + 1) * GRID_SIZE * GRID_SIZE * sizeof(char));


//***********************************************************************************************************************************
//				COMMENCE DRAWING NUMBERS
//***********************************************************************************************************************************

	int winning_board = 0;
	bool *board_winner_check = calloc((bingo_cards_index + 1), sizeof(bool));
	int *board_winner_num = calloc((bingo_cards_index + 1), sizeof(int));

	for(int i = 0; i < num_count; i++) {

		drawn_number = numbers_list[i];

		for(int j = 0; j < bingo_cards_index + 1; j++) {

			if(board_winner_check[j] == true) {

				continue;

			}

			for(int k = 0; k < GRID_SIZE; k++) {

				for(int l = 0; l < GRID_SIZE; l++) {

					if(bingo_cards_rows[j][k][l] == drawn_number) {

						bingo_cards_num_tracker[j][k][l] = 'X';
						bingo_cards_rows_win_check[j][k]++;
						bingo_cards_cols_win_check[j][l]++;

						if((bingo_cards_rows_win_check[j][k] == 5 ) || (bingo_cards_cols_win_check[j][l] == 5)) {

							winning_board = j;

							board_winner_check[j] = true;
							board_winner_num[j] = drawn_number;

						}

					}
				}

			}

		}

	}

	printf("Winning board: %i\nWinning number: %i\n",winning_board,board_winner_num[winning_board]);

	free(numbers_list);
	free(board_winner_check);


//***********************************************************************************************************************************
//				SUM WINNING BOARD NUMBERS
//***********************************************************************************************************************************

	int winning_sum = 0;

	for(int i = 0; i < GRID_SIZE; i++) {

		for(int j = 0; j < GRID_SIZE; j++) {
		
			if(bingo_cards_num_tracker[winning_board][i][j] == '-') {

				winning_sum = winning_sum + bingo_cards_rows[winning_board][i][j];

			}
		}

	}

	free(bingo_cards_rows);

	printf("Winning sum: %i\n",winning_sum);

//***********************************************************************************************************************************
//				PUZZLE ANSWER
//***********************************************************************************************************************************

	printf("Puzzle answer: %i\n",winning_sum*board_winner_num[winning_board]);

	free(board_winner_num);

	return 0;

}
