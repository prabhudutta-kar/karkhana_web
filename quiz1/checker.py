import requests

x = requests.get('./quiz.htmlpython')
print(x.status_code)