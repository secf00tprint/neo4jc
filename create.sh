#!/bin/bash
curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"CREATE (n'"$2"' { name : \"'"$1"'\" }) RETURN n"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
