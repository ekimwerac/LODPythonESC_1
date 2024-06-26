import unicodedata

greek = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta',
         'Iota','Kappa','Lamda','Mu','Nu','Xi','Omicron','Pi','Rho',
         'Final Sigma','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']

#Format required:
#    The character name (cname), left justified, maximum 12 characters
#    A colon separator
#    The lowercase Greek character
#    The uppercase Greek character
       
for cname in greek:
    try:
       lc = unicodedata.lookup("GREEK SMALL LETTER " +
                               cname.upper())
       uc = unicodedata.lookup("GREEK CAPITAL LETTER " +
                               cname.upper())
       print("{0:<12s}: {1} {2}".format(cname,lc,uc))
        
    except (UnicodeEncodeError,KeyError) as err:
        print(err)
        
