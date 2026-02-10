"""
--- DECK & SHUFFLING MECHANICS ---

This module implements card deck creation, shuffling, and dealing mechanics
for a Texas Hold'em poker game.

Its goals are:
- Generate a standard 52-card deck
- Deal two-card hands to a human player and a bot
- Reveal community cards (flop, turn, and river)

All card draws are random and modify the shared deck in place.
"""
# Import statement
import random

def Deck():
    """
    Creates and returns a standard 52-card deck.

    Each card is represented as a string containing its rank and suit,
    for example: "A ♠️" or "10 ♦️".
    Input: None

    Outputs:
        DECK (list[str]): A list of 52 unique card strings representing a full deck.
    """
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suit = ["♦️", "♥️", "♣️", "♠️"]

    # Creating a deck of cards (all combinations of ranks and suits)
    DECK = []
    for choice1 in rank:
        for choice2 in suit:
            DECK.append(f"{choice1} {choice2}")
    return DECK

def Hand(DECK):
    """
    Draws two random cards from the deck for the player.

    The drawn cards are removed from the deck to prevent duplication.

    Input:
        DECK (list[str]): The current deck of cards.

    Output:
        hand (list[str]): A list containing two card strings representing
                   the player's hand.
    """
    hand = []     # Hand of cards
    # Draw 2 cards
    for time in range(2):
        card = random.choice(DECK)
        hand.append(card)
        DECK.remove(card)
    return hand

"""
RIVER CARDS
"""
def flop(DECK):
    """
    Reveals the flop by drawing three community cards from the deck.

    The drawn cards are removed from the deck and shared by both players.

    Input:
        DECK (list[str]): The current deck of cards.

    Output:
        community_card (list[str]): A list of three card strings representing the flop.
    """
    community_card = []     # 3 community cards 

    # Draw 3 cards
    for time in range(3):
        ccard = random.choice(DECK)
        community_card.append(ccard)
        DECK.remove(ccard)
    return community_card

def newrivercard(DECK):
    """
    Draws a single community card from the deck.

    This function is used for both the turn (4th card) and river (5th card).

    The drawn card is removed from the deck.

    Input:
        DECK (list[str]): The current deck of cards.

    Output:
        rcard (str): A card string representing the newly revealed community card.
    """
    rcard = random.choice(DECK)
    DECK.remove(rcard)
    return rcard