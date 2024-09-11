# **SavePals**

SavePals is a collaborative savings platform that allows friends to save money together by setting group goals, tracking progress, and managing contributions. Built with Flask, the application provhrefes a streamlined and user-friendly interface for managing group savings plans, making financial collaboration easier and more transparent.

**Table of Contents**

- <a href="#features">Features</a>
- <a href="#stack">Tech Stack</a>
- <a href="#install">Installation</a>
- <a href="#setup">Setup</a>
- <a href="#env">Environment Variables</a>
- <a href="#usage">Usage</a>
- <a href="#api">API Endpoints</a>
- <a href="#contribute">Contributing</a>
- <a href="#licence">Licence</a>


<h2 id="features">Features</h2>

1. Create and Manage Groups: Create savings groups with specific goals, track progress, and manage contributions.

2. Contribution Management: Easily contribute to group goals and see indivhrefual progress.

3. Group Progress Visualization: View group progress with dynamic progress bars and financial summaries.

4. User Authentication: Secure login and logout functionality.

5. Interactive Dashboard: A personalized dashboard displaying group details, contribution options, and more.

<h2 id="stack">Tech Stack</h2>

1. Frontend: HTML, CSS, JavaScript (jQuery)

2. Backend: Flask (Python)

3. Database: PostgreSQL with SQLAlchemy ORM

4. Styling: Custom CSS with a focus on dark themes

5. Deployment: -

<h2 id="install">Installation</h2>

**Prerequisites**

- Python 3.12+
- PostgreSQL
- Node.js and npm (for frontend dependencies)
- Virtualenv (recommended)

**Clone the Repository**

- go to your bash
- git clone https://github.com/luckys-lnz/savepals.git
- cd savepals
- Create a Virtual Environment
- go to your bash
- python3 -m venv .venv
- source .venv/bin/activate

**Install Backend Dependencies**

- go to your bash
- yay -S psql or sudo apt install psql or sudo pacman -S psql
- visit psql documentation page to set up the needed configurations

**Create a PostgreSQL database:**

- got your bash
- sudo -i -u postgres
- createdb savepals_db
- Set up the database schema:

**Create a .env file in the project root with the following variables:**

- FLASK_APP=run.py
- FLASK_ENV=development
- DATABASE_URL=postgresql://<username>:<password>@localhost:5432/savepals_db
- SECRET_KEY=your_secret_key
- Replace <username> and <password> with your PostgreSQL credentials.

<h2 id="setup">Setup</h2>

**Database Configuration**

Create a PostgreSQL database:
- got your bash

- ``
createdb savepals_db
``

- Set up the database schema:

- Run the migrations or use an initial setup script:

- `flask db upgrade
`

<h2 id="env">Environment Variables</h2>

**Create a .env file in the project root with the following variables:**

`FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/savepals_db
SECRET_KEY=your_secret_key
`

Replace `<username>` and `<password>` with your PostgreSQL credentials.

- Initial Data Setup
(Optional) Populate the database with initial data if needed:

`flask seed`

<h2 id="usage">Usage</h2>

**Running the Application**

*Activate the virtual environment:*

`source .venv/bin/activate`

*Start the Flask server:*

`flask run`

*Access the application:*

Open your browser and navigate to http://127.0.0.1:5000.


<h2 id="api">API Endpoints</h2>

***Group Management**

*Get All Groups*

- URL: /api/v1/groups
- Method: GET
- Description: Retrieves a list of all groups.

*Create Group*

- URL: /api/v1/groups
- Method: POST
- Description: Creates a new group.

*Contribution Management*
- Contribute to a Group
- URL: /api/v1/groups/<group_id>/contribute
- Method: POST
- Description: Adds a contribution to a specified group.

*User Authentication*

- Login
- URL: /login
- Method: POST
- Description: Authenticates a user and starts a session.

- Logout
- URL: /logout
- Method: GET
- Description: Logs out the user and ends the session.

*Error Handling*

- Ensure proper error handling for cases like invalid group IDs, unauthorized access, and server errors.

<h2 id="contribute">Contributing</h2>

**We welcome contributions! To contribute:**

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Make your changes and commit (git commit -m 'Add feature').
4. Push to the branch (git push origin feature/your-feature-name).
Open a pull request.
4. Code Style
Follow PEP 8 for Python code. Ensure that your code is properly formatted and linted.

<h2 id="licence">License</h2>
This project is licensed under the MIT License - see the LICENSE file for details.

Custom License

Copyright (c) 2024 
- Lucky Archibong, 
- Deantosh Daiddoh, 
- Benedict Abudu

Permission to Contribute: Permission is hereby granted to any person or organization to contribute to this project by submitting code, suggestions, or documentation. Contributions are welcome, but must be submitted via pull request and are subject to review and approval by the project maintainer.

<h4>Restrictions on Use:</h4>

<h5>No Redistribution:</h5> You are not permitted to publish, distribute, sublicense, or sell any portion of this software, its concepts, or any derivative works without explicit, written permission from the copyright holder.

<h5>No Public Use:</h5> The project, its code, and any associated ideas are personal intellectual property and may not be shared publicly, used in commercial or non-commercial contexts, or presented as your own work.

<h5>No Modification for Personal Use:</h5> Modifying, creating derivative works, or using any part of this project for personal or external projects is strictly prohibited.

<h5>Disclaimer:</h5> The software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the author or copyright holder be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software