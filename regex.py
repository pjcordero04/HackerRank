import re
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile(r'(\w|[-.])+@([a-z]|-)+.[a-z]+')
matches = pattern.finditer(emails)

for match in matches:
    print(match)

urls = '''
https://www.google.com
http://coreysms.com
https://www.nasa.gov
'''

patterns = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matchesx = patterns.finditer(urls)

for matchx in matchesx:
    print(matchx)