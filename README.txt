STUDENT MANAGEMENT SYSTEM - MARIADB

IMPORTANT:
1. MariaDB Server must already be installed and running.
2. This project uses Python + Flask + MariaDB.

STEP 1 - Open MariaDB
Open Command Prompt and type:
mariadb -u root -p

Enter your MariaDB password.

STEP 2 - Create the database
Inside MariaDB, run:
source database.sql

If source does not work, open the database.sql file and copy-paste its SQL commands into MariaDB.

Then type:
exit

STEP 3 - Open this project folder in Command Prompt
Go to the folder containing app.py and requirements.txt.

Example:
cd Desktop\student_management_mariadb_simple

STEP 4 - Install Python packages
pip install -r requirements.txt

STEP 5 - Set your MariaDB password
Open app.py.

Find:
"password": "YOUR_MARIADB_PASSWORD"

Replace YOUR_MARIADB_PASSWORD with your actual MariaDB root password.

Example:
"password": "12345"

Save app.py.

STEP 6 - Run the website
In Command Prompt:
python app.py

You should see a message containing:
http://127.0.0.1:5000

STEP 7 - Open the website
Open Chrome and go to:
http://127.0.0.1:5000

You can:
- Add students -> INSERT
- View students -> SELECT
- Search students -> SELECT + WHERE + LIKE
- Edit students -> UPDATE
- Delete students -> DELETE

IMPORTANT:
requirements.txt does NOT install MariaDB Server.
It installs the Python MariaDB connector.

requirements.txt contains:
Flask
mariadb
