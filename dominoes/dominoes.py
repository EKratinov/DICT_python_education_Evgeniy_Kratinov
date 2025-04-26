import random


def generate_domino_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def distribute_pieces(domino_set):
    random.shuffle(domino_set)
    stock = domino_set[:14]
    player_pieces = domino_set[14:21]
    computer_pieces = domino_set[21:28]
    return stock, player_pieces, computer_pieces


def determine_start_piece(player_pieces, computer_pieces):
    max_double = None
    starter = None

    for piece in player_pieces + computer_pieces:
        if piece[0] == piece[1]:
            if max_double is None or piece[0] > max_double[0]:
                max_double = piece
                starter = "player" if piece in player_pieces else "computer"

    if max_double is None:
        return None, None

    return max_double, starter


while True:
    domino_set = generate_domino_set()
    stock, player_pieces, computer_pieces = distribute_pieces(domino_set)
    start_piece, first_player = determine_start_piece(player_pieces, computer_pieces)

    if start_piece is not None:
        break


def display_game(stock, computer_pieces, player_pieces, domino_snake, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer_pieces)}\n")


    if len(domino_snake) <= 6:
        print("Domino snake:", domino_snake)
    else:
        print("Domino snake:", f"{domino_snake[:3]} ... {domino_snake[-3:]}")


    print("\nYour pieces:")
    for idx, piece in enumerate(player_pieces, 1):
        print(f"{idx}: {piece}")


    if status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue ...")
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")


display_game(stock, computer_pieces, player_pieces, [start_piece], first_player)
