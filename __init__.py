#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main file of pyCFG2Chomsky. """

import sys

from cfg import ContextFreeGrammar as CFG

if __name__ == '__main__':
    myCFG = CFG(sys.stdin)
    print "End of input."
    myCFG.transform_to_Chomsky()
    # print "\nChomsky Normal Form Grammar\nRules:"
    myCFG.print_rules()
    # print "Terminals:"
    # for term in myCFG.terminals:
        # print term
    # print "Nonterminals:"
    # print myCFG.nonterminals
