# Pumpkin Spyce
A python library to add pumpkin spice to objects. Please don’t expect to much, this library is quite disappointing, just like pumpkin spice! It also adds unnecessary cost, contains no actual pumpkin and ruins perfectly good ~~coffee~~ classes.

## How to use
Say you are making some Node class for a binary tree.
```
class Node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
```
Who hasn’t see this a million times? It works, is functional, but will anyone care about your implementation of a node?<br/>
Why not spice things up?! 
```
from pumpkin_spyce import pumpkin_spice

@pumpkin_spice()
class Node(object):
    def __init__(self,name):
        self.left = None
        self.right = None
        self.name = name
```
This Node is sure to be popular during the autumn months!

That is not all! You can add extra spice to your classes by specifying the spice amount!
```
@pumpkin_spice(7500)
class Pizza(object):
	def __init__(self,toppings):
		if “pineapple” in toppings:
			raise NotAReallPizzaException()
		self.toppings = toppings
```
Wowzers! Thats a lot of pumpkin_spice!

Finally, Pumpkin Spyce ensures you don’t accidentally forget to add any spice to your classes.
```
@pumpkin_spice(0)
class Pumpkin_Beer(object):
    def __init__(self,ingredients):
        self.ingredients = ingredients + ["2 cans of real pumpkin"]
```
A Pumpkin_Beer class with real pumpkin in it?! This has to be a mistake!<br/>
Thankfully Pumpkin Spyce will catch this egregious error.
```
python make_good_beer.py 
NoSpice Exception
Traceback (most recent call last):
  File "make_good_beer.py", line 19, in <module>
    beer = Pumpkin_Beer(American_Pale_Ale_Ingredients)
  File "/home/moku/program/pumpkin_spyce/pumpkin_spyce.py", line 13, in __init__
    raise NoSpice()
pumpkin_spyce.NoSpice
```
