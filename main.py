from collections import Counter
from roll import Roulette
import random
import time

class Cartes: # багатофункціональна колода карт
    def __init__(self): # конструктор колоди з її значеннями
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
        self.deck = [] # створення колоди
        # додаємо значення рангу карти з кожної масті в колоду за допомогою таких for loop умов і методів self.deck.append()
        for rank in self.spades:
            self.deck.append({"rank": rank, "suit": "Spades", **self.spades[rank]})
        for rank in self.hearts:
            self.deck.append({"rank": rank, "suit": "Hearts", **self.hearts[rank]})
        for rank in self.diamonds:
            self.deck.append({"rank": rank, "suit": "Diamonds", **self.diamonds[rank]})
        for rank in self.clubs:
            self.deck.append({"rank": rank, "suit": "Clubs", **self.clubs[rank]})
        
    def create_deck(self): # функція створення столу
        random.shuffle(self.deck) # перемішуємо колоду
        return self.deck.copy() # повертаємо копію цієї колоди для кожного конкретного раунду гри
cartes = Cartes() # отримуємо доступ до значення класу карт для покеру і блекджеку через змінну карт
roulette = Roulette() # отримуємо доступ до значеннь столу рулетки які раніше через from roll import Roulette імпортували з іншого файлу

def access(): # проста функція доступу до функціоналу програми через пароль і його перевірку
    password = "pbrsm2025"
    check = input("Type your key to get access to game: ").lower().strip()
    return check == password

