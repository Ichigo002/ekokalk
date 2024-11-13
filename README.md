# ekokalk

# Guide step by step to set up
This guide provides steps to set up a Python project with a requirements.txt file on both Linux and Windows 10. By following these steps, you will install the required dependencies for the project and ensure everything is set up correctly for development.

Prerequisites:
- Python 3.x installed on your system
- pip (Python package installer) installed

Let's start:

1. Clone or Download the Project
Ensure you have the project folder that contains the requirements.txt file on your local machine.

On Linux:

2. Navigate to the project directory in terminal:

3. Create a virtual environment:
`python3 -m venv venv`

4. Activate the virtual environment:
`source venv/bin/activate`

On Windows 10:

2. Navigate to the project directory in terminal:

3. Create a virtual environment:
`python -m venv venv`

4. Activate the virtual environment:
`.\venv\Scripts\activate`

Once activated, your command prompt should display the virtual environment name (e.g., (venv) ).

5. Install Dependencies: `pip install -r requirements.txt`

This will install all the libraries and packages specified in the requirements.txt file.

6. Verify Installation
To ensure everything has been set up correctly, you can verify the installed packages using:
`pip list`
This will show you all the installed packages and their versions.

7. Running the Project: `python -m src.main`. You must be in "ekokalk" directory


Troubleshooting
- Missing Dependencies: If you run into missing dependencies errors, check the requirements.txt file for the correct package names and versions.
- Permission Issues on Linux: If you get a Permission denied error while installing packages, try adding sudo before the pip install command:
sudo pip install -r requirements.txt
