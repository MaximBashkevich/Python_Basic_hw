import requests
import re


my_request = requests.get('http://www.columbia.edu/~fdc/sample.html').text
pattern = r'(?<=>)(.*)(?=</h3>)'
result = re.findall(pattern, my_request)
print(result)
