# function finditer

import re
matcher=re.finditer('\D','12dsafd43 q434eq')
for m in matcher:
    print(m.start(),'...',m.end(),'...',m.group())

