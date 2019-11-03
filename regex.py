import re
def regex(p,s):
    if re.match(p, s):
        for match in re.finditer(p, s):
            print("Resultant match is {}".format(match.groups()))


p=r"(\w+)\@(\w+)\.(\w+)"
s="nava@gmail.com"

p=r"(\d+)\.(\d+)\.(\d+)\.(\d+)"
s="10.1.1.1"

#regex(p,s)


import re

regex = r"[A-Za-z0-9@#$%^&+=]{8,}"

test_str = "Python1199\nPython1323"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))



