
# main function which finds the change required
# change is ammount that must be created using coin denominations
def give_change(change, denominations):

    #special case
    if change == 0:
        return 0
    
    #check if the problem is even solvable
    if change < min(denominations):
        raise Exception("Change cannot be created using avaiable denominations!")
    
    memowization = [-1] * (change + 1)
    memowization[0] = 0
    num_coins = g_change(change, denominations, memowization)
    if num_coins < 0:
        raise Exception("I have no idea how this could happen")
    return num_coins

#recursive function c is change left, d is denominations and m is the array used for momowization
def g_change(c, d, m):
    #If a solution has already been found then use that
    if m[c] != -1:
        return m[c]
    elif c < min(d):
        #returns a large number so it is not selected as an answer
        return 100000000
    else:
        #saves the min solution
        m[c] = min([g_change(c-coin, d, m) + 1 for coin in d if c >= coin])
        return m[c]


# Tests give change to see if the output is normal
def test_give_change():
    print(give_change(40, [1, 10, 20, 25]))
 
    try:
        print(give_change(9, [10, 20, 25] ))
    except Exception as e:
        print(e)

    print(give_change(80, [10, 20, 25] ))

    print(give_change(0, [10, 20, 25] ))


test_give_change()
