import enchant
from nltk.metrics import edit_distance

class SpellingReplacer(object):
	def __init__(self,dict_name='en',max_dist=1):
		self.spell_dict = enchant.Dict(dict_name)
		self.max_dist = max_dist


	def replaces(self,word):
		if self.spell_dict.check(word):
			return word

		suggestions = self.spell_dict.suggest(word)
        
        for x in suggestions:
        	if edit_distance(word,x)<=self.max_dist:
			return suggestions[0] 
		    else :
			return word