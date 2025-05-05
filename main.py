# main.py
#---------------------------------------
#  Main Application
#    Integration of all components
#---------------------------------------

import game_mechanics
import question_bank
import user_experience

def main():
    # Display welcome message
    game_mechanics.welcome_message()
    
    # Allow the player to choose a difficulty (if applicable)
    difficulty = user_experience.choose_difficulty()
    
    # Initialize game state variables
    categories = list(question_bank.questions.keys())
    score = 0
    incorrect_answers = 0
    round_number = 1
    
    # Main game loop
    while not game_mechanics.check_game_over(incorrect_answers):
        # Player chooses a category
        chosen_category = game_mechanics.choose_category(categories)
        
        # A question is selected randomly from the chosen category
        question, correct_answer = question_bank.select_random_question(chosen_category)
        
        # Display the question and accept the player's answer
        player_answer = question_bank.display_question_and_accept_answer(question)
        
        # Validate the player's answer
        correct = question_bank.check_answer(player_answer, correct_answer)
        
        # Update score and incorrect_answers based on the player's answer
        if correct:
            score = game_mechanics.update_score(score, correct)
        else:
            incorrect_answers += 1
            question_bank.display_correct_answer(correct_answer)
        
        # Display the current score and round information
        game_mechanics.display_score(score, round_number)
        
        # Prepare for the next round
        round_number = game_mechanics.next_round(round_number)
        
        # Optionally, remove the question from the pool to prevent repetition
        question_bank.remove_question(chosen_category, question)
        
        # Check if the game should continue or end based on rounds or incorrect answers
        if game_mechanics.check_game_over(incorrect_answers):
            break
    
    # Display game over message and final score
    game_mechanics.game_over_message(score)
    
    # Save the score
    player_name = input("Enter your name: ")
    user_experience.save_score(player_name, score)
    
    # Display leaderboard
    leaderboard = user_experience.load_top_scores()
    user_experience.display_leaderboard(leaderboard)
    
    # Ask the player if they want to restart or exit
    game_mechanics.restart_or_exit()


#---------------------------------
#  Application Entry Point
main()
#---------------------------------

#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for nitrogen?", "N"),
    ],
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for nitrogen?", "N"),
    ],
}

hints = {
    "Science": [
        # Pair each question with a corresponding hint.
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer==correct_answer:
        return True 
    return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
