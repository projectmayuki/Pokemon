#
# @file BattleSceneSample.py
# @author Mayuki
#

from BattleLogic import Character

class BattleSimulator:

    def __init__(self):
        pass
    # def __init__

    def battle(self):
        print("Battle")
    # def battle

if __name__ == '__main__':

    simulator = BattleSimulator()
    simulator.battle()
    
    chara1 = Character.Character()
    chara1.set_status({"HP" : 73, "Attack" : 67, "Defence" : 75, "SpAttack" : 81, "SpDefence" : 100, "Speed" : 109})
    print(chara1.get_hp())
