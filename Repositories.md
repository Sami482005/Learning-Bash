# Why Repositories
Repositories can be a place where several people collaborate on a certain project, instead of having to send each other zip files, this is an easier way of collaborating.
The best way to do it, is having your own repository on your local machine, where the files that you are creating and for you, and connecting it to an online repository that everyone can update and download changes that other people made from.
Git is powerful enough to be able to make these changes and merges and you don't need to know how.

###### Note:
This will explain how you can create a repository through your VS code.

# Connecting Local Repository to online repository on Github

One way to do this is to create your local repository through the terminal:

1. Go to the location you want using cd
type: 
git init #makes whatever folder you are in a repository

note: you cannot make any commit commands outside a git repository

So now this directory is tracked by git and you can use its commands

2. Make all the modifications you want: including creating new files, codes, scripts...

3. git add: when you create several files 
    git add .: used when you have several files that have been changed.

    The add command puts all the changes into the staging area.

4. git commit -m "message to display"

    In between "" you can write a message up to 50 characters long that explains the changes that your are committing to the repository.

    Know that if you have made changes, you don't have to immediately commit them, you can wait until you have enough and then commit them all together.


    Also, if you made changes through your vs code, it does not mean that your online repository has been iammediately updated, instead you need to push these changes by writing in the terminal. Your local repository is updated.

5. go to github.com and create an online repository that can either be public or private depending on what you want

6. write in your command line:
    git remote add origin <URL_of_the_online_repository>

    And now you will connect your online repository to your local repository.

7. git push --all origin or git push -u origin master. #-u will save the settings of the push to always be on the master branch (I will explain)
    the first one actually worked for me but the second one can work. Unfortunately I am not so sure of when to use which one but try either and whatever works is great.
    But what I do know is that the second didn't work but because I did not link my online repository as I did here.
    What I did was through the welcome page on VS, I used clone git repository. 
    And it made me login into github account and this is how I'm working. 

## Online Repos Problems:
If you had any problems pushing unto the online repo, you might have to set up a username, you should have authenticated yourself on your machine first but do try this on your terminal
git config --global user.name "Put the name that will identify you every time you push or pull"

git config --global user.email "email on git"

If this doesn't work go on the internet and lookup how to authenticate

### Status:
git status #shows you what kind of changes have been made.

# Branches

In repositories, maybe you don't want to save your changes to the main branch where everyone can download it. Because it might be wrong and will mess everything up for everyone. 
Instead what we do is work on another branch which has all the features and updates of the main branch but it has the features in progress. This new branch can be later merged into the main branch and can be constantly updated from the main branch with new features.
The main branch that is containing the final product(S) is called the master branch.

to create a new branch use:
`git branch <name_of_the_new_branch>`
New Branch is created.
By Default: New branch is up to date with HEAD of main branch

`git checkout <name_Of_Branch>`
Goes to a specific branch

`git checkout -b <name_of_branch>` 
Creates a new branch and moves to it.

`git merge origin/new_branch_name`
Takes all the changes from the new branch into the branch you are currently in.

`git branch`
Shows you all the branches of the repository.
GIt shows an asterisk mark before currently checked out branch.

`git branch -D <Branch_name>`
Deletes a branch

`git branch -m <New_name>`
Renames the branch you are currently in

`git push origin <new_branch>`
Pushes changes to the other branch.

`git log origin/new_branch_name -2`
Allows a user to see the commit message the other user is performing on that new branch.

`git diff`
Reveals differences between branches

# Pull
git pull origin master: pull from the remote the master branch

updates local repo.

If you've made changes on both local and remote repo on the same time.
It won't allow you to push, so you need to pull first.
They will tell you that there is a configuration error. And the file that is downloaded will show you an error message, we need to delete whatever we need to delete and keep the file the way that we want it to appear. Which will fix it.
Then we add and commit the changes and the push to the remote repo.

# Pushing secondary branch:

git checkout other branch.

git push origin newBranch.

make a pull request.


# Disconnecting
to kow which remote repository is connected to your local repo
    git remote -v
To remove it
    git remote remove origin

You can have a repo that is connected to an online repo, and one directory in that repo is connected to another online repo because you cloned an online repo into that directory; that directory is called a submodule.