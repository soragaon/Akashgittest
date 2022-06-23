import io
import os
import sys
import shutil
import pygit2
import zipfile
import datetime

repo_url = 'https://github.com/rdkcentral/rdkservices.git'

LOCAL_REPO = 'local_repo'

fn = 'README'

version = 1


def create_commits(repo, how_many):
    if repo.head_is_unborn:
        parent = []
    else:
        parent = [repo.head.target]
    global version
    for i in range(how_many):
        """
        # Apparently the index needs to be written after a write tree to clean it up.
        # https://github.com/libgit2/pygit2/issues/370
        repo.index.write()
        parent = [commit]
        version += 1
        """
        #user = repo.default_signature('AKASH SORAGAON','test')
        user = pygit2.Signature('test', 'test')
        tree = repo.index.write_tree()
        commit = repo.create_commit('HEAD',
                                    user,
                                    user,
                                    'Version %d of test.txt on %s' % (version, os.path.basename(os.path.normpath(repo.workdir))),
                                    tree,
                                    parent)

if __name__ == "__main__" :

    if os.path.exists(LOCAL_REPO):
        shutil.rmtree(LOCAL_REPO)
    
    # Clone local repo
    local_repo = pygit2.clone_repository(repo_url,
                                           LOCAL_REPO, checkout_branch="feature_doc_site")


    branches_list = list(local_repo.branches)
    print(branches_list)

    from pygit2 import GIT_STATUS_WT_NEW, GIT_STATUS_WT_DELETED, GIT_STATUS_WT_MODIFIED
    print("GIT_STATUS_WT_NEW", GIT_STATUS_WT_NEW)
    print("GIT_STATUS_WT_DELETED", GIT_STATUS_WT_DELETED)
    print("GIT_STATUS_WT_MODIFIED", GIT_STATUS_WT_MODIFIED)

    source = "test.txt"
    destination ="./local_repo/test.txt"

    dest = shutil.copy(source, destination)

    #check repo status
    status = local_repo.status()

    for filepath,flags in status.items():
        print ("path %s flags %d", filepath)

    local_repo.index.add('test.txt')
    local_repo.index.write()  

    create_commits(local_repo, 1) 
