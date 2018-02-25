use strict;
use warnings;
use Term::ReadKey;

print "\nEnter user for db:";
ReadMode 2;
my $user = <>;
my $output = `echo "$user"|gpg --batch --yes --output data1c --symmetric --cipher-algo AES256`;
print "\nEnter password for db:";
my $pass = <>;
$output = `echo "$pass"|gpg --batch --yes --output data2c --symmetric --cipher-algo AES256`;
print "\nCredentials set for db";
