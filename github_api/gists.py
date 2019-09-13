import os
import sys
from github import Github
import sqlite3

def _get_db_conn():
	conn_string = "gists.db"
	# get a connection, if a connect cannot be made an exception will be raised here
	return sqlite3.connect(conn_string)


def get_new_gists(github_connection, github_username):
	user_obj = github_connection.get_user(login=github_username)
	gists = user_obj.get_gists()
	print('================================================================================\nGist search starts for username: ' + github_username)
	try:
		conn = _get_db_conn()
		for gist in gists:
			gist_id = gist.id
			cursor = conn.cursor()
			cursor.execute('select count(*) from gist where username = ? and gist_id = ?', (github_username, gist_id))
			if cursor.fetchone()[0]	== 0:
				insert_cursor = conn.cursor()
				insert_cursor.execute("insert into gist(username, gist_id) values(?,?)", (github_username, gist_id))
				print('New gist for ' + github_username + ' added with id: ' + gist_id)
				insert_cursor.close()
			cursor.close()
	except:
		print('There was an error. Please re-run')
		print('Error was: ', sys.exc_info())
		conn.rollback()
		sys.exit(1)
	conn.commit()
	print('Gist search complete\n================================================================================')

def check_inputs():
	try:
		os.environ['GITHUB_GISTS_USERNAME']
	except:
		print('GITHUB_GISTS_USERNAME must be set in the environment')
		sys.exit(1)

if __name__ in ('__main__', '__console__'):
	check_inputs()
	github_username = os.environ['GITHUB_GISTS_USERNAME']
	g = Github()
	get_new_gists(g, github_username)
