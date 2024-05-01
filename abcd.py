●	Set your username and email address by running the following commands: git config --global user.name "Your Name" git config -global user.email "your.email@example.com"
Replace "Your Name" with your desired username and "your.email@example.com" with your email address.

●	If you prefer to use a different name for the initial branch, you can set it using the following command:
git config --global init.defaultBranch main

●	To check your Git configuration settings, you can use the following command: git config
--list

To clone a remote repository, use the following command git clone <remote-url>
●	Replace <remote-url> with the URL of the remote repository.

●	To add a remote repository, use the following command:
git add remote <remote-name> <remote-url>

●	To push changes to a remote repository, use the following command:
git push <remote-name> <branch-name>

●	To pull changes from a remote repository, use the following command:
git pull <remote-name> <branch-name>

