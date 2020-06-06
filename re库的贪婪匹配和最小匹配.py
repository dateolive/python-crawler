import re
match=re.search(r'PY.*N','PYANBNCNDN')
print(match.group(0))  #贪婪匹配


match=re.search(r'PY.*?N','PYNNANNBNCNDN')#最小匹配
print(match.group(0))