#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main file of pyCFG2Chomsky. """

import sys

from cfg import ContextFreeGrammar as CFG

if __name__ == '__main__':
    myCFG = CFG(sys.stdin)
    print "End of input.\n\nCFG\nRules:"
    print myCFG.rules
    print "Terminals:"
    print myCFG.terminals
    print "Nonterminals:"
    print myCFG.nonterminals
    myCFG.transform_to_Chomsky()
    print "\nChomsky Normal Form Grammar\nRules:"
    print myCFG.rules
    print "Terminals:"
    print myCFG.terminals
    print "Nonterminals:"
    print myCFG.nonterminals
