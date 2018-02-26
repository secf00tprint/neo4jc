# Introduction

This project can be used to perform database queries on your Neo4j DB. 

Main purpose for this project was to have a fast way to interact with your database, so that you can use it in conjunction with your neo4j browser as a knowledge management tool. 

2 approaches where chosen to fulfill that:

1. Bash files where implemeneted for different CRUD operations you can call with just a few parameters which will translate to cipher queries and connect to database by REST.
2. A python script you can use to produce the same by text menu.

# System Requirements

- gpg >= 2
- python >= 2.7 < 3
- curl >= 7.50
- perl 5 >= version 26 
- neo4j >= 3.3

# Before first usage

## Perl
Install necessary perl library:

``` 
cpan Term::ReadKey
```

## Neo4j DB Authorization

To setup authorization for scripts to database
setup credentials with 

```
perl setcreds.pl
```

only use username and password without special characters

You will be asked for a password which GPG uses to store the credentials.

## Client start

```
python neoc.py
```
