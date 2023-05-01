#!/usr/bin/python3

import cheatdice
from cheatdice import Player
class cheater(Player):
    def cheat(self):
        self.dice[1] = 6
        self.dice[0] = 6
        self.dice[-1] = 6
