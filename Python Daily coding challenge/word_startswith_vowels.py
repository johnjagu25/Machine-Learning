import re
a = "europe"
regex = "^[aeiouAEIOU][a-zA-Z0-9]*$"
print(re.search(regex,a))