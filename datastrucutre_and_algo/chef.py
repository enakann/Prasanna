import re
import itertools
import operator
class Ingredient:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def __repr__(self):
        return self.name


def create_ingredients(ls):
    type=''
    ingredient_objects=[]
    for i in ls:
        if "FAT" in i:
            type="FAT"
        elif "FIBER" in i:
            type="FIBER"
        else:
            type="CARB"
        ingredient_objects.append(Ingredient(i,type))
    return ingredient_objects




ls=["FATOil","FATCheese","FATEgg","FIBERSpinach","CARBRice","FIBERBeans"]

if len(ls)>= 3:
    objs=create_ingredients(ls)
    todays_dish=objs[:3]
    common=set([x.type for x in todays_dish])
    if len(common) > 2:
        for i in todays_dish:
            ls.remove(i)
            print(1)
print(0)
    




















