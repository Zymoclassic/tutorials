#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):

    def __init__(self):
        self.name = "Rock Player"

    def get_choice(self):
        return 'rock'


class RandomPlayer(Player):

    def __init__(self):
        self.name = "Random Player"
        self.p1 = random.choice(["rock", "paper", "scissors"])
        self.p2 = random.choice(["rock", "paper", "scissors"])

    def get_choice(self):
        return self.p1

    def moveplay(self):
        return self.p2


class HumanPlayer(Player):

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def player_choice(self):
        print("Enter your choice: (rock, paper, scissors)")
        my_choice = input().lower()
        if my_choice not in self.choices:
            print("Invalid choice. \n\
                  Please choose from rock, paper, or scissors.")
            return self.player_choice()
        return my_choice


class ReflectPlayer(Player):

    def __init__(self):
        self.name = "Reflect Player"
        self.my_move = None
        self.their_move = None

    def get_choice(self):
        if self.their_move is not None:
            return self.their_move
        else:
            return random.choice(["rock", "paper", "scissors"])

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):

    def __init__(self):
        self.name = "Cycle Player"
        self.my_move = None
        self.their_move = None
        self.playchoice = ["rock", "paper", "scissors"]
        self.currentmove = 0

    def get_choice(self):
        if self.their_move is not None:
            self.currentmove = (self.currentmove + 1) % len(self.playchoice)
            return self.playchoice[self.currentmove]
        else:
            return random.choice(self.playchoice)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class Game:

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.computer2_score = 0
        self.round = 0
        self.opponent = random.choice([
                AllRockPlayer(),
                RandomPlayer(),
                ReflectPlayer(),
                CyclePlayer()
            ])

    def get_player_choice(self):
        return HumanPlayer().player_choice()

    def get_computer_choice(self):
        return RandomPlayer().get_choice()

    def get_computer2_choice(self):
        return RandomPlayer().moveplay()

    def determine_winner_pc(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_pc(self):
        self.round += 1
        player_choice = self.get_player_choice()
        computer_choice = self.opponent.get_choice()
        self.opponent.learn(computer_choice, player_choice)
        print(f"You are playing against {self.opponent.name}")
        print(f"Round {self.round}")
        print(f"You chose {player_choice}.\n\
Computer chose {computer_choice}.")
        result = self.determine_winner_pc(player_choice, computer_choice)
        print(result)
        print(f"Player: {self.player_score}\n\
Computer: {self.computer_score}")

        play_again = input("Play again?\n\
Reply 'yes' to continue or reply with anything else to quit : ").lower()
        if play_again == "yes":
            game.play_pc()
        else:
            if self.player_score > self.computer_score:
                print(f"Your score is {self.player_score},\n\
The computer score is {self.computer_score}.\n\
You won this game!!!")
            elif self.player_score < self.computer_score:
                print(f"Your score is {self.player_score},\n\
The computer score is {self.computer_score}.\n\
The Computer won this game!!!")
            else:
                print(f"Your score is {self.player_score},\n\
The computer score is {self.computer_score}.\n\
This game is a tie!!!")
            print("Thanks for playing!")

    def determine_winner_cc(self, computer_choice, computer2_choice):
        if computer_choice == computer2_choice:
            return "It's a tie!"
        elif (computer_choice == "rock" and computer2_choice == "scissors") \
            or (computer_choice == "paper" and computer2_choice == "rock") \
                or (computer_choice == "scissors" and
                    computer2_choice == "paper"):
            self.computer_score += 1
            return "Player 1 win!"
        else:
            self.computer2_score += 1
            return "Player 2 wins!"

    def play_cc(self):
        self.round += 1
        computer_choice = self.get_computer_choice()
        computer2_choice = self.get_computer2_choice()
        print(f"Round {self.round}")
        print(f"Player 1 chose {computer_choice}.\n\
Player 2 chose {computer2_choice}.")
        result = self.determine_winner_cc(computer_choice,
                                          computer2_choice)
        print(result)
        print(f"Player 1: {self.computer_score}\n\
Player 2: {self.computer2_score}")

        play_again = input("Play again?\n\
Reply 'yes' to continue or reply with anything else to quit) : ").lower()
        if play_again == "yes":
            game.play_cc()
        else:
            if self.computer2_score > self.computer_score:
                print(f"Player 1 score is {self.computer_score},\n\
Player 2 score is {self.computer2_score}.\n\
Player 2 won this game!!!")
            elif self.computer2_score < self.computer_score:
                print(f"Player 1 score is {self.computer_score},\n\
Player 2 score is {self.computer2_score}.\n\
Player 1 won this game!!!")
            else:
                print(f"Player 1 score is {self.computer_score},\n\
Player 2 score is {self.computer2_score}.\n\
This game is a tie!!!")
            print("Thanks for playing!")

    def start(self):
        gameselect = int(input())
        if gameselect == 0:
            game.play_cc()
        elif gameselect == 1:
            game.play_pc()
        else:
            print("Invalid selection, Please try again")
            self.start()


if __name__ == "__main__":
    game = Game()
    print("How many players? (Enter 0 or 1)")
    game.start()

