import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # r: string pura (raw)
mo = phone_num_regex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phone_num_regex = re.compile(r'\d\d \d\d\d\d-\d\d\d\d')  # brazilian mode
mo = phone_num_regex.search('My number is 21 4545-4242.')
print('Phone number found: ' + mo.group())
