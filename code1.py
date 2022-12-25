import csv
from collections import OrderedDict

inputFile = open('Resume.csv', 'r' ,encoding='utf-8')
inputReader = csv.reader(inputFile)

outputFile = open('out.txt', 'w' ,encoding='utf-8')
outputWriter = csv.writer(outputFile)

for row in inputReader:
        text = row[3]

        # write column 3 to file for category
        outputWriter.writerow(text)

outputFile.close()
inputFile.close()

text = open("out.txt", "r")
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split(" ")
                         
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# to sort occurrences of word in descending order
sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: -item[1])}


# Print the contents of dictionary
for key in list(sorted_d.keys()):
     print(key, ":", d[key])
