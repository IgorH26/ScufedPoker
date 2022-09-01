import sys
import csv
import random



class Deck:
    def __init__(self):
        format = { # dict created to make a printeable version of the cards
            2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K", 14:"A"
        }
        cards = []
        for i in range(2,15):
            cards.append({"color": "Clubs", "value": i, "print":f"{format[i]}♣"})
            cards.append({"color": "Diamonds", "value": i, "print":f"{format[i]}♦"})
            cards.append({"color": "Hearts", "value": i, "print":f"{format[i]}♥"})
            cards.append({"color": "Spades", "value": i, "print":f"{format[i]}♠"})

        random.shuffle(cards)
        self.cards = cards

    def __repr__(self):
        return f"{self.cards}"

    def __str__(self):
        return f"{self.cards}"

    def getStartHand(self):
        # gives cards to the player and the 3 AI players
        handPlayerOne = self.cards[0:5]

        handPlayerTwo = self.cards[5:10]

        handPlayerThree = self.cards[10:15]

        handPlayerFour = self.cards[15:20]

        new_deck = self.cards[20:]
        self.new_deck = new_deck


        return [handPlayerOne, handPlayerTwo, handPlayerThree, handPlayerFour]


    def getCards(self, c):
        return self.new_deck[0:len(c)]


def main():
    if len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("too few command-line arguments")
    name = sys.argv[1].capitalize()
    addPerson(name)
    player = Player(name)
    Pmoney = intro(player["wallet"])
    money = int(player["wallet"])
    print("#############################\n-     S  C  U   F  E  D     -\n-                           -\n-     P   O   K   E   R     -")
    print(f"-                           -\n-     Ur money: {Pmoney}     -")
    print("-                           -\n-                           -")
    input("-    press Enter to start   -")

    deck = Deck()
    hands = deck.getStartHand()
    yourHand = hands[0]
    yuri = hands[1]
    john = hands[2]
    alan = hands[3]
    yourHand.sort(key=get_value, reverse=True)
    yuri.sort(key=get_value, reverse=True)
    john.sort(key=get_value, reverse=True)
    alan.sort(key=get_value, reverse=True)




    """
    <<< 1r ROUND >>>

    the player can: raise
    TODO:
    - def RAISE, CALL, FOLD
    withdraw the money as its called

    """
    pot = 0
    npc = {
        0:"Player",
        1:"Yuri",
        2:"John",
        3:"Alan"
    }
    with open("SmallBlind.txt", 'r') as sb:
        for line in sb:
            if line[0] == "%":
                print(f"#  MONEY: ${money}")
            if line[0] == "$":
                bet = input("@: ").strip("$")
            else:
                print(line, end="")

    if bet == "":
        money -= 50
        newBalance(name, money)
        print("You are supposed to place more than $1\n# YOU ARE PENALIZED HAVE WITHDRAWN\n# $50 FROM YOUR ACCOUNT")
        sys.exit()
    bet = int(bet)
    if bet < 1:
        money -= 50
        newBalance(name, money)
        print("You are supposed to place more than $1\n# YOU ARE PENALIZED HAVE WITHDRAWN\n# $50 FROM YOUR ACCOUNT")
        sys.exit()
    elif not isinstance(bet, int):
        money -= 50
        newBalance(name, money)
        print("You are not supposed to place a float\n# YOU ARE PENALIZED HAVE WITHDRAWN\n# $50 FROM YOUR ACCOUNT")
        sys.exit()

    print("\n\n\n\n")
    pot += bet
    money -= bet
    bids = [bet,0,0,0]
    Round = 1
    turn = 1
    gameON = True
    yuriOut = False
    johnOut = False
    alanOut = False
    yourHandVal = checkHand(yourHand)
    YuriHand= checkHand(yuri)
    JohnHand = checkHand(john)
    AlanHand= checkHand(alan)
    while gameON:
        if yuriOut and johnOut and alanOut:

            money += pot
            newBalance(name, money)
            sys.exit("\n\nYou Win")
        if turn == 0: # YOUR TURN
            if Round == 1:
                with open("FirstRound.txt", 'r') as fr:
                    for line in fr:
                        if line[0] == "$":
                            if line[1:] == "hnd\n":
                                print("#   Your Hand: ", end="")
                                for i in yourHand:
                                    print(f"{i['print']}   ", end="")
                                print("\n#              ", end="")
                                for i in [0,1,2,3,4]:
                                    print(f" {i}   ", end="")

                                print("")
                            elif line[1:] == "pot\n":
                                printPot = f"${pot}{' '*(19-len(str(pot)))}"
                                i = 1

                                print(f"Alan            {printPot}Yuri")
                            elif line[1:] == "cash\n":
                                print(f"# MONEY: ${money}")
                            elif line[1:] == "discard\n":
                                discard = input("# DISCARD(separete the cards with \"/\"):").split("/")
                                if len(discard) > 4:
                                    sys.exit("Cannot discard more than 4 cards")
                                n = 0
                                if discard != [""]:
                                    for i in discard:
                                        if int(i) > 4:
                                            sys.exit("Cannot discard cards at an index supperior to 4")
                                newCards = deck.getCards(discard)

                                for i in range(5):
                                    if str(i) in discard:
                                        yourHand[i] = newCards[n]
                                        n += 1
                                yourHand.sort(key=get_value, reverse=True)
                                yourHandVal = checkHand(yourHand)

                                n = 0
                            else:
                                action = input("#: ").strip("$")
                                if action == '':
                                    newBalance(name, money)
                                    sys.exit("\n\nGOODBYE")



                                elif int(action) == 0:

                                    pot += highestBid(bids)
                                    bids[0] += highestBid(bids)
                                    money -= bids[0]
                                else:
                                    pot += highestBid(bids) + int(action)
                                    bids[0] += highestBid(bids) + int(action)
                                    money -= bids[0]
                        else:
                            print(line, end="")

                Round = 2
            else:
                with open("midGame.txt", 'r') as mg:
                    for line in mg:
                        if line[0] == "$":
                            if line[1:] == "hnd\n":
                                print("#    Your Hand: ", end="")
                                for i in yourHand:
                                    print(f"{i['print']}   ", end="")
                                print("\n#              ", end="")
                                for i in [0,1,2,3,4]:
                                    print(f" {i}   ", end="")
                                print("")
                            elif line[1:] == "cash\n":
                                print(f"# MONEY: ${money}")

                            elif line[1:] == "pot\n":
                                printPot = f"${pot}{' '*(19-len(str(pot)))}"
                                i = 1

                                print(f"Alan            {printPot}Yuri")
                            else:
                                action = input("#: ").strip("$")
                                if action == '':
                                    newBalance(name, money)
                                    sys.exit("\n\nGOODBYE")
                                elif action.lower() == 'check':
                                    if Max([yourHandVal, YuriHand, JohnHand, AlanHand]) == 0:
                                        money += pot
                                        newBalance(name, money)
                                        sys.exit("\n\nYou Win")
                                    elif Max([yourHandVal, YuriHand, JohnHand, AlanHand]) == 1:
                                        print("\n\n\n\n\nYou Lost, Yuri won")
                                        newBalance(name, money)
                                        sys.exit()
                                    elif Max([yourHandVal, YuriHand, JohnHand, AlanHand]) == 2:
                                        print("\n\n\n\n\nYou Lost, John won")
                                        newBalance(name, money)
                                        sys.exit()
                                    elif Max([yourHandVal, YuriHand, JohnHand, AlanHand]) == 3:
                                        print("\n\n\n\n\nYou Lost, Alan won")
                                        newBalance(name, money)
                                        sys.exit()
                                elif int(action) == 0:

                                    pot += highestBid(bids)
                                    bids[0] += highestBid(bids)
                                    money -= bids[0]
                                    newBalance(name, money)
                                elif int(action) != 0:
                                    pot += highestBid(bids) + int(action)
                                    bids[0] += highestBid(bids) + int(action)
                                    money -= bids[0]
                                    newBalance(name, money)
                        else:
                            print(line, end="")
            print("\n\n\n\n")
            turn = 1

        elif turn == 1: # YURI TURN
            yuriConfidance = confidance(YuriHand)
            if not yuriOut:
                if yuriConfidance == None:
                    print("\n\nYuri is out!")
                    yuriOut = True
                elif yuriConfidance == 0:
                    pot += highestBid(bids)
                    bids[1] += highestBid(bids)
                    print(f"\n\nYuri has CALLED(${highestBid(bids)})")
                else:
                    pot += highestBid(bids) + yuriConfidance
                    bids[1] += highestBid(bids) + yuriConfidance
                    print(f"\n\nYuri has RAISED BY ${yuriConfidance})")
            turn = 2
        elif turn == 2: # JOHN TURN
            johnConfidance = confidance(JohnHand)
            if not johnOut:
                if johnConfidance == None:
                    print("\n\nJohn is out!")
                    johnOut = True
                elif johnConfidance == 0:
                    pot += highestBid(bids)
                    bids[2] += highestBid(bids)
                    print(f"\n\nJohn has CALLED(${highestBid(bids)})")
                else:
                    pot += highestBid(bids) + johnConfidance
                    bids[2] += highestBid(bids) + johnConfidance
                    print(f"\n\nJohn has RAISED BY ${johnConfidance})")
            turn = 3
        else: # ALAN TURN
            alanConfidance = confidance(AlanHand)
            if not alanOut:
                if alanConfidance == None:
                    print("\n\nAlan is out!")
                    alanOut = True
                elif alanConfidance == 0:
                    pot += highestBid(bids)
                    bids[3] += highestBid(bids)
                    print(f"\n\nAlan has CALLED(${highestBid(bids)})")
                else:
                    pot += highestBid(bids) + alanConfidance
                    bids[3] += highestBid(bids) + alanConfidance
                    print(f"\n\nAlan has RAISED BY ${alanConfidance})")
            turn = 0




