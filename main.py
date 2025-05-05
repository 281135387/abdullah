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

#---------------------------------
# game_mechanics.py
#    StudentA
#--------------------------------

import random
from question_bank import select_random_question, check_answer, remove_question, display_question_and_accept_answer, provide_hint, display_correct_answer

# Global variables
score = 0
round_number = 1
incorrect_answers = 0
max_incorrect = 3

def display_welcome_message():
    print("Welcome to Trivia Trek! Get ready for an exciting quiz adventure.")
    print("Answer correctly to earn points and progress through rounds!")

def choose_category():
    categories = ["Science", "History", "Geography"]
    print("Choose a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    category_choice = int(input("Enter the number of your chosen category: "))
    return categories[category_choice - 1]

def display_score_and_round():
    print(f"Round {round_number} | Current Score: {score}")

def game_over():
    print(f"Game Over! Your final score is: {score}")
    exit()

def increase_round():
    global round_number
    round_number += 1

def main_game_loop():
    global score, round_number, incorrect_answers

    display_welcome_message()
    category = choose_category()

    while round_number <= 5 and incorrect_answers < max_incorrect:
        display_score_and_round()

        # Select and display question
        question, correct_answer = select_random_question(category)
        player_answer = display_question_and_accept_answer(question)
        
        # Check the player's answer
        if check_answer(player_answer, correct_answer):
            score += 10  # Example scoring system
            print("Correct! You've earned 10 points.")
        else:
            incorrect_answers += 1
            display_correct_answer(correct_answer)
            print(f"Incorrect! You have {max_incorrect - incorrect_answers} incorrect attempts left.")
        
        # Remove the question from the list after it's asked
        remove_question(category, question)

        # If incorrect answers reach the limit, end the game
        if incorrect_answers == max_incorrect:
            game_over()

        # Increase the round number
        increase_round()

    if incorrect_answers < max_incorrect:
        print("Congratulations, you've completed the game!")
        print(f"Your final score is: {score}")
    else:
        game_over()



#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------
import random

# Questions and answers for categories
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for nitrogen?", "N"),
        ("What is the atomic number of hydrogen?", "1"),
        ("What planet is known as the Red Planet?", "Mars")
    ],
    "History": [
        ("Who was the first President of the United States?", "George Washington"),
        ("In what year did World War II end?", "1945"),
        ("Who discovered America?", "Christopher Columbus"),
        ("What ancient civilization built the pyramids?", "Egyptians")
    ],
    "Geography": [
        ("What is the capital of France?", "Paris"),
        ("Which continent is Egypt located in?", "Africa"),
        ("What is the longest river in the world?", "Amazon"),
        ("Which ocean is the largest?", "Pacific")
    ]
}

hints = {
    "Science": [
        "The chemical symbol for water is made up of two elements, one of which is hydrogen.",
        "The chemical symbol for nitrogen is a single letter.",
        "Hydrogen is the first element on the periodic table.",
        "It is the planet closest to Earth."
    ],
    "History": [
        "He was the first president of the USA and led during the American Revolution.",
        "The war ended in the mid-1940s.",
        "He sailed across the Atlantic Ocean in 1492.",
        "They were located near the Nile River."
    ],
    "Geography": [
        "It is a famous European city known for the Eiffel Tower.",
        "It's a country known for the Sahara Desert.",
        "It flows through South America.",
        "This ocean covers more than a third of the Earth's surface."
    ]
}

def select_random_question(category):
    """ Selects a random question from the specified category. """
    question = random.choice(questions[category])
    return question

def check_answer(player_answer, correct_answer):
    """ Checks if the player's answer matches the correct answer. """
    return player_answer.strip().lower() == correct_answer.lower()

def remove_question(category, question):
    """ Removes the question from the list once it has been asked. """
    questions[category].remove(question)

def display_question_and_accept_answer(question):
    """ Displays a question and accepts the player's answer. """
    print(question[0])
    player_answer = input("Your answer: ")
    return player_answer

def provide_hint(category, question):
    """ Provides a hint for the given question. """
    index = questions[category].index(question)
    return hints[category][index]

def display_correct_answer(correct_answer):
    """ Displays the correct answer if the player was incorrect. """
    print(f"The correct answer was: {correct_answer}")



#---------------------------------------
#   Question experience
#      Student C
#---------------------------------------


import json
import time

# Dummy leaderboard for now
leaderboard = {}

def choose_difficulty():
    """ Lets the player choose the difficulty level, affecting score. """
    print("Choose difficulty:")
    print("1. Easy (5 points)")
    print("2. Medium (10 points)")
    print("3. Hard (15 points)")
    difficulty = int(input("Enter the number for your choice: "))
    if difficulty == 1:
        return 5
    elif difficulty == 2:
        return 10
    elif difficulty == 3:
        return 15

def save_score(player_name, score):
    """ Saves the player's score to a file. """
    leaderboard[player_name] = score
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f)

def load_scores():
    """ Loads the top scores from the file. """
    global leaderboard
    try:
        with open("leaderboard.json", "r") as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = {}

def show_leaderboard():
    """ Displays the leaderboard. """
    print("Leaderboard:")
    for player, score in leaderboard.items():
        print(f"{player}: {score}")

def provide_feedback(score):
    """ Gives feedback based on score. """
    if score >= 40:
        print("Great job! You're a quiz master!")
    elif score >= 20:
        print("Good job! Keep it up!")
    else:
        print("Try again! You can do better next time!")

def start_timer():
    """ Timer for each question (just an example). """
    print("You have 30 seconds to answer!")
    time.sleep(30)  # Placeholder for timer functionality.


