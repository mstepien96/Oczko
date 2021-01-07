import random


class Deck:
    suit_list = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    rank_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.card_list = []     # initialize card list (empty deck)
        self.create_deck()     # fill up the card list (full deck)

    def __str__(self):
        """Prints joined elements of the list.
        If not joined, ids will be printed instead."""
        return '\n'.join([str(x) for x in self.card_list])

    def __len__(self):
        return len(self.card_list)

    def create_deck(self):
        """Creates a deck of cards using Card class."""
        for suit in Deck.suit_list:
            for rank in Deck.rank_list:
                card = Card(suit, rank)
                self.card_list.append(card)

        return self.card_list


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + ' ' + self.rank


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.points = 0

    def __str__(self):
        return '\n\t'.join([str(x) for x in self.hand])

    def draw_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.hand.append(card)

    def count_points(self):
        self.points = 0
        for card in self.hand:
            self.points += Oczko.values[card.rank]


class Oczko:
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 2,
        'Queen': 3,
        'King': 4,
        'Ace': 11
    }

    def __init__(self):
        self.name = 'OCZKO'

    def __str__(self):
        return self.name


def start_game(game):
    print(f"*********{game.name}*********")

    # Setting number of players
    while True:
        no_of_players = int(input("Type the number of players: "))
        if no_of_players < 2:
            print("There has to be at least two players!")
            continue
        else:
            break

    # Creating a deck and players
    deck = Deck()
    players = []

    for player in range(no_of_players):
        name = input("Name of a player: ")
        player = Player(name, deck.card_list)
        players.append(player)

    print("\nYou're gonna play against each other.\nLet's start!\n")

    # Drawing cards
    players_copy = players.copy()   # copy players list for additional operations
    counter = 0    # counter for decisions of y/n

    while counter != len(players):    # run until everybody says stop
        for player in players_copy:
            decision = input(f"\n{player.name}, do you wanna draw a card? [y/n] ")
            if decision == 'n':
                counter += 1
                print("\nYou don't draw any card.")
                print("Your hand:\n\t", player, sep='')
                print("Your points:", player.points)
                players_copy.remove(player)
            elif decision == 'y':
                print("\nYou draw a card.")
                player.draw_card()
                player.count_points()
                print("Your hand:\n\t", player, sep='')
                print("Your points:", player.points)
            else:
                print("\nType y/n!")

            if player.points == 21:
                winner = player.name    # player that gets 21 automatically wins
                break
            elif player.points > 21:
                print(f"{player.name}, you loose! Your score is over 21 points.")
                counter += 1
                players_copy.remove(player)

    # Game over
    print("\nThe game has ended!\nPlayers' final points:")
    winning_score = 0
    for player in players:   # setting a winner
        print(f"\t{player.name}: {player.points}")
        if player.points <= 21 and player.points > winning_score:
            winning_score = player.points
            winner = player.name
    print(f"\nThe winner is: {winner}!\nCongratulations!")


def main():
    game = Oczko()
    start_game(game)


if __name__ == '__main__':
    main()