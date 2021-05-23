#
# @file Character.py
# @author Mayuki
#

class Character:

    def __init__(self):
        self._status = {
            "HP" : 0,
            "Attack" : 0,
            "Defence" : 0,
            "SpAttack" : 0,
            "SpDefence" : 0,
            "Speed" : 0
        }
    #def __init__

    def set_status(self, hash_value):
        self._status = hash_value
    #def set_status

    def get_hp(self):
        return self._status["HP"]
    #def get_hp

if __name__ == '__main__':
    pass
