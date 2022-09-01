from project import royalFlush, strFlush, straight, flush, trio, fourOfKind, pair, full, doublePair

def test_royalFlush1():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Spades", "value": 13, "print":f"K♠"},
        {"color": "Clubs", "value": 12, "print":f"Q♣"},
        {"color": "Spades", "value": 11, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert royalFlush(hand) == False


def test_royalFlush2():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Spades", "value": 13, "print":f"K♠"},
        {"color": "Spades", "value": 12, "print":f"Q♠"},
        {"color": "Spades", "value": 11, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert royalFlush(hand) == True


def test_royalFlush3():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Spades", "value": 7, "print":f"7♠"},
        {"color": "Spades", "value": 12, "print":f"Q♠"},
        {"color": "Spades", "value": 11, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert royalFlush(hand) == False


def test_strFlush1():
    hand = [
        {"color": "Spades", "value": 10, "print":f"10♠"},
        {"color": "Spades", "value": 9, "print":f"9♠"},
        {"color": "Spades", "value": 8, "print":f"8♠"},
        {"color": "Spades", "value": 7, "print":f"7♠"},
        {"color": "Spades", "value": 6, "print":f"6♠"}
    ]
    assert strFlush(hand) == True


def test_strFlush2():
    hand = [
        {"color": "Spades", "value": 10, "print":f"10♠"},
        {"color": "Spades", "value": 10, "print":f"9♠"},
        {"color": "Spades", "value": 8, "print":f"8♠"},
        {"color": "Spades", "value": 6, "print":f"7♠"},
        {"color": "Spades", "value": 6, "print":f"6♠"}
    ]
    assert strFlush(hand) == False


def test_strFlush3():
    hand = [
        {"color": "Clubs", "value": 10, "print":f"10♣"},
        {"color": "Spades", "value": 9, "print":f"9♠"},
        {"color": "Spades", "value": 8, "print":f"8♠"},
        {"color": "Spades", "value": 7, "print":f"7♠"},
        {"color": "Spades", "value": 6, "print":f"6♠"}
    ]
    assert strFlush(hand) == False


def test_straight1():
    hand = [
        {"color": "Spades", "value": 10, "print":f"10♠"},
        {"color": "Spades", "value": 10, "print":f"9♠"},
        {"color": "Spades", "value": 8, "print":f"8♠"},
        {"color": "Clubs", "value": 6, "print":f"7♣"},
        {"color": "Spades", "value": 6, "print":f"6♠"}
    ]
    assert straight(hand) == False


def test_straight2():
    hand = [
        {"color": "Clubs", "value": 10, "print":f"10♣"},
        {"color": "Spades", "value": 9, "print":f"9♠"},
        {"color": "Spades", "value": 8, "print":f"8♠"},
        {"color": "Spades", "value": 7, "print":f"7♠"},
        {"color": "Spades", "value": 6, "print":f"6♠"}
    ]
    assert straight(hand) == True


def test_Flush1():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Spades", "value": 9, "print":f"9♠"},
        {"color": "Spades", "value": 12, "print":f"Q♠"},
        {"color": "Spades", "value": 11, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert flush(hand) == True


def test_Flush2():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 9, "print":f"9♣"},
        {"color": "Spades", "value": 12, "print":f"Q♠"},
        {"color": "Spades", "value": 11, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert flush(hand) == False


def test_4ofKind1():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 14, "print":f"Q♠"},
        {"color": "Hearts", "value": 14, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert fourOfKind(hand) == True



def test_4ofKind2():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 14, "print":f"Q♠"},
        {"color": "Hearts", "value": 12, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert fourOfKind(hand) == False



def test_trio1():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 14, "print":f"Q♠"},
        {"color": "Hearts", "value": 12, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert trio(hand) == True


def test_trio2():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 11, "print":f"Q♠"},
        {"color": "Hearts", "value": 12, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert trio(hand) == False

def test_pair1():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 13, "print":f"Q♠"},
        {"color": "Hearts", "value": 12, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert pair(hand) == True

def test_pair2():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 13, "print":f"9♣"},
        {"color": "Diamonds", "value": 12, "print":f"Q♠"},
        {"color": "Hearts", "value": 11, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert pair(hand) == False

def test_pair3():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 13, "print":f"9♣"},
        {"color": "Diamonds", "value": 13, "print":f"Q♠"},
        {"color": "Hearts", "value": 12, "print":f"J♠"},
        {"color": "Spades", "value": 10, "print":f"10♠"}
    ]
    assert pair(hand) == True


def test_full1():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 13, "print":f"Q♠"},
        {"color": "Hearts", "value": 13, "print":f"J♠"},
        {"color": "Spades", "value": 13, "print":f"10♠"}
    ]
    assert full(hand) == True


def test_full2():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 13, "print":f"Q♠"},
        {"color": "Hearts", "value": 13, "print":f"J♠"},
        {"color": "Spades", "value": 12, "print":f"10♠"}
    ]
    assert full(hand) == False





def test_doublePair1():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 13, "print":f"Q♠"},
        {"color": "Hearts", "value": 13, "print":f"J♠"},
        {"color": "Spades", "value": 1, "print":f"10♠"}
    ]
    assert doublePair(hand) == True

def test_doublePair2():
    hand = [
        {"color": "Spades", "value": 14, "print":f"A♠"},
        {"color": "Clubs", "value": 14, "print":f"9♣"},
        {"color": "Diamonds", "value": 13, "print":f"Q♠"},
        {"color": "Hearts", "value": 12, "print":f"J♠"},
        {"color": "Spades", "value": 1, "print":f"10♠"}
    ]
    assert doublePair(hand) == False