# -*- coding: utf-8 -*-

class 植物基类(object):
    picture = None 
    card_picture = None  
    name = 'cwx'
    x = 0
    y = 0
    sunCost = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_picture(self): 
        return self.picture

    def get_card_picture(self): 
        return self.card_picture

    def get_sunCost(self): 
        return self.sunCost
