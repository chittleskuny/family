#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name, is_male, father = None, mother = None):
        self.name = name
        self.is_male = is_male
        self.father = father
        self.mother = mother


class Unit:
    def __init__(self, husband, wifes: list, concubines: list, children: list):
        self.husband = husband
        self.wifes = wifes
        self.concubines = concubines
        self.children = children


    def __str__(self):
        return f'[{self.rank}] {self.husband}'
