import sqlite3
import re

def prep_row (row, ncols):
    row = row.rstrip()
    row = re.sub(r"'",r"''",row)
    
    # Add quotes around each field
    lrow = list((map (lambda f: "'"+f+"'", row.split(','))))
    if len(lrow) < ncols: 
        lrow.append("''")
    else:
        lrow = lrow[0:ncols]
    
    return ",".join(lrow)
    
    
db = sqlite3.connect('whisky')
cur = db.cursor()

for row in open ("brands.txt"):
    cur.execute("INSERT INTO BRANDS VALUES (" + prep_row(row,4) + ")")

for row in open ("licensee.txt"):
    cur.execute("INSERT INTO LICENSEE VALUES (" + prep_row(row,3) + ")")

for row in open ("manufact.txt"):
    cur.execute("INSERT INTO MANUFACT VALUES (" + prep_row(row,2) + ")")

for row in open ("region.txt"):
    cur.execute("INSERT INTO REGION VALUES (" + prep_row(row,2) + ")")

db.commit()
db.close()
