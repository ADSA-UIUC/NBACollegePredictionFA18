# NBACollegePredictionFA18
This the repository for an ADSA project for FA 18.

Use of Github:
1. Don't work directly on master
2. Make branches based on small problems
3. Name branch <WhatBranchChanges-Names>
4. Commit frequently to your branch
5. Try and merge with master frequently (small branches)
6. Once you merge with master, create a new branch off master (don't just use the same branch every time.)
Commands:
* **Pull:** ```git pull origin <branch_name>```
* **Create a branch:** ```git checkout -b <branch_name>```
* **Commit to branch**
  * check changed files ```git status```
  * add files: ```git add <files_changed>``` or ```git add .``` to add all changes
  * commit changes with message: ```git commit -m "<message>"```
* **Push Commits** ```git push origin <branch_name>```
* **Checkout branch** ```git checkout <branch_name>```
* **TO MERGE WITH MASTER**
  * 1. Push changes to your branch ```git push origin <branch_name>```
  * 2. Pull from your branch ```git pull origin <branch_name>```
  * 3. Checkout master ```git checkout master```
  * 4. Pull from master ```git pull origin master```
  * 5. Checkout your branch again ```git checkout <branch_name>```
  * 6. Now both branches are up to date
  * 7. Pull from master so that they merge. You might (will) have merge conflicts ```git pull origin master```
  * 8. Fix merge conflicts and push changes to branch
  * 9. Make a PR from your branch to master (do this online)
