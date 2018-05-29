# tweet cleaner



#import os
import re
import string
import nltk 
from autocorrect import spell
#from nltk.tokenize import sent_tokenize 


class t_cleaner:

	def __init__(self,tweet):
		self.tweet = tweet

	

	def split_words(self): 

		self.tweet = re.sub(r'(@[a-zA-Z0-9]+[^\s])', r' *NAME* ', self.tweet)
		 # to clear @names  
        
                 # to split words JoinedLikeThis
		splitted_words =  re.sub( r'([A-Z][a-z0-9]+)', r' \1', self.tweet).split()   
		self.tweet = ' '.join(splitted_words) 
 
		self.tweet = re.sub(r'(I)([a-z]){2,3}[^\s]',r'\1[ ]\2',self.tweet)
		return self



	def basic_clean(self):

		 self.tweet = re.sub(r'(#)(\s?[^\s]*)', r' \2', self.tweet)
		 #replacing #hashtags with hashtag 

		 self.tweet = re.sub( r'([A-Z])\s', r'\1',self.tweet)
		 # to join words like H E L L O

		 self.tweet = re.sub(r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}",r'' , self.tweet ,re.IGNORECASE)
		 # to clear smileys 

		 self.tweet = re.sub( r'(-.+-)', r'',self.tweet)
		 # some more set of smileys

		 self.tweet = re.sub( r'[!]+', r'!',self.tweet)
		 # multiple exclamations

		 self.tweet = re.sub(r'(::\s[a-zA-Z0-9]+)|([;<>])', '',self.tweet)
		 # to clear out expressions in end

		 self.tweet = re.sub(r'([0-9]+:)|(:..)|(\.)|(&.+;)', '',self.tweet )
		 # to clearcp out tweet no. in the beginni

		 self.tweet = ' '.join(self.tweet.split())
		 # marking start of a new tweet and clearing out extra spaces

		 self.tweet = re.sub( r'([I])([a-z0-9]{2,4})', r'\1 \2', self.tweet)
		 # rough span to words like Iam Icant Ilike ...
		 
		 emoji_pattern = re.compile("["
		 u"\U0001F600-\U0001F64F"  # emoticons
		 u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                 u"\U0001F680-\U0001F6FF"  # transport & map symbols
                 u"\U0001F1E0-\U0001F1FF"  # flags 
                           "]+", flags=re.UNICODE)
		 self.tweet = emoji_pattern.sub(r'', self.tweet)
		 return self

         
	def spell_check(self) : 

		 pattern = re.compile(r'[!,.$%?]')
		 correct = []
		 x = nltk.word_tokenize(self.tweet)

		 for words in x :

		 	# we want to retain punctuations as well 
		 	if( words != '*NAME*') and (pattern.match(words) == None) :
		 		words = spell(words)
		 		
		 	correct.append(words)

		 self.tweet = ' '.join(correct)
		 return self


''' this is a checkpoint '''
tweet = '''
           125642617268176: hello @This lesving 
           noi #Hello !!!! Iam  #LetUsSeeIfThisThrngWorks 
           C A N I T J O I N T H I S :) now lets test ? this :: sad"
        '''   
e1 = t_cleaner(tweet)
e1 = e1.split_words()
e1 = e1.basic_clean()
print(e1.spell_check().tweet)

''' output is  - ( hello *NAME* leaving not Hello ! I am Let Us See If This Thing 
                     Works CANITJOINTHIS now lets test ? this of)
'''




# --main-- to clean up text file 

with open('test.txt','r') as rf :  #will change later to take in command line arg 

	with open('cleaned_text.txt','w') as wf:

		for line in rf:

			line = t_cleaner(line)

			x = line.split_words()
			x = x.basic_clean()
			x = x.spell_check()
			
			wf.write(x.tweet + '\n')


			
 
