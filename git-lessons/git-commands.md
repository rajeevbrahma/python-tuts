https://github.com/

Register using Email and Password

- Clone a repository

    # git clone "gitrepourl"

- Pull the changes of a repository

    # git pull

    Using (-p, --prune) option will ensure remove any remote-tracking references 
    that no longer exist on the remote before fetching
    
    # git pull -p

- To list all the branches in a repository

    # git branch -al

- To add specific files to the commit

    # git add <path/file1name> <path/file2name>

- To add all the changed files to the commit

    # git add .

- Delete a local branch

    # git branch -d "branchname"

- Delete a remote branch

    # git push origin -d "branchname"

- change case-sensitive folder names

    # git mv "FolderName" temp && git mv temp "foldername"

