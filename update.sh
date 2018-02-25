#! /bin/bash

if [ "$1" == "l" ] || [ "$1" == "L" ]
then	
	curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH(n) WHERE ID(n) = '$2' SET n '$3' return n"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
fi

if [ "$1" == "p" ] || [ "$1" == "P" ]
then
    if [ "$2" == "n" ] || [ "$2" == "N" ]
    then
	    curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH(n) WHERE ID(n) = '$3' SET n.'$4' = \"'"$5"'\" return n"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
    fi
    if [ "$2" == "r" ] || [ "$2" == "R" ]
    then
	    curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH ()-[r]-() WHERE id(r)='$3' SET r.'$4' = \"'"$5"'\" return r"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
    fi
fi
