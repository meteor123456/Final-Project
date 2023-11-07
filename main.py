

#takes in a list of 5 integers and returns the decimal value of the 8-bit binary()
def evaluatehand(hand: list):
    hand.sort(reverse=True);
    value = Royal(hand);
    if value:
        return value
    else:
        value = StraightFlush(hand);
    
    if value:
        return value
    else:
        value = Four(hand);
    
    if value:
        return value
    else:
        value = FullHouse(hand);
    
    if value:
        return value
    else:
        value = Flush(hand);
    
    if value:
        return value
    else:
        value = Straight(hand);

    if value:
        return value
    else:
        value = Three(hand);
    
    if value:
        return value
    else:
        value = TwoPairs(hand);
    
    if value:
        return value
    else:
        value = Pair(hand);

    if value:
        return value
    else:
        value = HighCard(hand);

    return value;



#All these function assumes the hand is sorted from greatest to least. 

#Returns value of the hand if Royal Flush, 0 if not. 
def Royal(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))
    suits = list ( map ( lambda x: x&0b11, hand))

    if  len(set(suits)) != 1:           #not flush
        return 0
    if ranks[0] != 0b1100:              #highest is not Ace
        return 0 
    if (ranks[0] == ranks[1] + 1) and (ranks[0] == ranks[2] + 2) and (ranks[0] == ranks[3] + 3) and (ranks[0] == ranks[4] + 4):  #Check Straight
        binhandrank = 0b1001
        binhighcard = ranks[0];
        binvalue = binhandrank << 4
        binvalue = binvalue | binhighcard
        return binvalue
    return 0

#Returns value of the hand if Straight Flush, 0 if not. 
def StraightFlush(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))
    suits = list ( map ( lambda x: x&0b11, hand))

    if  len(set(suits)) != 1:           #not flush
        return 0
    if (ranks[0] == ranks[1] + 1) and (ranks[0] == ranks[2] + 2) and (ranks[0] == ranks[3] + 3) and (ranks[0] == ranks[4] + 4): #Check Straight
        binhandrank = 0b1000
        binhighcard = ranks[0]
        binvalue = binhandrank << 4
        binvalue = binvalue | binhighcard
        return binvalue
    return 0

#Returns value of the hand if Four of a Kind, 0 if not. 
def Four(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))

    binhighcard = ranks[1]      
    highcount = ranks.count(binhighcard)
    if highcount != 4:          #check for 4 of a kind
        return 0
    else:
        binhandrank = 0b0111
        binvalue = binhandrank << 4
        binvalue = binvalue | binhighcard
        return binvalue

    

#Returns value of the hand if FullHouse, 0 if not. 
def FullHouse(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))

    binhighcard = ranks[2]      
    highcount = ranks.count(binhighcard)
    if highcount != 3:          #check for 3 of a kind
        return 0

    if ranks[2] != ranks[0]:
        alt_high = ranks[0]
    elif ranks[2] != ranks[4]:
        alt_high = ranks[4]
    altcount = ranks.count(alt_high)
    if altcount != 2:           #checks for other pair
        return 0
    
    binhandrank = 0b0110
    binvalue = binhandrank << 4
    binvalue = binvalue | binhighcard
    return binvalue


#Returns value of the hand if Flush, 0 if not. 
def Flush(hand: list):
    return 0

#Returns value of the hand if Straight, 0 if not. 
def Straight(hand: list):
    return 0

#Returns value of the hand if Three of a Kind, 0 if not. 
def Three(hand: list):
    return 0

#Returns value of the hand if Two Pairs, 0 if not. 
def TwoPairs(hand: list):
    return 0

#Returns value of the hand if One Pair, 0 if not. 
def Pair(hand: list):
    return 0

#Returns value of the hand if High Card, 0 if not. 
def HighCard(hand: list):
    return 0

#converts list of string into list of binary values
def str2binarylist(hand: str):
    strlist = hand.split(" ")
    binlist = [];
    suit2bin = {
        "C" : 0b00,
        "D" : 0b01,
        "H" : 0b10,
        "S" : 0b11
    }
    rank2bin = {
        "2" : 0b0000,
        "3" : 0b0001,
        "4" : 0b0010,
        "5" : 0b0011,
        "6" : 0b0100,
        "7" : 0b0101,
        "8" : 0b0110,
        "9" : 0b0111,
        "10": 0b1000,
        "J" : 0b1001,
        "Q" : 0b1010,
        "K" : 0b1011,
        "A" : 0b1100
    }

    for s in strlist:
        binsuit = suit2bin[s[-1]];
        binrank = rank2bin[s[:-1]];
        finalbin = binrank << 2;
        finalbin = finalbin | binsuit
        binlist.append(finalbin)
    
    return binlist

def main():
    hand1 = str(input("Input first hand:\n"));
    hand2 = str(input("Input second hand:\n"));
    hand1_bin = str2binarylist(hand1)
    hand2_bin = str2binarylist(hand2)

    val1 = evaluatehand(hand1_bin);
    val2 = evaluatehand(hand2_bin);
    print("Hand 1 value: " + str(bin(val1)));
    print("Hand 2 value: " + str(bin(val2)));
    if val1 > val2:
        print("Hand 1 wins!")
    elif val1 < val2:
        print("Hand 2 wins!")
    else:
        print("Tie")

main();