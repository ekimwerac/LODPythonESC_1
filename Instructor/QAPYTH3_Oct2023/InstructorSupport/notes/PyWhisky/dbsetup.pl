#!/usr/bin/perl
#  DBI Interface
#
#  Requires:
#
#      mysqladmin create publishers
#      mysqladmin create test         - used by Web exercises
#      mysqladmin -u root password secret
#
#   To check:
#      mysqlshow -u root -p publishers
#      mysqlshow -u root -p test
#
    use DBI;
    use strict;

my $dbh = DBI->connect('DBI:mysql:', 'root', 'secret') || die;
                                                                                
#+----------------+
#| Tables in test |
#+----------------+
#| guest          |
#+----------------+

my $sth = $dbh->prepare('CREATE DATABASE IF NOT EXISTS test');
$sth->execute();

$dbh = DBI->connect('DBI:mysql:test', 'root', 'secret') || die;
$sth = $dbh->prepare('DROP TABLE IF EXISTS authors');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE guest (
      id        varchar(6),
      name      varchar(30),
      address   varchar(255),
      phone     varchar(25),
      comments  varchar(255)
      )');
$sth->execute();
$dbh->disconnect;

#+----------------------+
#| Tables in publishers |
#+----------------------+
#| authors              |
#| blurbs               |
#| discounts            |
#| publishers           |
#| roysched             |
#| sales                |
#| salesdetail          |
#| stores               |
#| titleauthor          |
#| titles               |
#+----------------------+

$sth = $dbh->prepare('CREATE DATABASE IF NOT EXISTS publishers');
$sth->execute();

$dbh = DBI->connect('DBI:mysql:publishers', 'root', 'secret') || die;
$sth = $dbh->prepare('DROP TABLE IF EXISTS authors');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE authors (
      au_id      char(6) NOT NULL PRIMARY KEY,
      au_lname   varchar(30),
      au_fname   varchar(30),
      phone      varchar(25),
      address    varchar(255),
      city       varchar(50),
      state      char(2),
      country    varchar(30),
      postalcode varchar(10)
      )');
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS blurbs');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE blurbs (
      au_id char(6) NOT NULL PRIMARY KEY,
      copy  TEXT NOT NULL
      )');
$sth->execute();


my $sth = $dbh->prepare('DROP TABLE IF EXISTS discounts');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   "CREATE TABLE discounts (
      discounttype ENUM ('A', 'B', 'C', 'D', 'E') NOT NULL,
      stor_id  char(8) NOT NULL,
      lowqty   INTEGER,
      highqty  INTEGER,
      discount NUMERIC
      )");
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS publishers');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE publishers (
      pub_id   char(6) NOT NULL PRIMARY KEY,
      pub_name varchar(255) NOT NULL,
      city     varchar(50),
      state    char(2)
      )');
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS roysched');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE roysched (
      title_id char(8) NOT NULL,
      lorange  NUMERIC,
      hirange  NUMERIC,
      royalty  NUMERIC
      )');
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS sales');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE sales (
      ord_num   char(8) NOT NULL,
      salesdate DATE NOT NULL,
      stor_id   char(8)
      )');
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS salesdetail');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE salesdetail (
      title_id char(8) NOT NULL,
      ord_num  char(8) NOT NULL,
      discount NUMERIC,
      qty      INT,
      stor_id  char(8)
      )');
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS stores');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   "CREATE TABLE stores (
      stor_id      char(8) NOT NULL PRIMARY KEY,
      stor_name    varchar(255) NOT NULL,
      stor_address varchar(255),
      city         varchar(50),
      state        char(2),
      country      varchar(30),
      postalcode   varchar(10),
      payterms     ENUM ('M', 'N', 'P', 'R', 'S') NOT NULL
      )");
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS titleauthor');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   "CREATE TABLE titleauthor (
      au_id    char(6) NOT NULL,
      title_id char(8) NOT NULL,
      au_ord   NUMERIC,
      royaltyper ENUM ('T', 'U', 'V', 'W', 'X') NOT NULL
      )");
$sth->execute();

my $sth = $dbh->prepare('DROP TABLE IF EXISTS titles');
$sth->execute();
                                                                                
$sth = $dbh->prepare (
   'CREATE TABLE titles (
      title_id    char(8) NOT NULL PRIMARY KEY,
      title       varchar(255) NOT NULL,
      pub_id      char(6),
      price       NUMERIC,
      advance     NUMERIC,
      total_sales BIGINT,
      notes       TEXT,
      pubdate     DATE,
      contract    char(8)
      )');
$sth->execute();

    $sth->finish;
    $dbh->disconnect;

