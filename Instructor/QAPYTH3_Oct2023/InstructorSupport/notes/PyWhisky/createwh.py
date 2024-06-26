import sqlite3

db = sqlite3.connect('whisky')
cur = db.cursor()

cur.execute ('DROP TABLE IF EXISTS BRANDS')
cur.execute ('CREATE TABLE BRANDS ('
                  'LICENSEE_ID CHAR(4),'
                  'REGION_ID   CHAR(4),'
                  'BNAME       VARCHAR(60) NOT NULL,'
                  'FLAG        CHAR(1))')

cur.execute ('DROP TABLE IF EXISTS LICENSEE')
cur.execute ('CREATE TABLE LICENSEE ('
                  'LICENSEE_ID CHAR(4) NOT NULL,'
                  'MANUFACT_ID CHAR(4),'
                  'LNAME       VARCHAR(60) NOT NULL,'
                  'PRIMARY KEY(LICENSEE_ID))')

cur.execute ('DROP TABLE IF EXISTS REGION')
cur.execute ('CREATE TABLE REGION ('
                  'REGION_ID CHAR(4) NOT NULL,'
                  'RNAME     VARCHAR(60) NOT NULL,'
                  'PRIMARY KEY(REGION_ID))')

cur.execute ('DROP TABLE IF EXISTS MANUFACT')
cur.execute ('CREATE TABLE MANUFACT ('
                  'MANUFACT_ID CHAR(4) NOT NULL,'
                  'MNAME       VARCHAR(60) NOT NULL,'
                  'PRIMARY KEY(MANUFACT_ID))')

db.commit()
db.close()

