#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    print("Welcome to Trivia Trek! Get ready for an exciting quiz adventure.")
    print("Answer correctly to earn points and progress through rounds!")

#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    print("Choose a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    category_choice = int(input("Enter the number of your chosen category: "))
    return categories[category_choice - 1]

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    print(f"Round {round_number} | Current Score: {score}")

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    print(f"Game Over! Your final score is: {final_score}")
    exit()

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    for round_number in range(1, 6):  # Run for 5 rounds
        print(f"Starting Round {round_number}...")
        # Additional game logic can be added here

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    return player_answer.strip().lower() == correct_answer.strip().lower()

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    if correct:
        return score + 10  # Award 10 points for a correct answer
    return score  # No change for an incorrect answer

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    return round_number + 1

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    return incorrect_answers >= 3

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    choice = input("Would you like to restart the game? (yes/no): ").strip().lower()
    if choice == 'yes':
        print("Restarting the game...")
        # Logic to restart the game can be added here
    else:
        print("Thank you for playing! Goodbye!")
        exit()

#---------------------------------------
