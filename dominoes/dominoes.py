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


print(f"Stock pieces: {stock}")
print(f"Computer pieces: {computer_pieces}")
print(f"Player pieces: {player_pieces}")
print(f"Domino snake: [{start_piece}]")
print(f"Status: {first_player}")
