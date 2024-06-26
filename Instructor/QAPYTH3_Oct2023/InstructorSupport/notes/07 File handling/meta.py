import glob

pattern = 'C:/QA/Python/*.ppt'
for file in glob.iglob(pattern):
    print (file)


        

