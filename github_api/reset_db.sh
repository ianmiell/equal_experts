#!/usr/bin/env bash
if [[ ! -a /.dockerenv ]]
then
	echo Must be run in a Docker container
	exit 1
fi
cp db_initialise.sql db_export.sql
git commit -am 'reset db'
git push
