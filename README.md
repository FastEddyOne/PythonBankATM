# Simple Banking App

## Description

A basic banking app implemented in Python that allows a user to check their balance, make a deposit, make a withdrawal, and quit the application. This application is designed to be simple and straightforward to use, providing a base upon which additional functionalities can be added.

## Features

- **Check Balance**: View the current balance.
- **Make a Deposit**: Add funds to the account.
- **Make a Withdrawal**: Remove funds from the account.
- **Quit**: Exit the application.

## Usage

The user interacts with the application through a command-line interface and can choose an option by entering a single letter (capitalization doesn't matter). The following options are available:

- **B** or **b** - Check the current account balance.
- **D** or **d** - Make a deposit to the account.
- **W** or **w** - Make a withdrawal from the account.
- **Q** or **q** - Quit the application.

When making a deposit or withdrawal, the user is prompted to enter the amount.

## Installation and Running

1. Ensure Python is installed on your machine.
2. Download the app (app.py file) and navigate to its directory in the terminal.
3. Run the app using the command `python app.py` (Ensure you are using Python 3, you may need to use `python3` depending on your system configuration).
4. Follow the prompts on the screen to interact with the app.


### Note:
This is a basic version and doesn't handle several edge cases and doesn't store the balance persistently - if you close the app, the balance information will be lost. The deposit and withdrawal functions do not validate the input for non-numeric characters or negative amounts. Future versions may handle these cases and provide additional functionality.

### Contribution
Feel free to fork the repository and submit pull requests to add more functionalities or improve existing ones. Also, open issues if you find bugs or want to suggest new features.

### License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
