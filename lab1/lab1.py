import requests
print('requests version ' + requests.__version__)

print('\n Google Home Page')
homePage = requests.get('http://www.google.com')
print(homePage)

print('\n Github')
githubCode = requests.get('https://raw.githubusercontent.com/aaronz1999/CMPUT404/lab1/main/lab1.py')
print(githubCode.text)
