# Introduction and Initial Setup

## Git Started
This section will guide you on how to Install both Git and the Github Command Line Interface (CLI). Prior to first using GitHub, you will need to [Create an account](https://github.com/). Head there now, create an account and head straight back here.

Well done, you're now ready to procees. 


## Opening a Terminal
This workshop will be operating near exclusively from the terminal. Opening one differs slightly based on which Operating System (OS) you are using. Please proceed with the relevant instructions for your given OS.

### Linux
In Linux, you can open up a terminal using the GUI or simply use the shortcut button combination `ctrl`+`alt`+`t`

### MacOS
In Macos, you can use `command`+`spacebar` to open the search utility. then just type `terminal` and click on the result `Terminal.app`, a terminal will be opened for you.

## Installing Git

### Linux

For Debian/Ubuntu-based distributions, use the commands:

```bash
sudo apt update
sudo apt install git
```

For Fedora or RHEL/CentOS (with EPEL):
```bash
sudo dnf install git
```

### MacOS

Use Homebrew (reccomended) to install Git:

```bash
brew install git
```
Alternatively, Git can be installed on MacOS using the Xcode Command Line Tools by running:

```bash
xcode-select --install
```

## Configuring Git

Configure your Git installation with your name and email address using the following commands:
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

## Verifying Your Setup
To ensure Git is installed and configured correctly, run:
```bash
git --version
git config --list
```

## Installing GitHub CLI
Whilst GitHub is not strictly neccesary to enjoy the wonders of version control, its a very powerful tool and will help you share your projects seamlessly with your collaborators working on the same project. Before diving into your first GitHub project, lets ensure you're all set up with the necessary tools and access first. We will be doing this from the command line for maximum control, note however that there are various software packages with a GUI you could use instead, for example GitHub Desktop (not covered here).

### Step 1: Create a GitHub Account

You've done this already haven't you?! If not, sign up for a [Github account](https://github.com/) on their website. This is essential for managing and collaborating on projects hosted on GitHub, don't worry it's completely free!

### Step 2: Install Command Line Interface (CLI) Tools

GitHub provides CLI tools to work from the terminal when using GitHub. You can download them from the official [GitHub CLI page](https://github.com/cli/cli?tab=readme-ov-file#installation).

You can use the popular package manager `Brew` to install the CLI tools. MacOS typically comes with `Brew` pre-installed. For Linux users, you can install `Brew` by executing the following command in a terminal:

```bash
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
```

Follow the on-screen instructions to complete the installation. Then, install the GitHub CLI tools with:

```bash
brew install gh
```

## Step 3: Authenticate with GitHub CLI

Once the CLI tools are installed, start by logging in:

```bash
gh auth login
```

You'll navigate through a series of prompts to configure your setup. Here are the recommended responses:

```bash
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes 
? How would you like to authenticate GitHub CLI? Login with a web browser
```

## Note:
While it's possible to perform local operations, GitHub has required the use of a Personal Access Token (PAT) instead of a password since 2021 to access remote repositories. This adds an extra step for authentication but enhances security. If you followed the above instructions you should have nothing to worry about, but if you use a different CLI you might need to make sure you handle this correctly

## Extra Nuggets

Change Default text editor to Vim (only if you actually want to use Vim)
```bash
git config --global core.editor "vim"`
```

Enable / Disable coloured output (Would reccomend this one)
```bash
git config --global color.ui true
```

Create aliases
```bash
git config --global alias.ci commit
```
This will create an alias such that you can use git ci as a shorthand for `git commit`
