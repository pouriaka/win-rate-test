import random
import matplotlib.pyplot as plt
import numpy as np


def trade(winrate, Reward_Risk, equity, volum_list, number_trades, plot=True):
    # Win rate shuld be between 0 to 100 percent
    
    equity_list = []
    volum_number = 0
    back_to_back_loss = 0
    back_to_back_loss_list = []
    volum_choice = []
    winrate_list = []

    # Creat winrate list
    for number in range(int(winrate * 10)):
        winrate_list.append(1)

    for number in range(1000 - int(winrate * 10)):
        winrate_list.append(-1)

    # Simulate trading
    for i in range(number_trades):
        trade = random.choice(winrate_list)
        #print("trade :", trade)

        if trade == 1:
            equity += trade * volum_list[volum_number] * Reward_Risk 
            equity_list.append(equity)
            volum_choice.append(volum_list[volum_number])
            #print("equity:", equity)
            #print("volum", volum_list[volum_number])
            volum_number = 0
            back_to_back_loss = 0 
            back_to_back_loss_list.append(back_to_back_loss)

        else:
            equity += trade * volum_list[volum_number]
            equity_list.append(equity)
            volum_choice.append(volum_list[volum_number])
            #print("equity:", equity)
            #print("volum", volum_list[volum_number])
            back_to_back_loss += 1 
            back_to_back_loss_list.append(back_to_back_loss)

            if volum_number == len(volum_list) - 1:
                volum_number = 0
            else:
                volum_number += 1 

    if plot:
        print(equity_list)   
        plt.plot(equity_list)
        plt.show()

        #plt.plot(volum_choice)
        #plt.show()

        plt.plot(back_to_back_loss_list)
        plt.show()

    return back_to_back_loss_list, equity_list


# RR = 1
#volum_list = [1, 2, 4, 8]
# RR = 2
volum_list = [1, 1 , 2, 3 , 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]
# RR = 3
#volum_list = [1, 1, 1, 2, 2, 3, 4, 5]
# RR = 3
#volum_list = [1, 1, 2, 2, 3, 4, 5]
# RR = 1.5
#volum_list = [1, 1, 2, 3, 5]

#trade(50, 2, 0, volum_list, 100, plot=True)


"""
# Repet the simulation
max_back_to_back_loss_list = []
final_equity_list = []

for traders in range(10000):
    trader_back_to_back_loss, equity_list = trade(33, 2, 0, volum_list, 1000, plot=False)
    max_back_to_back_loss_list.append(max(trader_back_to_back_loss))
    final_equity_list.append(max(equity_list))



plt.plot(sorted(max_back_to_back_loss_list))
plt.show()

plt.plot(sorted(final_equity_list))
plt.show()

"""
def calculate_average(lst):
    if not lst:
        return None  # Return None for an empty list to avoid division by zero

    # Calculate the average
    average = sum(lst) / len(lst)
    return average

#print(calculate_average(max_back_to_back_loss_list))
#trader_back_to_back_loss, equity_list = trade(50, 1, 0, volum_list, 1000, plot=True)

for i in range(10):
    trader_back_to_back_loss, equity_list = trade(32.4, 2, 1000, volum_list, 700, plot=False)
    plt.plot(equity_list)

plt.show()
# For always profitable 
# RR = 1 ---- 56% win rate
# RR = 2 ---- 39% win rate
# RR = 3 ---- 30% win rate