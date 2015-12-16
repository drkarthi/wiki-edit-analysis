"""
Convert given data to csv format
"""

import csv

f = open('usersContributions_allUsers', encoding='utf-8')
lines = f.readlines()

csvwriter = csv.writer(open("wiki.csv","w",encoding="utf-8"), delimiter=',', lineterminator='\n')
csvwriter.writerow(['Editor','Article','NumEdits'])
for line in lines:
	unclean_flag = 0
	rows = []
	items = line.split('\t')
	editor = items[0]
	articles = items[1:-1]
	end_char = items[-1]
	for article in articles:
		comps = article.split('::::')
		if len(comps)==1:
			print("Less than 4 colons when user is {} and article is {}".format(editor,article))
			unclean_flag = 1
			break
		article_name = comps[0]
		# remove additional colons and store in num_edits
		num_edits = int( comps[1].strip(':') )
		rows.append([editor,article_name,num_edits])
	# ignore users who have less than 4 colons separating an article and num_edits 
	if unclean_flag == 0:
		csvwriter.writerows(rows)

