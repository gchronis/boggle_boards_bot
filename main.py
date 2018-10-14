# -*- coding: utf-8 -*-
#
from config import *
import tweepy
import random
from unicodedata import normalize

def login():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def tweet(api, string):
    print string
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
    letters = [ random.choice(die) for die in dice ]
    random.shuffle(letters)
    return letters

WIDE_MAP = dict((i, i + 0xFEE0) for i in xrange(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000

def widen(s):
    """
    Convert all ASCII characters to the full-width counterpart.
    
    >>> print widen('test, Foo!')
    ｔｅｓｔ，　Ｆｏｏ！
    >>> 
    """
    return unicode(s).translate(WIDE_MAP).encode('utf8')

def board_string(letters):
    #horiz = widen("+---------+")
    horiz = widen("+") + " "
    for i in range(7):
        horiz += widen("-") + " "
    horiz += widen("+")

    # construct row divider
    divider = widen("|") + " "
    for i in range(7):
        divider += widen("-") + " "
    divider += widen("|")

    board = ""
    board += horiz
    board += "\n"
    for i in range(4):
        board += widen("|") + " "
        for j in range(4):
            letter = letters.pop()
            if letter == "Q":
                board += "Qu" + widen("|") + " "
            else:
                #board += widen(letter)+" | "
                board += widen(letter) + " " + widen("|") + " "
        board += "\n"
        if not i  == 3:
            #board += widen("| - - - - |")
            board += divider
            board += "\n"
    board += horiz 
    return normalize('NFC',unicode(board, 'utf-8'))

def main():
    letters = generate_board()
    boggle_board = board_string(letters)
    print "Tweeting this board"
    print boggle_board
    api = login()
    tweet(api, boggle_board)
