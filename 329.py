# 860. Lemonade Change. Easy. 50.8%.

# At a lemonade stand, each lemonade costs $5. 

# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

# Note that you don't have any change in hand at first.

# Return true if and only if you can provide every customer with correct change.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for c in bills:
            if c == 5:
                five += 1
            elif c == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
