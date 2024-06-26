#!/usr/bin/perl -w
use DBI;

local $, = "\n";
print DBI->data_sources('mysql'),"\n";

