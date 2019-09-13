#!/usr/bin/env bash
function usage() {
	echo "$0 [GITHUB_USERNAME]"
}
if [[ $1 == '' ]]
then
	usage
	exit 1
fi
GITHUB_GISTS_USERNAME=${1}
# Ensure that we bust the Docker cache at the 'clone' point before cloning the repo.
perl -p -i -e "s/(.*bustcache:) .*/\1 $RANDOM/" Dockerfile
# Build the image with the latest clone/data in it.
docker build -t gists --build-arg git_username=${GITHUB_GISTS_USERNAME} .
# Run the search for new gists.
docker run -e GITHUB_GISTS_USERNAME=${GITHUB_GISTS_USERNAME} gists
