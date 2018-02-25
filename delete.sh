#!/bin/bash

if [ "$1" == "n" ] || [ "$1" == "N" ]
then
	curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH(n) WHERE ID(n) = '$2' DETACH DELETE n;"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
fi

if [ "$1" == "r" ] || [ "$1" == "R" ]
then
	curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH ()-[r]-() WHERE id(r)='$2' DELETE r"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
fi