def highestBid(bids):
    return max(bids)


def Max(l):
    j = 0
    for i in l:
        if i == max(l):
            return j

        j += 1

def newBalance(person, balance):
    l = []

    with open("wallet.csv", "r") as copy:
        reader = csv.reader(copy)
        next(reader)
        for name, money in reader:
            if person == name:

                l.append({"name":name,"wallet":balance})
            else:
                l.append({"name":name,"wallet":money})


    file = open("wallet.csv", "w")
    file.write("person,money\n")
    for line in l:
        file.write(f"{line['name']},{line['wallet']}\n")
    file.close()







def confidance(i):
    if i == 10: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[1, 15, 25, 10])[0], None], weights=[35, 65, 0])[0]
    elif i == 9: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[1, 15, 25, 5])[0], None], weights=[45, 55, 0])[0]
    elif i == 8: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[5, 10, 20, 1])[0], None], weights=[45, 55, 0])[0]
    elif i == 7: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[5, 5, 5, 1])[0], None], weights=[65, 30, 5])[0]
    elif i == 6: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[50, 10, 1, 1])[0], None], weights=[75, 20, 5])[0]
    elif i == 5: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[50, 10, 1, 1])[0], None], weights=[70, 25, 5])[0]
    elif i == 4:
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[50, 10, 1, 1])[0], None], weights=[70, 25, 5])[0]
    elif i == 3:
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[5, 10, 20, 1])[0], None], weights=[55, 45, 10])[0]
    elif i == 2: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[5, 10, 20, 1])[0], None], weights=[50, 40, 10])[0]
    elif i == 1: ## DONE
        return random.choices([0, random.choices([10, 30, 50, 100], weights=[5, 10, 20, 1])[0], None], weights=[10, 5, 85])[0]

