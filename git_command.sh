#check remote url
git remote -v

#Git doesn’t store data as a series of changesets or deltas, but instead as a series of snapshots.

#explanation of branch https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is

#create a new branch, but not switch to this new branch 
git branch new_branch

#HEAD file pointing to the branch you’re on.

#switch to a new branch 
git checkout new_branch

git push origin master