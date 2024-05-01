•	git add ,git commit, git push 
$ git status

git add file-name.extension

You can also add all of the files that you have edited at the same time using:   git add .

Creating branches
4.	git checkout -b feature-branch

Merging branch:
1.	Switch back to the main branch.
i.	git checkout main
2.	Merge the branch into the main branch
i.	git merge feature-branch
i.	git add .
ii.	git commit -m "Merge feature-branch into main"
4.	Push changes to github using the following command.
i.	git push origin main

