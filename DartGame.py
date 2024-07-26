"""
'THE DARTS GAME SIMULATOR' PROMPTS USER TO PICK 1 OR 0.
ONCE USER INPUTS "1", PROGRAM SIMULATES USING RANDOMLY GENERATED THROWS
AND SUBTRACT EACH DISTANCE OF DART FROM THE CENTRE OF TARGET UNTIL
501 BECOMES 0 OR BELOW 0. IT RETURNS THE AMOUNT OF THROWS TO ACHIEVE THIS.
ONCE USER INPUTS "0", THE PROGRAM PRINTS OUT THE RESULT AND HALTS. 

AUTHOR: JAE KIM
"""
import random
import math

def main():
    username = "jkim"
    number_of_player1_wins = 0
    number_of_player2_wins = 0
    number_of_draws = 0
    print_banner(username)
    print()
    print_menu()
    user_choice = get_user_input()
    while user_choice == 1:
        print()
        print_separator()
        result_player1 = get_num_throws_to_reach_501()
        print_player_throws("Player 1", result_player1)
        result_player2 = get_num_throws_to_reach_501()
        print_player_throws("Player 2", result_player2)
        if result_player1 < result_player2:
            print("Player 1 wins.")
            number_of_player1_wins += 1 
        elif result_player1 > result_player2:
            print("Player 2 wins.")
            number_of_player2_wins += 1
        else:
            print("This is a draw.")
            number_of_draws += 1
        print()
        print_separator()
        print_menu()
        user_choice = get_user_input()
    print()
    print_separator()    
    print_stats(number_of_player1_wins, number_of_player2_wins,number_of_draws)
    print_separator()
    

def print_separator():
    print("-" * 37)

def print_banner(user_name):
    message = "Darts game simulator 1.0 by " + user_name
    dart = "-" * len(message)
    print(dart)
    print(message)
    print(dart)

def print_menu():
    print("Please select an option:") 
    print("Enter 1 to play a darts game.")
    print("Enter 0 to exit.")

def get_user_input():
    prompt = input("Please enter your choice: ")
    while not(int(prompt) == 0 or int(prompt) == 1):
        prompt = input("Error. Please enter a valid choice: ")
    if prompt == "0" or prompt == "1":
        return int(prompt)

def get_coordinate(lower_bound, upper_bound):
    random_float = round(random.uniform(lower_bound, upper_bound), 2)
    return random_float

def get_dart_throw(min_dart_board, max_dart_board):
    coordinate1 = get_coordinate(min_dart_board, max_dart_board)
    coordinate2 = get_coordinate(min_dart_board, max_dart_board)
    str_coordinates = str(coordinate1) + " " + str(coordinate2)
    return str_coordinates

def get_distance_to_centre(string_coordinates):
    space_pos = string_coordinates.find(" ")
    front_num = float(string_coordinates[:space_pos])
    second_num = float(string_coordinates[space_pos+1:])
    distance_centre = round(math.sqrt((front_num**2) + (second_num**2)), 2)
    return distance_centre

def is_bullseye(distance_to_centre):
    if distance_to_centre <= 1:
        return True
    else:
        return False

def is_50(distance_to_centre):
    if distance_to_centre >= 1 and distance_to_centre <= 2:
        return True
    else:
        return False

def is_20(distance_to_centre):
    if distance_to_centre > 2 and distance_to_centre <= 3:
        return True
    else:
        return False

def is_10(distance_to_centre):
    if distance_to_centre > 3 and distance_to_centre <= 4:
        return True
    else:
        return False

def is_out(distance_to_centre):
    if distance_to_centre > 4:
        return True
    else:
        return False

def get_score_throw(distance_to_centre):
    bullseye = is_bullseye(distance_to_centre)
    if bullseye:
        return int(100)
    fifty = is_50(distance_to_centre)
    if fifty:
        return int(50)
    twenty = is_20(distance_to_centre)
    if twenty:
        return int(20)
    ten = is_10(distance_to_centre)
    if ten:
        return int(10)
    is_out(distance_to_centre)
    if is_out:
        return int(0)

def get_num_throws_to_reach_501():
    point = float(501)
    num_throw = 0
    while not(point == 0 or point < 0):
        random_dart = get_dart_throw(-5, 5)
        str_distance = get_distance_to_centre(random_dart)
        score = get_score_throw(str_distance)
        point = point - score
        num_throw += 1
    return num_throw

def print_player_throws(name_player, number_of_throws):
    print(name_player + " reached 501 with " + str(number_of_throws) + " throws.")

def print_stats(num_player1_wins, num_player2_wins, num_draws):
    print("Player 1 won " + str(num_player1_wins) + " time(s).")
    print("Player 2 won " + str(num_player2_wins) + " time(s).")
    print("There was/were " + str(num_draws) + " draw game(s).")

    
main()
