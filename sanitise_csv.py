
# Remove or replace specified substrings (e.g characters) in a CSV file and output in a new file
# For corrupted chars you may need to run in terminal: iconv -c -t utf8 input.csv > input.utf8.csv

# Import dependencies
import csv
import time

input_file = 'input.utf8.csv' 																# define the file to be cleaned-up
output_file = "clean_output %s.csv" % time.strftime("%Y-%m-%d %H:%M")						# define the output file

# Move rows from the input to a list
with open(input_file, 'r', encoding='utf-8') as f:
  reader = csv.reader(f)
  items_to_fix_list = list(reader)

# Setup the output CSV file
with open(output_file,'a') as file:
	file.write("Fixed")

# Define replacements. To be expanded
special_chars = [
	['Œ',' '],
	['ä',' '],
	['ó',' '],
	['ñ',' '],
	['¢',' '],
	['ì',' '],
	['»',' ']]

changes = len(special_chars)

def write_result_csv(item):
	with open(output_file,'a') as file:
		file.write("\n" + item)

for item in items_to_fix_list:
	item = str(item)
	count = 0
	print(item)
	while count < changes:
		item = str.replace(item, str(special_chars[count][0]), str(special_chars[count][1]))
		count +=1
	print(item)
	write_result_csv(item) 


