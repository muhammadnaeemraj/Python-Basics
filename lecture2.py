# Regular Experation

import re

# Define a regular expression pattern
pattern = r'apple'

# Define a string to search
text = 'I like apples and oranges.'

# Using match() to find if the pattern matches at the beginning of the text
match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")

# Using search() to find if the pattern exists anywhere in the text
search = re.search(pattern, text)

if search:
    print("Pattern found at index:", search.start())
else:
    print("Pattern not found.")

# Using sub() to replace occurrences of the pattern with a new string
new_text = re.sub(pattern, 'banana', text)
print("New text:", new_text)





#################### More Practice #####################

content = "AI Artificial intelligence (AI), the ability of a digital computer or AI computer-controlled robot to perform tasks commonly associated with intelligent beings. The term is frequently applied to the project of developing systems endowed with the intellectual processes characteristic of humans, such as the ability to reason, discover meaning, generalize, or learn from past experience. Since the development of the digital computer in the 1940s, it has been demonstrated that computers can be programmed to carry out very complex tasks—such as discovering proofs for mathematical theorems or playing chess—with great proficiency. Still, despite continuing advances in computer processing speed and memory capacity, there are as yet no programs that can match full human flexibility over wider domains or in tasks requiring much everyday knowledge. On the other hand, some programs have attained the performance levels of human experts and professionals in performing certain specific tasks, so that artificial intelligence in this limited sense is found in applications as diverse as medical diagnosis, computer search engines, voice or handwriting recognition, and chatbots.";
pat = r"AI"

newMatch = re.match(pat, content)

if newMatch:
    print("Match Found :", newMatch.group())
else:
    print("Match not Found.")


newSearch = re.search(pat, "Artificial intelligence (AI), the ability of a digital computer or computer-controlled robot.")

if(newSearch):
    print("Match Found at ", newSearch.start())
else: 
    print("Match not Found.")



replace = re.sub(pat, "ai", content)
print(replace)



pattern3 = r'\d+'  # Matches one or more digits

text = 'I have 3 apples, 5 oranges and 10 bananas.'

matches = re.findall(pattern3, text)
print("Matches:", matches)





pattern4 = r'\w+'  # Matches one or more alphanumeric characters

text3 = 'The quick brown fox jumps over the lazy dog.'

matches4 = re.findall(pattern4, text3)
print("Matches:", matches4)





pattern5 = r'^The'  # Matches 'The' at the beginning of a line

text5 = '''The quick brown fox,
 The lazy dog'''

matches5 = re.findall(pattern5, text5, re.MULTILINE)
print("Matches:", matches5)








# Define a regular expression pattern
pattern6 = r'\d+'  # Matches one or more digits

# Compile the pattern into a regex object
pattern_obj6 = re.compile(pattern6)

# Define a text string
text6 = 'I have 3 apples and 5 oranges.'

# Use the compiled regex object to find all matches in the text
matches6 = pattern_obj6.findall(text6)
print("Matches:", matches6)

# You can reuse the compiled regex object for other operations
new_text = 'The price is $10.'
new_matches = pattern_obj6.findall(new_text)
print("New matches:", new_matches)
