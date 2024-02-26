# Initial Setup

Before diving into the intricacies of version control with Git, it's essential to have your environment set up. This section guides you through installing Git on Linux and MacOS, configuring Git for the first time, and ensuring your machine is ready for the workshop activities.

## Objectives

- Install Git on your system.
- Configure Git with your user information.
- Verify your installation and configuration.

## Installing Git

### Linux

For Debian/Ubuntu-based distributions, use:

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

Understood, Nick. Let's adjust the structure to include an initial setup as Section 01 and then revise the exercise in what will now be Section 02 to involve hands-on use of Git. Here’s how you can structure the README.md for both sections and a new exercise-1.md for Section 02.
Section 01: Initial Setup
README.md for "01-Initial Setup"

markdown

# Initial Setup

Before diving into the intricacies of version control with Git, it's essential to have your environment set up. This section guides you through installing Git on Linux and MacOS, configuring Git for the first time, and ensuring your machine is ready for the workshop activities.

## Objectives

- Install Git on your system.
- Configure Git with your user information.
- Verify your installation and configuration.

## Installing Git

### Linux

For Debian/Ubuntu-based distributions, use:

```bash
sudo apt update
sudo apt install git

For Fedora or RHEL/CentOS (with EPEL):

bash

sudo dnf install git

MacOS

Use Homebrew to install Git:

bash

brew install git

Alternatively, Git can be installed on MacOS using the Xcode Command Line Tools by running:

bash

xcode-select --install

Configuring Git

Configure your Git installation with your name and email address using the following commands:

bash

git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

## Verifying Your Setup

To ensure Git is installed and configured correctly, run:

```bash
git --version
git config --list
```
These commands should display your Git version and the user information you've configured, respectively.

## Next Steps

With Git installed and configured, you're ready to begin exploring version control concepts and start using Git. Proceed to the next section to dive into the basics of version control with Git
