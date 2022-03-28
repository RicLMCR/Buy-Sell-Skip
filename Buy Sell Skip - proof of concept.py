from random import randint

# 2 dimensional list containg: name of corp | # of shares | value of shares
companies = [
['Pear Inc', 100, 80 ],
['Eye Bee Emma',200, 40],
['Jiggle', 200, 20],
['Motor',100, 70]]

myshares = []
mycash = 200

day = 1
shareval = 0
value_adj = randint(90,100)
incr_decr = 0
buy_sell = None # **************

# determine if share value increases or decreases
def rand_change():
    global incr_decr
    incr_decr = randint(0,1)
    return incr_decr

# increase/decrease share value by random amount between 1% and 10%
def share_change():
    global incr_decr
    global shareval

    for row in companies:
        rand_change()
        print ('------------------------------------------------------------')
        if incr_decr > 0:
            print (f'The previous share value of {row[0]} was {row[2]}')
            shareval = ((row[2] / value_adj)*100)
            row.pop(2)
            row.insert(2, shareval)
            print (f'The share value has increased to:{shareval}')
        else:
            print (f'The previous share value of {row[0]} was {row[2]}')
            shareval = ((row[2] * value_adj)/100)
            row.pop(2)
            row.insert(2, shareval)
            print (f'The share value has decreased to:{shareval}')
    
    return (shareval)

# End the current trading day and start the next day
def day_count():
    global day

    print (f'These are the figures for trading day number:{day}')
    day +=1
    share_change()
    next_day = input('\nDo you want to move to the next day? Y/N\n')
    next_day = next_day.upper()
    if next_day == 'Y':
        day_count()

day_count()