def roulette_game(balance): # гра в рулетку
    is_running = True # задаємо конкретній змінній логічне значення щоб легше було контролювати ходом гри і позиціями її заверщення
    if balance <= 0: # умови перевірки балансу
        deposit = float(input("Deposit your debt: "))
        if deposit > 0:
            balance += deposit
        else:
            print("Deposit can\'t be 0 or lower")
            return balance
        
    while is_running:    # цикл гри
        bet_type = input("""What is your bet type?: 
                        1. Color
                        2. Even/Odd
                        3. Number
                        4. Section
                        5. Quit\n\n""") # змінна яка дає нам обрати тип ставки
        if bet_type.isdigit(): # перевіряємо чи та змінна є числом через метод .isdigit()
            bet_type = int(bet_type) # перетворюємо змінну в змінну яка є цілим числом яке наш користувач введе (пояснюю це собі, бо для мене це був перший досвід використання подібних прийомів)
            if bet_type not in [1,2,3,4,5]: # створюємо список для всіх опцій з меню для спрощеної перевірки чи є вони в вводі користувача, якщо їх немає виводмо повідомлення про непривильну опцію, якщо є, надаємо доступ до подальшого функціоналу гри
                print("Invalid option")
                return balance
            # тип ставки кольор
            elif bet_type == 1:
                bet_color = int(input("""What color you want to bet?: 
                                1. Green
                                2. Red
                                3. Black
                                4. Quit"""))
                if bet_color == 1:
                    bet_color = "green"
                elif bet_color == 2:
                    bet_color = "red"
                elif bet_color == 3:
                    bet_color = "black"
                elif bet_color == 4:
                    is_running = False
                    continue

                bet_amount = input("""Enter your bet amount (no lesser than 10$) or chose our presets:
                                        1. 100$
                                        2. 500$
                                        3. 1000$
                                        4. 5000$
                                        5. Quit\n\n""")
                if bet_amount.isdigit():
                    bet_amount = float(bet_amount)
                    
                    if bet_amount > balance:
                        print("Bet can\'t be more than balance")
                        continue
                    elif bet_amount <= 0:
                        print("Bet can\'t be lower or equal to 0")
                        continue
                    elif bet_amount in range(1,10):
                        if bet_amount == 1:
                            bet_amount = 100
                        elif bet_amount == 2:
                            bet_amount = 500
                        elif bet_amount == 3:
                            bet_amount = 1000
                        elif bet_amount == 4:
                            bet_amount = 5000
                        elif bet_amount == 5:
                            is_running = False
                        else:
                            print("Bet can\'t be lower than 10$")
                else:
                    print("Invalid type of bet")
            
                balance -= bet_amount

                result = random.choice(list(roulette.roulette.keys()))
                result_color = roulette.roulette[result]["color"]
                print("Game had began. Ball will land in 30 seconds")
                countdown = 30
                while countdown > 0:
                    print(f"{countdown} seconds left")
                    time.sleep(1)
                    countdown -= 1
                print(f"The ball landed on {result} ({result_color})")

                if bet_color == result_color:
                    if bet_color == "green":
                        winning = bet_amount * 100
                    elif bet_color == "red":
                        winning = bet_amount * 20
                    elif bet_color == "black":
                        winning = bet_amount * 20
                    print(f"You won {winning:.2f}$!")
                    print(f"Your balance: {balance:.2f}$")
                    balance += winning
                else:
                    print("You lose!")
                    print(f"Your balance: {balance:.2f}")
            # тип ставки парне/непарне
            elif bet_type == 2:
                ev_odd = int(input("""Even or odd?:
                            1. Single
                            2. Even
                            3. Odd
                            4. Quit\n\n"""))
                if ev_odd == 1:
                    ev_odd = "single"
                elif ev_odd == 2:
                    ev_odd = "even"
                elif ev_odd == 3:
                    ev_odd = "odd"
                elif ev_odd == 4:
                    is_running = False
                    continue

                bet_amount = input("""Enter your bet amount (no lesser than 10$) or chose our presets:
                                        1. 100$
                                        2. 500$
                                        3. 1000$
                                        4. 5000$
                                        5. Quit\n\n""")
                if bet_amount.isdigit():
                    bet_amount = float(bet_amount)
                    
                    if bet_amount > balance:
                        print("Bet can\'t be more than balane")
                        continue
                    elif bet_amount <= 0:
                        print("Bet can\'t be lower or equal to 0")
                        continue
                    elif bet_amount in range(1,10):
                        if bet_amount == 1:
                            bet_amount = 100
                        elif bet_amount == 2:
                            bet_amount = 500
                        elif bet_amount == 3:
                            bet_amount = 1000
                        elif bet_amount == 4:
                            bet_amount = 5000
                        elif bet_amount == 5:
                            is_running = False
                        else:
                            print("Bet can\'t be lower than 10$")
                            continue
                else:
                    print("Invalid type of bet")
            
                balance -= bet_amount

                result = random.choice(list(roulette.roulette.keys()))
                result_type = roulette.roulette[result]["type"]
                print("Game had began. Ball will land in 30 seconds!")
                countdown = 30
                while countdown > 0:
                    print(f"{countdown} seconds left")
                    time.sleep(1)
                    countdown -= 1
                print(f"Ball landed on {result} {result_type}")

                if ev_odd == result_type:
                    if ev_odd == "single":
                        winning = bet_amount * 100
                    elif ev_odd == "even":
                        winning = bet_amount * 30
                    elif ev_odd == "odd":
                        winning = bet_amount * 30
                    print(f"You won {winning:.2f}$")
                    print(f"Your balnce: {balance:.2f}$")
                    balance += winning
                else:
                    print("You lose!")
                    print(f"Your balance: {balance:.2f}$")
            # тип ставки номер
            elif bet_type == 3:
                bet_num = input("Enter a number of your bet (0-36): ")

                if bet_num.isdigit():
                    bet_num = int(bet_num)

                    if bet_num < 0:
                        print("Chosed number must be in range 0-36.")
                        continue
                    elif bet_num > 37:
                        print("Chosed number must be in range 0-36")
                        continue
                else:
                    print("Invalid value")

                bet_amount = input("""Enter your bet amount (higher that 10$) or chose suggested options: 
                                1. 50$
                                2. 100$
                                3. 250$
                                4. 500$
                                5. 1000$
                                6. Quit
                                \n\n""")
                
                if bet_amount.isdigit():
                    bet_amount = float(bet_amount)

                    if bet_amount > balance:
                        print("Bet can\'t be more than balance")
                        continue
                    elif bet_amount <= 0:
                        print("Bet can\'t be lower or equal to 0")
                        continue
                    elif bet_amount in range(1,10):
                        if bet_amount == 1:
                            bet_amount = 50
                        elif bet_amount == 2:
                            bet_amount = 100
                        elif bet_amount == 3:
                            bet_amount = 250
                        elif bet_amount == 4:
                            bet_amount = 500
                        elif bet_amount == 5:
                            bet_amount = 1000
                        elif bet_amount == 6:
                            is_running = False
                        else:
                            print("Bet can\'t be lower than 10$")
                            continue
                else:
                    print("Invalid type of bet")

                balance -= bet_amount

                result = random.choice(list(roulette.roulette.keys()))
                result_symbol = roulette.roulette[result]["symbol"]
                print("Game had began. Ball will land in 30 seconds")
                countdown = 30
                while countdown > 0:
                    print(f"{countdown} seconds left")
                    time.sleep(1)
                    countdown -= 1
                print(f"Ball landed on {result} ({result_symbol})")

                if bet_num == result_symbol:
                    if bet_num == 0:
                        winning = bet_amount * 100
                    elif bet_num in range(1, 37):  # Замість "36", оскільки результат може включати всі числа до 36
                        winning = bet_amount * 30
                    print(f"You won {winning:.2f}$")
                    print(f"Your balance: {balance:.2f}$")
                    balance += winning
                else:
                    print("You lose!")
                    print(f"Your balance: {balance:.2f}$")
            # тип ставки секція
            elif bet_type == 4:
                bet_section = input("""What section you want to set bet:
                1. 0                    
                2. 1-17
                3. 18-36
                4. Quit\n\n""")

                if bet_section.isdigit():
                    bet_section = int(bet_section)

                    if bet_section == 1:
                        bet_section = 0
                    elif bet_section == 2:
                        bet_section = random.randint(1,17)
                    elif bet_section == 3:
                        bet_section == random.randint(18,37)
                    elif bet_section == 4:
                        is_running = False
                    else:
                        print("Invalid choice")
                        continue
                else:
                    print("Invalid input")

                bet_amount = input("""Enter your bet amount (higher that 10$) or chose suggested options: 
                                1. 50$
                                2. 100$
                                3. 250$
                                4. 500$
                                5. 1000$
                                6. Quit
                                \n\n""")
                
                if bet_amount.isdigit():
                    bet_amount = float(bet_amount)

                    if bet_amount > balance:
                        print("Bet can\'t be more than balance")
                        continue
                    elif bet_amount <= 0:
                        print("Bet can\'t be lower or equal to 0")
                        continue
                    elif bet_amount in range(1,10):
                        if bet_amount == 1:
                            bet_amount = 50
                        elif bet_amount == 2:
                            bet_amount = 100
                        elif bet_amount == 3:
                            bet_amount = 250
                        elif bet_amount == 4:
                            bet_amount = 500
                        elif bet_amount == 5:
                            bet_amount = 1000
                        elif bet_amount == 6:
                            is_running = False
                        else:
                            print("Bet can\'t be lower than 10$")
                            continue
                else:
                    print("Invalid type of bet")

                balance -= bet_amount

                result = random.choice(list(roulette.roulette.keys()))
                result_section = roulette.roulette[result]["section"]
                print("Game had began. Ball will land in 30 seconds")
                countdown = 30
                while countdown > 0:
                    print(f"{countdown} seconds left")
                    time.sleep(1)
                    countdown -= 1
                print(f"Ball landed on {result} ({result_section})")

                if bet_section == result_section:
                    if bet_section == 0:
                        winning = bet_amount * 100
                    elif 1 <= bet_section <= 17:
                        winning = bet_amount * 20
                    elif 18 <= bet_section <= 37:
                        winning = bet_amount * 20
                    print(f"You won {winning:.2f}$")
                    print(f"Your balance: {balance:.2f}$")
                    balance += winning
                else:
                    print("You lose")
                    print(f"Your balance: {balance:.2f}$")
            elif bet_type == 5:
                is_running = False

            if input("Do you want to play one more round? (Y/N): ").upper().strip() != "Y":
                is_running = False
    print(f"Your total: {balance:.2f}$")
    return balance

