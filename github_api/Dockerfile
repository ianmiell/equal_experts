FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y sqlite3 git python-pip
RUN echo 'PyGithub>=1.43.8' > requirements.txt && pip install -r requirements.txt && rm requirements.txt
RUN git config --global user.email "gist_searcher@example.com"
RUN git config --global user.name "Gist Searcher"
WORKDIR /gists
ARG git_username
# git_username _must_ be passed in
RUN /bin/bash -c '[[ ${git_username} != "" ]]'
ARG git_reponame=equal_experts
ARG git_server=github.com
ADD git_user_key /root/.ssh/id_rsa
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN git clone git@${git_server}:${git_username}/${git_reponame} # bustcache: 7021
WORKDIR /gists/equal_experts/github_api
CMD ["./get_new_gists.sh"]
