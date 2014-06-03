#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main file of pyCFG2Chomsky. """

import sys

from additional import sort_and_deduplicate as sdedup

class ContextFreeGrammar(object):

    def __init__(self, file_of_rules):
        self.rules = []
        self.terminals = set()
        self.nonterminals = set()
        for line in file_of_rules:
            self.add_rule(line[:-1])

    def add_rule(self, rule_str):
        divide = rule_str.split("->")
        left = divide[0].strip()
        self.nonterminals.add(left)
        right = self._divide_right_(divide[1].strip())
        self.rules.append((left, right))

    def print_rules(self):
        for rule in self.rules:
            prt_val = "" + rule[0] + " -> "
            for elem in rule[1]:
                prt_val += elem + " "
            print prt_val[:-1]

    def _divide_right_(self, right):
        tab = right.split(" ")
        for itera in range(len(tab)):
            if (len(tab[itera]) == 1) or (tab[itera] == "ε"):
                self.terminals.add(tab[itera])
            else:
                self.nonterminals.add(tab[itera])
        return tab

    def transform_to_Chomsky(self):
        self._remove_eps_()
        self._transform_terminals_()
        to_del = []
        for rule in self.rules:
            if _is_unary_chain_rule_(rule):
                self._transform_chain_rule_(rule)
                to_del += [rule]
        for rule in to_del:
            self.rules.remove(rule)
        biter = len(self.nonterminals)
        for rule in self.rules:
            if _is_too_long_rule_(rule):
                self._break_rule_(rule, len(self.nonterminals) - biter)
        to_del = []
        for rule in self.rules:
            if len(rule[1]) > 2:
                to_del += [rule]
        for rule in to_del:
            self.rules.remove(rule)

    def _remove_eps_(self):
        to_del = [rule for rule in self.rules if rule[1] == ["ε"]]
        for rule in to_del:
            self.rules.remove(rule)
        self.terminals.remove("ε")

    def _transform_terminals_(self):
        for term in self.terminals:
            checklist = [elem for elem in self.rules if (term in elem[1]) and (len(elem[1])>1)]
            if len(checklist) > 0:
                nonterm = "@" + term
                self.nonterminals.add(nonterm)
                for rule in self.rules:
                    for iterator in range(len(rule[1])):
                        if rule[1][iterator] == term:
                            rule[1][iterator] = nonterm
                self.rules.append((nonterm, [term]))

    def _transform_chain_rule_(self, rule):
        left = rule[0]
        rnterm = rule[1][0]
        goodrules = [rl for rl in self.rules if rl[0] == rnterm]
        for groole in goodrules:
            self.rules.append((left, groole[1]))

    def _break_rule_(self, rule, biter):
        left = rule[0]
        rfterm = rule[1][0]
        roterms = rule[1][1:]
        existing = [text for text in self.rules if text[1]==roterms]
        if len(existing) == 0:
            biterm = "@@" + str(biter)
            self.nonterminals.add(biterm)
            self.rules.append((biterm, roterms))
        else:
            biterm = existing[0][0]
        self.rules.append((left, [rfterm, biterm]))

def _is_unary_chain_rule_(rule):
    if len(rule[1]) == 1:
        return len(rule[1][0]) > 1
    return False

def _is_too_long_rule_(rule):
    return len(rule[1]) > 2