def poker(balance):
    # Перевірка балансу перед посадкою за стіл
    while balance < 1000: # створення циклу для перевірки умови чи є на балансі необхідна сума
        deposit = float(input(f"Deposit your balance to at least 1000$ (current balance: {balance:.2f}$): "))
        if deposit <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            balance += deposit

    human_name = input("What is your name? ").strip()
    # Створення інших гравців
    names = ["Alice", "John", "Mattew", "Jessie", "Patrick", "Alexa"]
    random.shuffle(names)
    
    # створення гравців через словник і подальше додавання ботів в цей словник
    players = {
        "human": {"name": human_name, "balance": balance}
    }
    for i in range(1, 5):
        players[f"player{i}"] = {"name": names[i-1], "balance": random.randint(1000, 5000)}
    
    # створення видів режимів гри (3, 4, 5 гравців за столом)
    game_modes = input("""What game mode do you want to play? \n1. 3 players\n2. 4 players\n3. 5 players\n4. Exit\n\n: """)
    selected_players = [players["human"]]  # Завжди додаємо людину
    if game_modes.isdigit():
        game_modes = int(game_modes)
        if game_modes == 1:
            selected_players += random.sample(list(players.values())[1:], 2)  # Додаємо 2 боти
        elif game_modes == 2:
            selected_players += random.sample(list(players.values())[1:], 3)  # Додаємо 3 боти
        elif game_modes == 3:
            selected_players += random.sample(list(players.values())[1:], 4)  # Додаємо 4 боти
        elif game_modes == 4:
            return balance

    # Використання створеної колоди карт з класу Cartes
    deck = cartes.create_deck()
    community_cards = []  # Визначення змінної community_cards

    def deal_hands(): # функція видачі карт гравцям, шукаємо гравців в обраних гравцях (їхню кількісь в обраному гравцем режимі) і кожному видаємо карти
        for player in selected_players:
            player["hand"] = [deck.pop(), deck.pop()]

    deal_hands() # запуск функції 

    # Відображення карт гравців (лише для людини)
    def show_hands(): # функція показу карт гравцеві
        for player in selected_players:
            if player["name"] == human_name:
                hand = player["hand"]
                print(f"{player['name']} has {hand[0]['emoji']} ({hand[0]['name']}) and {hand[1]['emoji']} ({hand[1]['name']})")
            else:
                print(f"{player['name']}'s cards are hidden.")

    def deal_community_cards(round_name, num_cards): # функція видачі карт на стіл від дилера
        print(f"\n{round_name}")
        for _ in range(num_cards):
            community_cards.append(deck.pop()) # на стіл додаємо карту(community_cards.append()) з колоди забираємо (deck.pop())
        print("Community Cards:", " ".join([card['emoji'] for card in community_cards]))

    def betting_round(pot): # функція ставки гравця і ботів
        current_bet = 0
        for player in selected_players:
            if player["name"] == human_name:
                while True:
                    print("\nChoose your action:")
                    print("1. Fold")
                    print("2. Call/Check")
                    print("3. Raise")
                    print("4. All-in")
                    print("5. Exit")
                    action = input(f"{player['name']}, enter the number of your action: ").strip()
                    
                    if action.isdigit():
                        action = int(action)
                        if action == 1:
                            print(f"{player['name']} folds.")
                            selected_players.remove(player)
                            break
                        elif action == 2:
                            if current_bet == 0:
                                print(f"{player['name']} checks.")
                            else:
                                player["balance"] -= current_bet
                                pot += current_bet
                                print(f"{player['name']} calls with {current_bet:.2f}$. Remaining balance: {player['balance']:.2f}$")
                            break
                        elif action == 3:
                            raise_amount = float(input("Enter raise amount: "))
                            if raise_amount <= player["balance"]:
                                current_bet = raise_amount
                                player["balance"] -= raise_amount
                                pot += raise_amount
                                print(f"{player['name']} raises to {raise_amount:.2f}$. Remaining balance: {player['balance']:.2f}$")
                                break
                            else:
                                print("Raise amount exceeds your balance. Try again.")
                        elif action == 4:
                            current_bet = player["balance"]
                            pot += player["balance"]
                            player["balance"] = 0
                            print(f"{player['name']} goes all-in with {current_bet:.2f}$")
                            break
                        elif action == 5:
                            print("Game interrupted by the player.")
                            return False, pot
                        else:
                            print("Invalid action. Try again.")
                    else:
                        print("Invalid input. Please enter a number from 1 to 5.")
            else:
                print("Players taking actions...")
                time.sleep(random.uniform(5, 15))  # Боти "думають"
                action = random.choice(["fold", "call", "check", "raise", "all-in"])
                if action == "fold":
                    print(f"{player['name']} folds.")
                    selected_players.remove(player)
                elif action == "call" or action == "check":
                    if current_bet == 0:
                        print(f"{player['name']} checks.")
                    else:
                        player["balance"] -= current_bet
                        pot += current_bet
                        print(f"{player['name']} calls with {current_bet:.2f}$. Remaining balance: {player['balance']:.2f}$")
                elif action == "raise":
                    raise_amount = min(random.uniform(50, 500), player["balance"])
                    current_bet = raise_amount
                    player["balance"] -= raise_amount
                    pot += raise_amount
                    print(f"{player['name']} raises to {raise_amount:.2f}$. Remaining balance: {player['balance']:.2f}$")
                elif action == "all-in":
                    current_bet = player["balance"]
                    pot += player["balance"]
                    player["balance"] = 0
                    print(f"{player['name']} goes all-in with {current_bet:.2f}$")
            print(f"Pot is now {pot:.2f}$")
        return True, pot

    def play_rounds(): # функція відігравання раундів
        deal_hands()
        pot = 0  # Ініціалізація поту
        print("\n--- Pre-Flop ---")
        show_hands()
        continue_game, pot = betting_round(pot)
        if not continue_game:
            return pot

        print("\n--- Flop ---")
        deal_community_cards("Flop", 3) # в раунді флоп дилер видає три карти на стіл
        continue_game, pot = betting_round(pot)
        if not continue_game:
            return pot

        print("\n--- Turn ---")
        deal_community_cards("Turn", 1) # в торні одну карту
        continue_game, pot = betting_round(pot)
        if not continue_game:
            return pot

        print("\n--- River ---")
        deal_community_cards("River", 1) # в рівері теж одну
        continue_game, pot = betting_round(pot)
        if not continue_game:
            return pot

        return pot

    def evaluate_hand(hand): # обробка рангів і мастей карт
        combined = hand + community_cards
        ranks = [card['rank'] for card in combined]
        suits = [card['suit'] for card in combined]
        rank_counts = Counter(ranks) # підраховуємо всі комбінації з столу і гравців

        # Перевірка на стріт-флеш, флеш, стріт, каре, фул-хаус, трійка, дві пари, пара, старша карта
        if is_royal_flush(combined): # обробка комбінації через змінну комбінації бо ця комбінація включає і карти зі столу і карти гравця
            return ("Royal Flush", 10)
        elif is_straight_flush(combined): # теж саме
            return ("Straight Flush", 9)
        elif is_four_of_a_kind(rank_counts): # обробка комбінації через підрахунок рангів, бо нам треба певний набір рангів кард
            return ("Four of a Kind", 8)
        elif is_full_house(rank_counts): # теж саме
            return ("Full House", 7)
        elif is_flush(suits): # обробка комбінації по мастям
            return ("Flush", 6)
        elif is_straight(ranks): # обробка комбінації по рангам
            return ("Straight", 5)
        elif is_three_of_a_kind(rank_counts):
            return ("Three of a Kind", 4)
        elif is_two_pair(rank_counts):
            return ("Two Pair", 3)
        elif is_pair(rank_counts):
            return ("One Pair", 2)
        else:
            return ("High Card", 1, max(ranks, key=rank_value)) # обробка комбінації старшої карти, якщо ні в кого немає комбінацій наведених вище

    def is_royal_flush(combined):
        return is_straight_flush(combined) and max(rank_value(card['rank']) for card in combined) == 14

    def is_straight_flush(combined):
        return is_flush([card['suit'] for card in combined]) and is_straight([card['rank'] for card in combined])

    def is_four_of_a_kind(rank_counts):
        return 4 in rank_counts.values()

    def is_full_house(rank_counts):
        return 3 in rank_counts.values() and 2 in rank_counts.values()

    def is_flush(suits):
        return any(suits.count(suit) >= 5 for suit in suits)

    def is_straight(ranks):
        values = sorted(rank_value(rank) for rank in set(ranks))
        for i in range(len(values) - 4):
            if values[i:i+5] == list(range(values[i], values[i]+5)):
                return True
        return False

    def is_three_of_a_kind(rank_counts):
        return 3 in rank_counts.values()

    def is_two_pair(rank_counts):
        return list(rank_counts.values()).count(2) == 2

    def is_pair(rank_counts):
        return 2 in rank_counts.values()

    def rank_value(rank):
        if isinstance(rank, int):  # Якщо ранг є числом
            return rank
        else:  # Якщо ранг є строковим значенням ("J", "Q", "K", "A")
            return {"J": 11, "Q": 12, "K": 13, "A": 14}[rank]

    while True:
        if len(selected_players) < 2:
            print("Not enough players left to continue. Game over.")
            break

        pot = play_rounds()

        # Визначення переможця
        player_hands = [(player['name'], *evaluate_hand(player["hand"])) for player in selected_players]
        winner = max(player_hands, key=lambda x: (x[1], x[2] if len(x) > 2 else 0))  # Порівняння по комбінаціях і старшій карті
        print(f"\n{winner[0]} wins with {winner[1]}!")
        for player in selected_players:
            if player['name'] == winner[0]:
                player['balance'] += pot
            #     if player["balance"] == human_name:
            #         balance = player["balance"]
            #     break
            # elif player["name"] != winner[0]:
            #     player["balance"] -= pot
            #     if player["balance"] == human_name:
            #         balance = player["balance"]
            #     break
        print(f"The pot of {pot:.2f}$ has been added to {winner[0]}'s balance.")

        if input("Do you want to play another round? (Y/N): ").upper() != "Y":
            break
        else:
            deck = cartes.create_deck()
            community_cards.clear()
            deal_hands()  # Нові карти для наступного раунду

    return balance

