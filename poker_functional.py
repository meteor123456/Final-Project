#takes in a list of 5 integers and returns the decimal value of the 8-bit binary()
def evaluatehand(hand: list):
    hand.sort(reverse=True);

    if Royal(hand):
        return Royal(hand)
    
    elif StraightFlush(hand):
        return StraightFlush(hand)
    
    elif Four(hand):
        return Four(hand)
 
    elif FullHouse(hand):
        return FullHouse(hand)
    
    elif Flush(hand):
        return Flush(hand);
    
    elif Straight(hand):
        return Straight(hand)
    
    elif Three(hand):
        return Three(hand)
    
    elif TwoPairs(hand):
        return TwoPairs(hand)
    
    elif Pair(hand):
        return Pair(hand)

    else:
        return HighCard(hand);


#All these function assumes the hand is sorted from greatest to least. 

#Returns value of the hand if Royal Flush, 0 if not. 
def Royal(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))     #binary list of only the rank values of the hand
    suits = list ( map ( lambda x: x&0b11, hand))   #binary list of only the suits of the hand

    if  len(set(suits)) != 1:           #not flush
        return 0
    if ranks[0] != 0b1100:              #highest is not Ace
        return 0 
    if (ranks[0] == ranks[1] + 1) and (ranks[0] == ranks[2] + 2) and (ranks[0] == ranks[3] + 3) and (ranks[0] == ranks[4] + 4):  #Check Straight
        binhandrank = 0b1001
        binhighcard = ranks[0];
        binvalue = (binhandrank << 4) | binhighcard
        
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
        binvalue = (binhandrank << 4) | binhighcard
        
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
        binvalue = (binhandrank << 4) | binhighcard
        
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
    binvalue = (binhandrank << 4) | binhighcard
    
    return binvalue


#Returns value of the hand if Flush, 0 if not. 
def Flush(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))
    suits = list ( map ( lambda x: x&0b11, hand))

    if  len(set(suits)) == 1:           #flush
        binhandrank = 0b0101
        binhighcard = ranks[0];
        binvalue = (binhandrank << 4) | binhighcard
        
        return binvalue
    return 0
  

#Returns value of the hand if Straight, 0 if not. 
def Straight(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))
    if (ranks[0] == ranks[1] + 1) and (ranks[0] == ranks[2] + 2) and (ranks[0] == ranks[3] + 3) and (ranks[0] == ranks[4] + 4): #Check Straight
        binhandrank = 0b0100
        binhighcard = ranks[0]
        binvalue = (binhandrank << 4) | binhighcard
        
        return binvalue
    return 0

#Returns value of the hand if Three of a Kind, 0 if not. 
def Three(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))

    binhighcard = ranks[2]      
    highcount = ranks.count(binhighcard)
    if highcount != 3:          #check for 3 of a kind
        return 0
    if len (set (ranks)) == 3:  #check if the two other cards are different.
        binhandrank = 0b0011
        binvalue = (binhandrank << 4) | binhighcard
        
        return binvalue
    return 0

#Returns value of the hand if Two Pairs, 0 if not. 
def TwoPairs(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))

    rank1 = ranks[1]
    rank2 = ranks[3]
    count1 = ranks.count(rank1)
    if count1 != 2:
        return 0
    count2 = ranks.count(rank2)
    if count2 != 2:
        return 0
    binhandrank = 0b0010
    binhighcard = ranks[1]
    binvalue = (binhandrank << 4) | binhighcard
    
    return binvalue

#Returns value of the hand if One Pair, 0 if not. 
def Pair(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))

    counts = [ranks.count(x) for x in ranks ]

    if counts.count(2)/2 != 1: #only one instance of 2 should exist, divide by two for double counting
        return 0
    else:
        binhighcard = ranks[counts.index(2)]
        binhandrank = 0b0001
        binvalue = (binhandrank << 4) | binhighcard
        return binvalue

  

#Returns value of the hand if High Card, 0 if not. 
def HighCard(hand: list):
    ranks = list ( map ( lambda x: x>>2, hand))
    if len (set (ranks)) == 5:
        binhandrank = 0b0000
        binhighcard = ranks[0]
        binvalue = (binhandrank << 4) | binhighcard
        
        return binvalue
    return 0

#converts list of string into list of binary values
def strlist2binarylist(hand: list):
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
    binlist = [ (rank2bin[s[:-1]]<<2)|suit2bin[s[-1]] for s in hand  ]
    
    return binlist

#compares two given string lists of a hand. Returns a string denoting the more valuable hand.
def compareHandStr(hand1:list, hand2:list):
    hand1_bin = strlist2binarylist(hand1)
    hand2_bin = strlist2binarylist(hand2)

    val1 = evaluatehand(hand1_bin);
    val2 = evaluatehand(hand2_bin);
    print("Hand 1 value: " + str(bin(val1)) + " " + str(val1));
    print("Hand 2 value: " + str(bin(val2)) + " " + str(val2));
    if val1 > val2:
        return("Hand 1 wins!")
    elif val1 < val2:
        return("Hand 2 wins!")
    else:
        return("Tie")