class Cartes:
    def __init__(self):
        self.spades = {
            14: {"emoji": "🂡", "name": "Ace Spades"},
            2: {"emoji": "🂢", "name": "2 Spades"},
            3: {"emoji": "🂣", "name": "3 Spades"},
            4: {"emoji": "🂤", "name": "4 Spades"},
            5: {"emoji": "🂥", "name": "5 Spades"},
            6: {"emoji": "🂦", "name": "6 Spades"},
            7: {"emoji": "🂧", "name": "7 Spades"},
            8: {"emoji": "🂨", "name": "8 Spades"},
            9: {"emoji": "🂩", "name": "9 Spades"},
            10: {"emoji": "🂪", "name": "10 Spades"},
            11: {"emoji": "🂫", "name": "Jack Spades"},
            12: {"emoji": "🂭", "name": "Queen Spades"},
            13: {"emoji": "🂮", "name": "King Spades"}
        }

        self.hearts = {
            14: {"emoji": "🂱", "name": "Ace Hearts"},
            2: {"emoji": "🂲", "name": "2 Hearts"},
            3: {"emoji": "🂳", "name": "3 Hearts"},
            4: {"emoji": "🂴", "name": "4 Hearts"},
            5: {"emoji": "🂵", "name": "5 Hearts"},
            6: {"emoji": "🂶", "name": "6 Hearts"},
            7: {"emoji": "🂷", "name": "7 Hearts"},
            8: {"emoji": "🂸", "name": "8 Hearts"},
            9: {"emoji": "🂹", "name": "9 Hearts"},
            10: {"emoji": "🂺", "name": "10 Hearts"},
            11: {"emoji": "🂻", "name": "Jack Hearts"},
            12: {"emoji": "🂽", "name": "Queen Hearts"},
            13: {"emoji": "🂾", "name": "King Hearts"}
        }

        self.diamonds = {
            14: {"emoji": "🃁", "name": "Ace Diamonds"},
            2: {"emoji": "🃂", "name": "2 Diamonds"},
            3: {"emoji": "🃃", "name": "3 Diamonds"},
            4: {"emoji": "🃄", "name": "4 Diamonds"},
            5: {"emoji": "🃅", "name": "5 Diamonds"},
            6: {"emoji": "🃆", "name": "6 Diamonds"},
            7: {"emoji": "🃇", "name": "7 Diamonds"},
            8: {"emoji": "🃈", "name": "8 Diamonds"},
            9: {"emoji": "🃉", "name": "9 Diamonds"},
            10: {"emoji": "🃊", "name": "10 Diamonds"},
            11: {"emoji": "🃋", "name": "Jack Diamonds"},
            12: {"emoji": "🃍", "name": "Queen Diamonds"},
            13: {"emoji": "🃎", "name": "King Diamonds"}
        }

        self.clubs = {
            14: {"emoji": "🃑", "name": "Ace Clubs"},
            2: {"emoji": "🃒", "name": "2 Clubs"},
            3: {"emoji": "🃓", "name": "3 Clubs"},
            4: {"emoji": "🃔", "name": "4 Clubs"},
            5: {"emoji": "🃕", "name": "5 Clubs"},
            6: {"emoji": "🃖", "name": "6 Clubs"},
            7: {"emoji": "🃗", "name": "7 Clubs"},
            8: {"emoji": "🃘", "name": "8 Clubs"},
            9: {"emoji": "🃙", "name": "9 Clubs"},
            10: {"emoji": "🃚", "name": "10 Clubs"},
            11: {"emoji": "🃛", "name": "Jack Clubs"},
            12: {"emoji": "🃝", "name": "Queen Clubs"},
            13: {"emoji": "🃞", "name": "King Clubs"}
        }

        self.deck = {**self.spades, **self.hearts, **self.diamonds, **self.clubs}
