#!/usr/bin/perl -w
# select2.pl
use DBI;
use strict;

my $dbh = DBI->connect('DBI:mysql:whisky', 'root', 'secret') ||
	                 die "Unable to connect: $DBI::errstr\n";
					  
my $sql = "SELECT LICENSEE.LNAME, MANUFACT.MNAME FROM LICENSEE,MANUFACT " .
          "WHERE LICENSEE.MANUFACT_ID = MANUFACT.MANUFACT_ID";

my $sth = $dbh->prepare($sql);
$sth->execute();

open (MORE, "| more") or die "No more $!\n";
select MORE;

printf "%-40s %-39s\n", 'LICENSEE', 'MANUFACTURER';
while (my $row = $sth->fetchrow_hashref) 
{
   #printf "%-40s %-39s\n", $row->{'LNAME'}, $row->{'MNAME'} 

   printf "%-40s %-39s\n", 
           substr($row->{'LNAME'}, 0, 40), substr($row->{'MNAME'}, 0, 39) 
}

close MORE;

$sth->finish();
$dbh->disconnect();

