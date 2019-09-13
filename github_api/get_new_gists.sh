#!/usr/bin/env bash
if [[ ! -a /.dockerenv ]]
then
	echo Must be run in a Docker container
	exit 1
fi

function cleanup() {
	echo ".dump" | sqlite3 gists.db > db_export.sql
	git commit -am "Updated at $(date)"
	git push
	rm -f gists.db
}

if [[ ${GITHUB_GISTS_USERNAME} == '' ]]
then
	echo GITHUB_GISTS_USERNAME must be set in the environment
	exit 1
fi

cat db_export.sql | sqlite3 gists.db
trap cleanup EXIT
python gists.py
