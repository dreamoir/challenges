# this script counts all words in an input file and outputs frequency of each word
import sys
import os

filename = input('Enter a filename: ') 
cur_dir = os.getcwd()
file_list = os.listdir(cur_dir)
words = { }

if filename in file_list:
	print("***File Found!***")
	with open(filename,'r') as file:
		for word in file.read().split():
			if word not in words:
				words[word] = 1

			else:	
				words[word] +=1

	print(words)
	most_word=max(words,key=words.get)
	print("Most frequently word is : ",most_word," - occuring",words.get(most_word),"times")


else:
	print('***Invalid file name or File not found!***')

	# Use a dictionary to store word and freq?
	# define a function?