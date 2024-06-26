#!/usr/bin/ruby

require 'dbi'

dbh = DBI.connect("dbi:Mysql:whisky:localhost", 'root', '')

#cur = dbh.cursor()
					  
#cur.execute ('

#for row in cur.fetchall():
#   print "%-30s %-30s" % row


sth = dbh.execute('SELECT BRANDS.BNAME, REGION.RNAME' +    
                  'FROM BRANDS,REGION' +                    
                  'WHERE REGION.REGION_ID = BRANDS.REGION_ID' +
                  'ORDER BY BRANDS.BNAME;')
                  
   sth.fetch do |row|
       printf "%s, %s\n", row[0], row[1]
   end
   
sth.finish


#rescue DBI::DatabaseError => e
#    puts "An error occurred"
#    puts "Error code: #{e.err}"
#    puts "Error message: #{e.errstr}"
#ensure
    # disconnect from server
    dbh.disconnect if dbh
#end


