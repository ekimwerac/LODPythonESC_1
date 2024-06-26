#!/usr/bin/perl -w

use DBI;
use strict;

my $dbh = DBI->connect('DBI:mysql:whisky', 'root', 'secret') ||
	                 die "Unable to connect: $DBI::errstr\n";
					  
my $sql = "SELECT BRANDS.BNAME, REGION.RNAME FROM BRANDS,REGION " .
          "WHERE REGION.REGION_ID = BRANDS.REGION_ID ORDER BY BRANDS.BNAME";

my $sth = $dbh->prepare($sql);
$sth->execute();

open (my $less, '>', "db.out") or die "No less $!\n";

$sth->dump_results (80, undef, ',', $less);
close $less;

$sth->finish();
$dbh->disconnect();