def blackjack(balance):
    while balance < 1000:
        deposit = int(input("Сума для депозиту: "))
        if deposit <= 0:
            print("Сума депозиту не може бути 0 або менше нього")
            return balance
        else:
            balance += deposit
            print(f"Ваш баланс складає: {balance:.2f} $")
            
    while balance > 1000:
        print(f"\nТвій баланс: ${balance}")
        while True:
            try:
                bet = int(input("Введи суму ставки: "))
                if bet <= 0 or bet > balance:
                    print("Невірна ставка. Введи коректну суму!")
                else:
                    break
            except ValueError:
                print("Введи числове значення ставки!")

        deck = cartes.create_deck()

        def calculate_hand_value(hand):
            values = [min(card["rank"], 10) if card["rank"] != 14 else 11 for card in hand]
            total = sum(values)
            num_aces = sum(1 for card in hand if card["rank"] == 14)

            while total > 21 and num_aces:
                total -= 10
                num_aces -= 1

            return total

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print(f"Твоя рука: {' '.join(card['emoji'] for card in player_hand)}  | Очки: {calculate_hand_value(player_hand)}")
        print(f"Рука дилера: {dealer_hand[0]['emoji']} ❓")

        while calculate_hand_value(player_hand) < 21:
            action = input("Взяти ще карту (h) чи зупинитись (s)? ").strip().lower()
            if action == "h":
                new_card = deck.pop()
                player_hand.append(new_card)
                print(f"Ти взяв: {new_card['emoji']}, очки: {calculate_hand_value(player_hand)}")
            elif action == "s":
                break

        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())

        print(f"Рука дилера: {' '.join(card['emoji'] for card in dealer_hand)} | Очки: {calculate_hand_value(dealer_hand)}")

        player_score = calculate_hand_value(player_hand)
        dealer_score = calculate_hand_value(dealer_hand)

        if player_score > 21:
            print("Перебір! Ти програв 😞")
            balance -= bet
        elif dealer_score > 21 or player_score > dealer_score:
            print(f"Ти виграв! 🎉 Твій виграш: {bet * 2} $")
            balance += bet
            print(f"Твій баланс: {balance:.2f} $")
        elif player_score < dealer_score:
            print("Ти програв 😞")
            balance -= bet
        else:
            print("Нічия! Ставка повертається.")

        if balance <= 0:
            print("У тебе закінчились гроші! Гра завершена.")
            break

        again = input("Хочеш зіграти ще раз? (y/n): ").strip().lower()
        if again != "y":
            print(f"Твій фінальний баланс: ${balance}. Дякуємо за гру!")
            break
        
