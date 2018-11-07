import random


class battle:
#    PA = player.getAtk()
#    EA = enemy.getAtk()

    def main(self, player, enemy):
        while(True):
            if(player.getHit() <= 0 or enemy.getHit() <= 0):
                return
            self.PlayerTurn(player, enemy)
            self.EnemyTurn(player, enemy)

    def PlayerTurn(self, player, enemy):
        while(True):
            opt = raw_input('1)Attack\n2)Run\n')
            num = ['0','1','2','3','4','5','6','7','8','9']
            if(opt in num):
                opt = int(opt)
                break
            else:
                print("invalid input")
        if (opt == 1):
            dmg = player.getAtk() + random.randint(1,3)
            enemy.setHit(dmg)
            print("Enemy Hp Remaining: "+ str(enemy.getHit()))
    def EnemyTurn(self, player, enemy):
        dmg = enemy.getAtk() + random.randint(0,5)
        player.setHit(dmg)
        print("The player has: " + str(player.getHit()) + " left")
        return
