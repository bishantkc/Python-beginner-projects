# Git and GitHub

Git and GitHub are powerful tools for version control and collaboration. Understanding its basics will help us manage our projects and contribute to open source development.

**Table of Contents:**

1. [Git](#git)                                     
2. [Basic Git Commands](#basic-git-commands)
3. [Git status files](#git-status-files)
4. [Branching in Git](#branching-in-git)
5. [Remote Repositories](#remote-repositories)
6. [Configuration](#configuration)
7. [Undoing Changes(reset)](#undoing-changes)
8. [Terminal Commands](#terminal-commands)
9. [GitHub](#github)
10. [GitHub Basics](#github-basics)
11. [GitHub Workflow](#github-workflow)


## Git

* Git is a distributed version control system that helps you track changes in your code and collaborate with others.
* Git provides a collaborative and efficient way for teams to work on projects, enabling them to manage codebase versions, coordinate changes, and track the history of modifications.

## Basic Git Commands

| Command | Description |
| :------ | :------ |
| `git init` | Used to create a new Git repository |
| `git clone [repository URL]` | Creates a copy of a remote repository on our local machine |
| `git add [file]`| Stages changes for commit |
| `git commit -m "Commit message"`| Commits changes to the repository |
|`git status` | Shows the status of changes as untracked, modified, or staged |
| `git log`| Displays a log of commits |
| `git --help`| Displays help information about Git commands |
| `git --version` | Shows the Git version installed on your machine |

## Git status files

1. **Modified:** Changes have been made but not yet committed.

2. **Untracked:** New files that are not yet tracked by git or committed.

3. **Staged:** File is ready to be committed.

4. **Unmodified:** Unchanged or files that haven't been changed since the last commit.
    

## Branching in Git

| Command | Description |
| :------ | :------ |
| `git branch` | Lists all branches in the repository / to check branch |
| `git branch -M [branch-name]` | To rename branch |
| `git branch [branch-name]` | Creates a new branch |
| `git branch -d [branch-name]` | Deletes a specified branch |
| `git checkout -b [branch-name]`| Creates a new branch and switches to it |
| `git checkout [branch-name]` | Switches to a different branch |
| `git diff [branch-name]`| To compare commits, branches, files & more |
| `git merge [branch-name]` | Merges changes from one branch into another |

## Remote Repositories

| Command | Description |
| :------ | :------ |
| `git remote add origin [repository URL]`| Adds a remote repository to the local repository |
| `git remote -v` | Lists remote repositories / to verify remote |
| `git fetch` |  Fetches changes from a remote repository |
| `git pull origin [branch-name]` | Updates your local repository with changes from the remote repository |
| `git push origin [branch-name]` | Push changes to a remote repository / Upload local repo content to remote repository |

## Configuration

| Command | Description |
| :------ | :------ |
| `git config --global [option] [value]`| Sets a global configuration option for Git |
| `git config --global user.name "My Name"` |  Sets the author name for all commits | 
| `git config --global user.email "email@example.com"` | Sets the author email for all commits |
| `git config --list` |  Lists all Git configuration settings |

## Undoing Changes

| Command | Description |
| :------ | :------ |
**Case 1:** Staged / added changes
| `git reset [file]` |  Unstages changes for the specified file |
| `git reset` |  Unstages all changes |
**Case 2:** Committed changes| (for one commit)
| `git reset HEAD~1`| Resets the last commit
| `git reset HEAD [file]`| Unstages changes for the specified file without discarding changes |
**Case 3:** Committed changes | (for many commits)
| `git reset [commit hash]` | Resets to a specific commit, discarding changes after that commit (can get hash from `git log`)|
| `git reset --hard [commit hash]`| Discards all changes and resets to the specified commit |

## Terminal Commands

| Command | Description |
| :------ | :------ |
| `cd [directory-path]` | Changes the current working directory to the specified path |
| `cd ..` | Goes back to the parent directory |
| `clear` | Clears the terminal screen |
| `mkdir [directory-name]` | Creates a new directory with the specified name |

## GitHub

* GitHub is a website that allows developers to store and manage their code using Git.
* It offers a collaborative environment where developers can work together on projects, manage code repositories, track changes, and contribute to open source projects.

## GitHub Basics

1. **Repository:** A storage location for our project. It can be public or private.

2. **Fork:** Creates a personal copy of someone else's project.

3. **Clone:** Creates a local copy of a repository on our machine.

4. **Pull Request:** Proposes changes from our forked repository to the original repository.

## GitHub Workflow

1. **Create / Fork a GitHub Repository**

2. **Clone the Repository:**
    * Copy the repository URL.
    * Open a terminal and use `git clone [repository URL]` to clone the repository.

3. **Make Changes:**
    * Make changes to your code.

4. **Commit and Push Changes:**
    * Add changes (`git add [file]`)
    * Commit changes (`git commit -m "Commit message"`)
    * Push changes to your repository (`git push origin [branch-name]`)

5. **Create a Pull Request:**
    * Go to your fork on GitHub.
    * Click on "New Pull Request"
    * Compare changes and create the pull request.

6. **Review and Merge:**
    * The original repository owner reviews our changes.
    * If accepted, our changes are merged into the original repository.

