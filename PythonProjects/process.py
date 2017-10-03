import sys
import os
import csv

#filename = input('Enter a filename: ') 


def process(filename):
	cur_dir = os.getcwd()
	file_list = os.listdir(cur_dir)
	section=[]
	status=''
	inet=''
	a= False
	if filename in file_list:
		print("***File Found!***")
		# open file to read
		with open(filename,'r') as file:
			print('interface, inet, status')
			# check every line to split into sections of status,interface,inet
			for line in file:
					#new section when line begins with interface and section is nonempty
				if "flags" in line and section:	
					words = [word for line in section for word in line.split()]
					interface = (words[0])
					for word in words:
						if '.' in word and not a:
							#boolean a ensured i net is not over written by data of similiar format
							inet = word
							a = True
						elif 'active' in word:
							status = word
					print(interface[:-1],',',inet,',',status)
					output=[interface,inet,status]
					#write output to csv
					with open('output.csv','a') as f:
						wr = csv.writer(f, dialect='excel')
						wr.writerow(output)
					
					a=False
					inet=''
					status=''	
					section = []
				

				section.append(line)

				



	else:
		print('***Invalid file name or File not found!***')

process('input.txt')