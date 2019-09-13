= `github_api`

"Using the Github API you should query a user's publicly available github gists. The script should then tell you when a new gist has been published."

This implementation uses:

- Docker to run the check for new gists.

- Sqlite3 to store the previously-seen gists.

- Git to store the database.

It is thus 'serverless'. It uses git to store state.

== Quickstart

1) Clone this repo, and navigate to it.

2) Place your git account access key in: `git_user_key`

3) Call `./run.sh [GITHUB_USERNAME]`, where `[GITHUB_USERNAME]` is replaced with the username you wish to target.

The output will tell you if a new public gist has been seen in the given GitHub user account.

For example, it will contain:

```
================================================================================
Gist search starts for username: ianmiell
New gist for ianmiell added with id: 0b9dd8de61c831486d5888a424a35058
New gist for ianmiell added with id: 20cbf0722622a0fb606d2a04ff71150e
Gist search complete
================================================================================
```

== Requirements

- Docker

- perl

- Git account key

== Files

=== Entrypoint

`run.sh` - Main user entrypoint: builds and runs the Docker container. Requires the targeted Github user id be passed in. Not stored in Docker container. Takes one argument (the 'target' GitHub account).

=== Files in Git

`Dockerfile`        - Builds the Docker image in which the application runs. It clones the repository containing the database using the `git_user_key` you place in this folder.

`db_export.sql`     - Contents of gists database, which stores previously-seen gists per user.

`db_initialise.sql` - Database initialisation schema. Used by `reset_db.sh`.

`get_new_gists.sh`  - Shell script to get new gists. Must be run in a Docker container.

`gists.py`          - Python script that does the work to retrieve public gists from a given user.

`reset_db.sh`       - Reset the database to empty. Uses `db_initialise.sql` to overwrite the database.

=== Files Not Stored in Git

These files are in `.gitignore`, as we do not want them to be checked in.

`git_user_key`      - Key to log into the git server to clone this repo. This is not stored in git, and must be provided by the user.

`gists.db`          - The loaded database of previously-seen gists.

=== Test files

`TEST_PLAN.md`      - Documentation on tests run.
