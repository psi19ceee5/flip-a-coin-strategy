from library import player as ply
from library import game as gm

def main() :

    player = ply.Player()
    player.set_init_capital(3)
    print("The player starts with",  player.get_capital(), "coin(s)");

    game = gm.Game()
    game.initialize(player)
    game.set_init_stake(1)
    game.set_random_seed(0)

    while game.is_on() :
        game.next_round()
        print("Capital after round "+str(game.get_no_rounds())+":", player.get_capital())

    print("Final stake:", game.get_stake(), " cannot be paid. Game ended")
    print("Rounds until loss: ", game.get_no_rounds())

if __name__ == "__main__" :
    main()
