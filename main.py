from library import player as ply
from library import game as gm
from matplotlib import pyplot as plt
import numpy as np

def main() :

    player = ply.Player()
    game = gm.Game()
    game.set_random_seed(0)

    rounds = []
    maxcap = []
    
    for i in range(1000000) :
        player.set_init_capital(100)
        game.initialize(player)
        game.set_init_stake(1)

        while game.is_on() :
            game.next_round()

        rounds.append(np.log10(game.get_no_rounds()))
        maxcap.append(np.log10(player.get_max_capital()))
        # print("Final stake:", game.get_stake(), " cannot be paid. Game ended")
        # print("Rounds until loss:", game.get_no_rounds())
        # print("Maximum Capital:", player.get_max_capital(), "in round", game.get_round_of_max_capital())

    plt.hist(rounds,bins=100,histtype='step')
    plt.yscale('log')
    plt.title("start capital: "+str(player.get_init_capital())+", stake: "+str(game.get_init_stake()))
    plt.xlabel('log10(rounds)')
    plt.ylabel('Entries')
    plt.savefig("rounds.pdf")

    plt.clf()
    
    plt.hist(maxcap,bins=100,histtype='step')
    plt.yscale('log')
    plt.title("start capital: "+str(player.get_init_capital())+", stake: "+str(game.get_init_stake()))
    plt.xlabel('log10(max. capital)')
    plt.ylabel('Entries')
    plt.savefig("maxcap.pdf")

if __name__ == "__main__" :
    main()
