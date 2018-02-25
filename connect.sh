#! /bin/bash
if [[ $# -eq 2 ]]
then
	curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH(n) WHERE ID(n) = '$1' MATCH(m) WHERE ID(m) = '$2' CREATE (n) -[r:USE]-> (m) RETURN n,r,m;"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
fi
if [[ $# -eq 3 ]]
then
	curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH(n) WHERE ID(n) = '$1' MATCH(m) WHERE ID(m) = '$2' CREATE (n) -[r:'$3']-> (m) RETURN n,r,m;"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
fi
if [[ $# -eq 4 ]]
then
	curl -s -H accept:application/json -H content-type:application/json -d '{"statements":[{"statement":"MATCH(n) WHERE ID(n) = '$1' MATCH(m) WHERE ID(m) = '$2' CREATE (n) -[r:'$3'{'"$4"'}]-> (m) RETURN n,r,m;"}]}' http://$(gpg --decrypt data1c 2> /dev/null):$(gpg --decrypt data2c 2> /dev/null)@localhost:7474/db/data/transaction/commit
fi
