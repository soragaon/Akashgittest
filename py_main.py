import io
import os
import sys
import shutil
import pygit2
import zipfile
import datetime

repo_url = 'https://github.com/rdkcentral/rdkservices.git'

LOCAL_REPO = 'local_repo'


if __name__ == "__main__" :

    if os.path.exists(LOCAL_REPO):
        shutil.rmtree(LOCAL_REPO)
    
    # Clone local repo
    local_repo = pygit2.clone_repository(repo_url,
                                           LOCAL_REPO, checkout_branch="feature_doc_site")

    #repo = pygit2.clone_repository(url,dir,bare=False,checkout_branch="master",callbacks=RemoteCallbacks())

    branches_list = list(local_repo.branches)
    print(branches_list)
    #pygit2_branch = local_repo.branches['origin/' + branch]
    #branch = local_repo.lookup_branch('feature_doc_site')

    #ref = local_repo.lookup_reference(branch)

    #repo.checkout(ref)

    #print (ref)

