import random

def roll_dice():
    return random.randint(1, 6) 

def play_turn(play_name):
    turn_score = 0

    print(f"\n{play_name}'s turn:")

    while True:
        roll = roll_dice()
        print(f"You rolled a {roll}")

        if roll == 1:
            return 0
        turn_score += roll
        choice = input('Roll again? (y/n): ').lower()
        if choice != 'y':
            return turn_score

def main():
    scores = [0,0]
    current_player = 0

    while True:
        player_name = f'player {current_player + 1}'
        turn_score = play_turn(player_name)
        scores[current_player] += turn_score

        print(f'\nyou scored {turn_score} points')
        print(f'Current scores:player 1 = {scores[0]}, player 2 = {scores[1]}')

        if scores[current_player] >= 50:
            print(f'\n{player_name} wins!')
            break
        current_player = 1 if current_player == 0 else 0

if __name__ == '__main__':
    main()