#!/usr/bin/perl -w

my $dbh = DBI->connect('DBI:mysql:test', 'root', 'secret');


"Click here to look at the Guestbook: ",
    $co->a({href=>"http://localhost/cgi-bin/guestviewsql.cgi"}, "View"), ".";

my $q1 = "INSERT INTO guest (id, name, address, phone, comments) VALUES 
          (\'\', \'" . $co->param('name') . "\', \'" . 
                       $co->param('address') . "\', \'" . 
                       $co->param('phone') . "\', \'" . 
                       $co->param('comments') . "\')";

