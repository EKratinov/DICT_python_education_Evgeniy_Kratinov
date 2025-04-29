import random


def generate_domino_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def distribute_pieces(domino_set):
    random.shuffle(domino_set)
    return {
        "stock": domino_set[:14],
        "player": domino_set[14:21],
        "computer": domino_set[21:29]
    }


def determine_start_piece(player_pieces, computer_pieces):
    max_double, starter = None, None

    for piece in player_pieces[:]:
        if piece[0] == piece[1]:
            if max_double is None or piece[0] > max_double[0]:
                max_double, starter = piece, "player"
                player_pieces.remove(piece)

    for piece in computer_pieces[:]:
        if piece[0] == piece[1]:
            if max_double is None or piece[0] > max_double[0]:
                max_double, starter = piece, "computer"
                computer_pieces.remove(piece)

    return max_double, starter if max_double else (None, None)


def display_game(state):
    print("=" * 70)
    print(f"Stock size: {len(state['stock'])}")
    print(f"Computer pieces: {len(state['computer'])}\n")

    snake = state["snake"]
    print(f"Domino snake: {snake if len(snake) <= 6 else f'{snake[:3]} ... {snake[-3:]}' }")

    print("\nYour pieces:")
    for idx, piece in enumerate(state["player"], 1):
        print(f"{idx}: {piece}")

    status_msg = "Computer is about to make a move. Press Enter to continue ..." if state["turn"] == "computer" else "It's your turn to make a move. Enter your command."
    print(f"\nStatus: {status_msg}")


def check_game_end(state):
    if not state["player"]:
        return "Status: The game is over. You won!"
    if not state["computer"]:
        return "Status: The game is over. The computer won!"

    first, last = state["snake"][0][0], state["snake"][-1][1]
    if sum(piece.count(first) for piece in state["snake"]) == 8 or sum(piece.count(last) for piece in state["snake"]) == 8:
        return "Status: The game is over. It's a draw!"

    return None


def is_valid_move(piece, snake, move):
    left_match, right_match = snake[0][0], snake[-1][1]

    if (move < 0 and piece[1] == left_match) or (move > 0 and piece[0] == right_match):
        return True
    return False


def rotate_piece(piece):
    return [piece[1], piece[0]]

def place_piece(piece, snake, move):
    left_match, right_match = snake[0][0], snake[-1][1]

    if move < 0 and piece[1] != left_match:
        piece = rotate_piece(piece)
    elif move > 0 and piece[0] != right_match:
        piece = rotate_piece(piece)

    snake.insert(0, piece) if move < 0 else snake.append(piece)

def evaluate_piece_values(snake, pieces):
    counts = {i: 0 for i in range(7)}
    for piece in snake + pieces:
        counts[piece[0]] += 1
        counts[piece[1]] += 1

    return {tuple(piece): counts[piece[0]] + counts[piece[1]] for piece in pieces}


def get_best_computer_move(computer_pieces, snake):
    values = evaluate_piece_values(snake, computer_pieces)
    sorted_pieces = sorted(computer_pieces, key=lambda x: values[tuple(x)], reverse=True)

    for piece in sorted_pieces:
        if is_valid_move(piece, snake, 1):
            return computer_pieces.index(piece) + 1
        elif is_valid_move(rotate_piece(piece), snake, 1):
            return computer_pieces.index(piece) + 1

    return 0


def get_player_move(player_pieces, snake):
    while True:
        try:
            move = int(input("\nEnter your move: "))
            if move == 0:
                if game_state["stock"]:
                    game_state["player"].append(game_state["stock"].pop())
                    print("\n You took a piece from the reserve.")
                    return 0
                else:
                    print("\n The reserve is empty.")
                    continue

            if abs(move) > len(player_pieces):
                print("Invalid input. Please try again.")
                continue

            piece = player_pieces[abs(move) - 1]
            if is_valid_move(piece, snake, move) or is_valid_move(rotate_piece(piece), snake, move):
                return move

            print("Illegal move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")
while True:
    domino_set = generate_domino_set()
    game_state = distribute_pieces(domino_set)
    start_piece, first_player = determine_start_piece(game_state["player"], game_state["computer"])

    if start_piece:
        break

game_state["snake"] = [start_piece]
game_state["turn"] = first_player

while True:
    display_game(game_state)
    result = check_game_end(game_state)
    if result:
        print(result)
        break

    if game_state["turn"] == "player":
        move = get_player_move(game_state["player"], game_state["snake"])
        if move != 0:
            piece = game_state["player"].pop(abs(move) - 1)
            place_piece(piece, game_state["snake"], move)

        game_state["turn"] = "computer"
    else:
        move = get_best_computer_move(game_state["computer"], game_state["snake"])
        if move == 0 and game_state["stock"]:
            game_state["computer"].append(game_state["stock"].pop())
        else:
            piece = game_state["computer"].pop(abs(move) - 1)
            place_piece(piece, game_state["snake"], move)

        game_state["turn"] = "player"
