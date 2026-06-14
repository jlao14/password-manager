# password-manager
A secure, offline desktop application built with Python to manage your passwords. This tool allows you to generate strong, randomized passwords, securely store them locally, and quickly retrieve them whenever needed.

## Features
- **Password Generation:** Automatically generates strong, randomized passwords combining letters, numbers, and symbols.
  
- **Auto-Copy to Clipboard:** Generated passwords are automatically copied to your clipboard (using `pyperclip`) for immediate use.
  
- **Secure Local Storage:** Saves your website, email, and password combinations in a structured, local `data.json` file for easy reading and data management.
  
- **Search Functionality:** Quickly find saved passwords by typing the website name and clicking "Search" to retrieve the data from the JSON file.
  
- **Graphical User Interface (GUI):** A clean, user-friendly desktop interface built with Python's native `tkinter` library.

## Prerequisites
To run this project, you need Python installed on your system along with the `pyperclip` library. 

## Setup & Installation
1. Clone this repository or download the project files to your local machine.
2. Install the required `pyperclip` library by running the following command in your terminal:
   ```bash
   pip install pyperclip
