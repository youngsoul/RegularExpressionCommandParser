__author__ = 'appliedpathways'

import re

txt='When "my test string" goes above 3.1415298 sendemailto "me@me.com,you@you.com"'

re1='((?:[a-z][a-z]+))'	# Word 1
re2='.*?'	# Non-greedy match on filler
re3='(".*?")'	# Double Quote String 1
re4='.*?'	# Non-greedy match on filler
re5='((?:[a-z][a-z]+))'	# Word 2
re6='.*?'	# Non-greedy match on filler
re7='((?:[a-z][a-z]+))'	# Word 3
re8='.*?'	# Non-greedy match on filler
re9='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
re10='.*?'	# Non-greedy match on filler
re11='((?:[a-z][a-z]+))'	# Word 2 (sendemailto)
re12='.*?'	# Non-greedy match on filler
re13='(".*?")'	# Double Quote String 2 email addresses

reg_ex_string = re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13
print "reg ex: " + reg_ex_string

rg = re.compile(reg_ex_string,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
#m = rg.match(txt)

if m:
    word1=m.group(1)
    string1=m.group(2)
    word2=m.group(3)
    word3=m.group(4)
    float1=m.group(5)
    action=m.group(6)
    emails=m.group(7)
    print "("+word1+")"+"("+string1+")"+"("+word2+")"+"("+word3+")"+"("+float1+")"+"("+action+")"+"("+emails+")"+ "\n"
