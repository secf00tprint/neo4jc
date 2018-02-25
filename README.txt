# Introduction

This project can be used to interact with your Neo4j DB.

# System Requirements

- gpg >= 2
- python >= 2.7 < 3
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