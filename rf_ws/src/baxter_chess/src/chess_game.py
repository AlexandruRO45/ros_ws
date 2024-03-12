import os
import random

class ChessGame:
    def __init__(self):
        """Initialize the chess game by attempting to read from 'chess_game.txt'."""
        # Default empty state
        default_state = [
            ['r', '*', '*', '*', '*', '*', '*', 'r'],
            ['*', '*', '*', '*', '*', '*', '*', '*'],
            ['k', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', 'K'],
            ['*', '*', '*', '*', '*', '*', '*', '*'],
            ['R', '*', '*', '*', '*', '*', '*', 'R']
        ]

        # if os.path.exists('chess_game.txt'):
        #     try:
        #         with open('chess_game.txt', 'r') as file:
        #             self.game_state = [line.strip().split(' ') for line in file if line.strip()]
        #     except Exception as e:
        #         print("Failed to load game from 'chess_game.txt', initializing to default state. Error: {}".format(e))
        #         self.game_state = default_state
        # else:
        self.game_state = default_state
        # Optionally, create the file with the default state
        self.save_state_to_file('chess_game.txt')


    def update_state(self, from_pos, to_pos):
        """Update the state of the game by moving a piece from 'from_pos' to 'to_pos'."""
        # Convert 'from_pos' and 'to_pos' from 'ij' format to row and column indices
        from_row, from_col = int(from_pos[0]), int(from_pos[1])
        to_row, to_col = int(to_pos[0]), int(to_pos[1])

        # Check if the 'from' position and 'to' position are within the board limits
        if 0 <= from_row < len(self.game_state) and 0 <= from_col < len(self.game_state[0]) and 0 <= to_row < len(self.game_state) and 0 <= to_col < len(self.game_state[0]):
            piece = self.game_state[from_row][from_col]
            self.game_state[from_row][from_col] = '*'  # Remove the piece from its original location
            self.game_state[to_row][to_col] = piece    # Place the piece at the new location
        else:
            print("Error: Invalid board positions.")


    def print_game_state(self):
        """Print the current state of the chess board."""
        print("    0   1   2   3   4   5   6   7")
        print("  +---+---+---+---+---+---+---+---+")
        for i, row in enumerate(self.game_state):
            row_str = "{} | ".format(i) + " | ".join(row) + " |"
            print(row_str)
            print("  +---+---+---+---+---+---+---+---+")

    def save_state_to_file(self, file_name='chess_game.txt'):
        """Save the current game state to a text file."""
        with open(file_name, 'w') as file:
            for row in self.game_state:
                file.write(' '.join(row) + '\n')

    def load_state_from_file(self, file_name='chess_game.txt'):
        """Load the game state from a text file."""
        new_state = []
        with open(file_name, 'r') as file:
            for line in file:
                new_state.append(line.strip().split(' '))
        self.game_state = new_state


    def find_all_valid_moves(self, i, j):
        """Find all valid moves for a piece located at (i, j)."""
        valid_moves = []
        piece = self.game_state[i][j]

        # Define movement patterns
        if piece.lower() == 'k':  # King moves
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if 0 <= i + di < 8 and 0 <= j + dj < 8:
                        valid_moves.append((i + di, j + dj))

        elif piece.lower() == 'r':  # Rook moves
            # Horizontal moves
            for dj in range(-7, 8):
                if 0 <= j + dj < 8:
                    valid_moves.append((i, j + dj))
            # Vertical moves
            for di in range(-7, 8):
                if 0 <= i + di < 8:
                    valid_moves.append((i + di, j))

        # Filter out invalid moves (including those that don't change position and those blocked by other pieces)
        filtered_moves = []
        for new_i, new_j in valid_moves:
            if (new_i != i or new_j != j) and (piece.lower() == 'k' or self.is_path_clear(i, j, new_i, new_j)):
                filtered_moves.append((new_i, new_j))
        
        return filtered_moves

    def is_path_clear(self, i, j, new_i, new_j):
        """Check if the path is clear for a rook moving from (i, j) to (new_i, new_j)"""
        if i == new_i:  # Moving horizontally
            step = 1 if new_j > j else -1
            for col in range(j + step, new_j, step):
                if self.game_state[i][col] != '*':
                    return False
        elif j == new_j:  # Moving vertically
            step = 1 if new_i > i else -1
            for row in range(i + step, new_i, step):
                if self.game_state[row][j] != '*':
                    return False
        return True  # Clear path


    def generate_random_valid_move(self, team):
        """Generate a random valid move for the specified team."""
        # Determine which pieces to consider based on the team
        pieces_to_consider = ['r', 'k'] if team == 1 else ['R', 'K']
        
        # Find all pieces for the specified team
        all_pieces = [(i, j) for i in range(8) for j in range(8) if self.game_state[i][j] in pieces_to_consider]
        random.shuffle(all_pieces)  # Randomize the order of pieces to choose from

        for i, j in all_pieces:
            valid_moves = self.find_all_valid_moves(i, j)
            # Filter valid moves based on team's piece
            valid_moves = [
                    move for move in valid_moves 
                        if self.game_state[move[0]][move[1]] == '*' or 
                        (team == 1 and self.game_state[move[0]][move[1]].isupper()) or 
                        (team == 2 and self.game_state[move[0]][move[1]].islower())
                ]
            if valid_moves:
                new_i, new_j = random.choice(valid_moves)
                return (i, j, new_i, new_j)  # Return start and end positions for the move

        return None  # If no valid moves found
