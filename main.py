import random

tarot = {1:	 "The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor",
         5:  "The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit",
         10: "Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance",
         15: "The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement",
         21: "The World", 22: "The Fool"}
times = ["past", "present", "future"]


def spread_cards():
    spread = {}
    numbers = []
    while len(numbers) < 3:
        # gets the 3 random keys for the cards in the spread, and checks for duplicates
        new_number = random.randint(1, len(tarot))
        if new_number not in numbers:
            numbers.append(new_number)
    for x in range(0, 3):
        # make a new dict with "past" "present" or "future" and the associated randomly drawn card
        spread[times[x]] = tarot[numbers[x]]
    for x, y in spread.items():
        print("Your {key} is the {value} card.".format(key=x, value=y))


spread_cards()


