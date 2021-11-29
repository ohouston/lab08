# testing File

from PlayerHand import Card, PlayerHand




'''
hand = PlayerHand()
hand.put('D', 'A')
hand.put('S', 'K')
hand.put('S', '2')
hand.put('C', 'Q')
hand.put('H', '7')
#print("Cards:", hand.getTotalCards())
hand.put('S', 'K')
hand.put('C', 'K')
print(hand.inOrder())
print(hand.preOrder())
#print(hand.delete('S', 'K'))
#print(hand.delete('S', 'K'))
#print(hand.inOrder())
#print(hand.preOrder())
#print(hand.getSuccessor('S', '2'))
'''

def testingMultiDef():
    #
    hand = PlayerHand()
    assert hand.isEmpty() == True
    assert hand.getTotalCards() == 0
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert str(hand.get('C', 'K')) == "C K | 1\n"
    assert hand.get('C', '8') == None
    assert hand.getTotalCards() == 7
    assert hand.isEmpty() == False
    assert hand.delete('S','K') == True
    assert hand.getTotalCards() == 6

testingMultiDef()