def slots_machine(slots, balance):
    is_running = True
    if balance <= 0:
        deposit = float(input("Deposit your debt: "))
        if deposit > 0:
            balance += deposit
        else:
            print("Deposit can't be 0 or lower")
            return balance

    while is_running:
        bet = input("""Place your bet to start (bet must be higher than 10$). Or chose automatic presets: 
1. 50$
2. 100$
3. 500$
4. 1000$
5. Quit\n\n""")

        if bet.isdigit():
            bet = int(bet)
            if bet > balance:
                print("Bet can't be higher than balance")
                continue
            elif bet <= 0:
                print("Bet can't be lower or equal to 0")
                continue
            elif bet in range(1,10):
                if bet == 1:
                    bet = 50
                elif bet == 2:
                    bet = 100
                elif bet == 3:
                    bet = 500
                elif bet == 4:
                    bet = 1000
                elif bet == 5:
                    is_running = False
                else:
                    print("Bet can\'t be lower than 10$")
                    continue
            
            balance -= bet
        

        print(f"Your bet: {bet:.2f}$")
        
        result = [random.choice(slots) for _ in range(3)]
        print("Spinning...")
        time.sleep(1)
        print(result[0])
        time.sleep(1)
        print(result[1])
        time.sleep(1)
        print(result[2])
        print("|".join(result))

        if result[0] == result[1] == result[2]:
            print("💸💸💸JACKPOT!💸💸💸")
            if result[0] == "🃏":
                winnings = bet * 5
            elif result[0] == "🎲":
                winnings = bet * 10
            elif result[0] == "💸":
                winnings = bet * 20
            elif result[0] == "🔮":
                winnings = bet * 25
            elif result[0] == "💰":
                winnings = bet * 30
            elif result[0] == "🏆":
                winnings = bet * 50
            print(f"You won {winnings:.2f}$")
            print(f"You balance: {balance:.2f}$")
            balance += winnings
        else:
            print("LOSE!")
            print(f"Your balance: {balance:.2f}$")
        
        if input("Roll again? (Y/N): ").upper().strip() != "Y":
            is_running = False
    print(f"Your total: {balance:.2f}$")
    return balance

