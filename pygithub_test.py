import io
import os
import sys
import shutil
import pygit2
import zipfile
import datetime
from pygit2 import Username, UserPass, Keypair, KeypairFromAgent, KeypairFromMemory
import web_driver

#repo_url = 'https://github.com/rdkcentral/rdkservices.git'
repo_url = 'https://github.com/kponnu013/rdkservices.git'

LOCAL_REPO = 'rdkservice_local_repo'

username = 'kponnu013'
password = 'Leotimes@2022'

"""
def git_push(repo, remote_name='origin', ref='refs/heads/updateonscript:refs/heads/updateonscript'):
    for remote in repo.remotes:
        if remote.name == remote_name:
            remote.push(ref)  
"""

def gitpush():
    os.system("ls -l")
    os.chdir('./local_repo') # This will change the present working directory
    os.system("git push origin updateonscript") # Some application invocation I need to do.

def git_add(repo):
    #check repo status
    status = repo.status()

    for filepath,flags in status.items():
        print ("path %s flags %d", filepath)

    repo.index.add_all()
    repo.index.write()


def create_commits(repo, how_many):
    if repo.head_is_unborn:
        parent = []
    else:
        parent = [repo.head.target]
    global version
    for i in range(how_many):
        user = pygit2.Signature('test', 'test')
        tree = repo.index.write_tree()
        commit = repo.create_commit('HEAD',
                                    user,
                                    user,
                                    'test.txt on %s' % ( os.path.basename(os.path.normpath(repo.workdir))),
                                    tree,
                                    parent)

if __name__ == "__main__" :

    web_driver.automate_git_pull_request() 
    if os.path.exists(LOCAL_REPO):
        shutil.rmtree(LOCAL_REPO)
    
    
    credentials = UserPass(username, password)
    callbacks = pygit2.RemoteCallbacks(credentials=credentials)
    # Clone local repo
    local_repo = pygit2.clone_repository(repo_url,
                                           LOCAL_REPO, checkout_branch="feature_doc_site", callbacks=callbacks)

    branches_list = list(local_repo.branches)
    print(branches_list)

    source = "test.txt"
    destination ="./local_repo/test.txt"

    dest = shutil.copy(source, destination)

    git_add(local_repo)

    create_commits(local_repo, 1) 

    #gitpush()
