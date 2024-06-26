import glob, os, os.path,re

def get_dir(path):
    pattern = path + '/*'
    
    gfile = glob.iglob(pattern)
    file = True
    
    while file:
        file = next(gfile)
    
        if os.path.isdir(file):
            inp = yield file
            if inp:
                agen = get_dir(inp)
                file = None
                while True:
                    try:
                        file = yield agen.send(file)
                    except StopIteration:
                        break
                file = True

######################################################################

gen = get_dir('C:/')
cmd = None

while True:
    # If send is used, a StopIteration excepton is raised
    try:
        fn = gen.send(cmd)
        print(fn)
        if re.search(r'[cC]live',fn):
            cmd = fn
        else:
            cmd = None
    except StopIteration:
        break
    