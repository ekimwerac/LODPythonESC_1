#!/usr/bin/perl -w

use DBI;
use strict;
use warnings;

my $lessh;
my $passwd;

if ( $^O ne 'MSWin32' ) {
   open ($lessh, "| less") or die "No less $!\n";
   select $lessh;
   
   $passwd = 'secret';
}

my $dbh = DBI->connect('DBI:mysql:whisky', 'root', $passwd) ||
                    die "Unable to connect: $DBI::errstr\n";

my $sql = "SELECT BRANDS.BNAME, REGION.RNAME FROM BRANDS,REGION " .
          "WHERE REGION.REGION_ID = BRANDS.REGION_ID ORDER BY BRANDS.BNAME";

my $sth = $dbh->prepare($sql);
$sth->execute();

while (my $row = $sth->fetchrow_arrayref) 
{
   printf ("%-30s %-20s\n", @$row);
}

close $lessh if defined $lessh;

$sth->finish();
$dbh->disconnect();

