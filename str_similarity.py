from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
  
>>> similar("Apple","Appel")
0.8
>>> similar("Apple","Mango")
0.0  
