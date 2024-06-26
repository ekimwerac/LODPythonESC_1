#!/usr/bin/perl -w

use DBI;
use strict;

for my $driver (DBI->available_drivers())
{
   print "Driver: $driver\n";
   eval{print map {"\t$_\n"} DBI->data_sources($driver)};
   print "\n";
}

DBI->installed_versions();