def checkHand(hand):
    if royalFlush(hand):
        return 10
    elif strFlush(hand):
        return 9
    elif fourOfKind(hand):
        return 8
    elif flush(hand):
        return 7
    elif full(hand):
        return 6
    elif straight(hand):
        return 5
    elif trio(hand):
        return 4
    elif doublePair(hand):
        return 3
    elif pair(hand):
        return 2
    return 1


def royalFlush(hand):
    n = 0
    for color in ["Clubs", "Diamonds", "Hearts", "Spades"]:
        for i in range(5):
            if hand[i]["value"] == 14-i and hand[i]["color"] == color:
                n += 1

        if n == 5:
            return True
        n = 0

    return False

def strFlush(hand):
    n = 0
    average = 0
    for card in hand:
        average  += card["value"]
    average = average/5
    suposedAverage = hand[2]["value"]
    for color in ["Clubs", "Diamonds", "Hearts", "Spades"]:


        for i in range(4):
            if hand[i]["value"] in get_cards(hand[(i+1):]):
                return False

        for i in range(5):
            if hand[i]["color"] == color:
                n += 1

        if n == 5 and suposedAverage == average:
            return True
        n = 0

    return False


def fourOfKind(hand):
    i = 0
    for val in range(2, 15):
        for card in hand:
            if card["value"] == val:
                i += 1

        if i == 4:
            return True
        i = 0

    return False



def flush(hand):
    n =0
    for color in ["Clubs", "Diamonds", "Hearts", "Spades"]:
        for card in hand:
            if card["color"] == color:
                n += 1

        if n == 5:
            return True
        n = 0

    return False


def full(hand):
    if trio(hand) and pair(hand):
        return True
    return False


def straight(hand):
    average = 0
    for card in hand:
        average  += card["value"]
    average = average/5
    suposedAverage = hand[2]["value"]

    for i in range(4):
        if hand[i]["value"] in get_cards(hand[(i+1):]):
            return False

    if suposedAverage == average:
        return True


    return False

def trio(hand):
    i = 0
    for val in range(2, 15):
        for card in hand:
            if card["value"] == val:
                i += 1

            if i == 3:
                return True
        i = 0

    return False


def doublePair(hand):
    firstPairValue = 0
    i = 0
    for val in range(2, 15):
        for card in hand:
            if card["value"] == val:
                i += 1


        if i == 2:
            firstPairValue = val
            firstPair = True
        i = 0

    i = 0
    for val in range(2, 15):
        for card in hand:
            if card["value"] == val and val != firstPairValue:
                i += 1

        if i == 2:
            return True
        i = 0

    return False


def pair(hand):
    i = 0
    for val in range(2, 15):
        for card in hand:
            if card["value"] == val:
                i += 1

        if i == 2:
            return True
        i = 0

    return False






def SmallBlind(n):
    return n-1 if n != 0 else 4

def get_color(color):
    return color.get('color')

def get_value(value):
    return value.get('value')

def get_cards(cards):
    l = []
    for i in cards:
        l.append(i["value"])

    return l

def getInfo():

    l = []

    with open("wallet.csv", "r") as before:
        reader = csv.reader(before)
        next(reader)
        for name, money in reader:
            l.append({"name":name,"wallet":money})

    return l

def addPerson(person):
    f = getInfo()
    for line in f:
        if line["name"] == person:
            return False
    with open("wallet.csv", 'a') as newP:
        newP.write(f"{person},500\n")

def Player(person):
    f = getInfo()
    for line in f:
        if line["name"] == person:
            return line

def intro(money):
    l = len(money)
    spaces = 6 - l
    return "$"+money + " "*spaces


if __name__ == "__main__":
    main()
