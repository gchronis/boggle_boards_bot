from config import *
import tweepy
import random

def login():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def tweet(api, string):
    api.update_status(status=string)

# returns a list of 16 boggle letters
def generate_board():
    dice = [
        "RIFOBX",
        "IFEHEY",
        "DENOWS",
        "UTOKND",
        "HMSRAO",
        "LUPETS",
        "ACITOA",
        "YLGKUE",
        "QBMJOA",
        "EHISPN",
        "VETIGN",
        "BALIYT",
        "EZAVND",
        "RALESC",
        "UWILRG",
        "PACEMD",
    ]
    print len(dice)
    letters = [ random.choice(die) for die in dice ]
    print len(letters)
    random.shuffle(letters)
    print len(letters)
    return letters

def board_string(letters):
    horiz = "+---------------+"

    board = ""
    board += horiz
    board += "\n"
    for i in range(4):
        board += "|"
        for j in range(4):
            board += " "
            letter = letters.pop()
            if letter == "Q":
                board += "Qu|"
            else:
                board += letter + " |"
        board += "\n"
        if not i  == 3:
            board += "| - - - - - - - |"
            board += "\n"
    board += horiz 
    print board

letters = generate_board()
boggle_board = board_string(letters)
api = login()
tweet(api, boggle_board)
print string
