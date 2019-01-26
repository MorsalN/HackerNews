import requests

from flask import Flask 
from flask import render_template

app =Flask(__name__)


@app.route('/')
def HackerNewsCode():
	response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')

# Get top 5 ids
top_five_ids = response.json()[:5]

# Fetch top 5 stories

stories = []

for top_id in top_five_ids:
	curr_story_api_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(id)
	curr_story = requests.get(curr_story_api_url)
	stories.append(curr_story.json())

listOfStories = []

for story in stories:
	title = story['title'] #gets the title of the current story
	comments = [] #creates an empty comments list every iteration of the loop
	dictionary = {}  #creates a new dictionary every iteration of the loop
   #print("\nTitle: " + title + "\n")
	for kid in story['kids'][:5]:
	   #print(kid)
	   kid_url = requests.get('https://hacker-news.firebaseio.com/v0/item/' +str(kid)+'.json?print=pretty')
	   #print(kid_url.json()['text'])
	   comment = kid_url.json()['text'] #puts the current comment text in a variable
	   #print(comment)
	   comments.append(comment) #adds the comment to the current comment list
	dictionary[title] = comments #sets key-value pair of title and list of comments
	listOfStories.append(dictionary) #add the current dictionary to the listOFStories

#print results
#for l in listOfStories:
	#print(l)
	#print("\n")

class HackerNews:
	with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/positive_words.txt', 'r') as open_pos:
		positive_vocab=open_pos.readlines()

	with open('/Users/MorsalNiyaz/Development/polyglot/cohort-1/data/negative_words.txt', 'r') as open_neg:
		negative_vocab=open_neg.readlines()
	
	def __init__(self, positive_vocab, negative_vocab):
		self.positive_vocab = positive_vocab
		self.negative_vocab = negative_vocab

	
	def analyze_news(hacker):
		words = hacker.split()

		num_positive_vocab = 0 
		num_negative_vocab = 0 
		for word in words:
		 
			if word in positive_vocab:
				num_positive_vocab += 1
			elif word in negative_vocab:
				num_negative_vocab += 1 

		if num_positive_vocab > num_negative_vocab:
			return "positive"

		elif num_positive_vocab < num_negative_vocab:
			return "negative"
		else: 
			return "inconclusive" 

		for sentence in listOfStories:
			hacker = sentence.split(",")[3].strip()

			analyze_news(hacker)
	
	hacker = input("What do you want to analyze?")
	analyze_news(hacker)
	print(analyze_news(hacker))

	