def show_balance(balance):
    print(f"Your balance is {balance:.2f} $")

def deposit_balance(balance):
    try:
        deposing = float(input("Amount to deposit: "))
        if deposing <= 0:
            print("Error! To start the game your balance needs to be higher than 0")
            return balance
        else:
            balance += deposing
            print(f"Your balance: {balance:.2f} $")
    except ValueError:
        print("Invalid input, please enter a number.")
    return balance
    
def withdraw_balance(balance):
    try:
        withdraw = float(input("Amount to withdraw: "))
        if withdraw > balance:
            print("Error! Amount of withdraw can't be higher than balance")
            return balance
        elif withdraw <= 0:
            print("Error! Amount of withdraw can't be lower or equal to 0")
            return balance
        else:
            balance -= withdraw
            print(f"{withdraw:.2f} $ was withdrawn from your account. Current balance: {balance:.2f} $")
    except ValueError:
        print("Invalid input, please enter a number.")
    return balance
    
def main():
    slots = ["🃏", "🎲", "💸", "🔮", "💰", "🏆"]
    balance = 0

    if access():
        print("🔮🎲🃏Python Casino🃏🎲🔮")
        while True:
            menu = input("1. Games.\n2. Show balance.\n3. Deposit Balance.\n4. Withdraw balance.\n5. Exit\n\n")
            if menu == "1":
                gamechose = input("1. Poker\n2. Roulette\n3. Blackjack\n4. Slot Machine\n5. Exit\n\n")
                if gamechose == "1":
                    balance = poker(balance)
                elif gamechose == "2":
                    balance = roulette_game(balance)
                elif gamechose == "3":
                    balance = blackjack(balance)
                elif gamechose == "4":
                    balance = slots_machine(slots, balance)
                elif gamechose == "5":
                    continue
                else:
                    print("Invalid choice from menu")
            elif menu == "2":
                show_balance(balance)
            elif menu == "3":
                balance = deposit_balance(balance)
            elif menu == "4":
                balance = withdraw_balance(balance)
            elif menu == "5":
                break
            else:
                print("Invalid option")
    else:
        print("Access denied!")

if __name__ == "__main__":
    main()