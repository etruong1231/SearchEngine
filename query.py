
import os
import json
from pprint import pprint
import re
from collections import Counter, defaultdict
import pickle

data = {}
index = defaultdict(list)

def get_json_data():
	global data	
	#loads up the info as a dict
	with open('WEBPAGES_CLEAN/bookkeeping.json') as data_file:    
	    data = json.load(data_file)

def look_for_url(path):
	global data
	#get the url
	return data[path]


def load_dict():
	global index
	#opens the file and gets the dict
	with open('indexed_words.json') as data_file:    
		index = json.load(data_file)



def find_query():
	global index
	query = raw_input("Please Enter Query:") #.lower() ? need to keep all lower?
	try:
		query_list = sorted(index[query], key= lambda x: x[1],reverse = True)
		if len(query_list) == 0:
			print(query+" was not found")
		else:
			for found in query_list:
				print(look_for_url(str(found[0])))
	except Exception as e:
		print("Error: Something went wrong!!")




if __name__ == '__main__':
	get_json_data()
	load_dict()
	while(True):
		find_query()
