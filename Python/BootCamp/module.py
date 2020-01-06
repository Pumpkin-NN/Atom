# Regular Expression Module
import re

text = 'Today is a good day, day day happy day'

# Search the word in the phrase, return a Match object
match = re.search('day', text)

print(match)


# Remove all the punctuation
print(re.findall('[^?/, ]+', text))



# Split the email domain

split_term = '@'

email = 'hello@mail.com'

domain = re.split(split_term, email)

print(domain[0])
