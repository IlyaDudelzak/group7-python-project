    # Personal assistant

    Welcome to the Personal assistant! This repository contains the source code for Python project built with Django, PostgreSQL, and Poetry.

    ## Table of Contents

    - [Project Overview](#project-overview)
    - [Features](#features)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Contributing](#contributing)
    - [License](#license)
    - [Contact](#contact)

    ## Project Overview

    This project is a web application developed using Django. It allows users to manage contacts and notes, store files.

    ## Features

    - Contact management
    - Notes creation and editing
    - Display of current news
    - File upload and storage
    - Built with Django + PostgreSQL + Poetry

    ## Installation

    1. Clone the repository:
        ```bash
        git clone https://github.com/Alexandr-1973/group7-python-project.git
        ```
    2. Navigate to the project directory:
        ```bash
        cd group7-python-project
        ```
    3. Install Poetry if you haven't already:
        ```bash
        pip install poetry
        ```
    4. Install dependencies using Poetry:
        ```bash
        poetry install
        ```
    5. Set up PostgreSQL database.
        ```bash
        docker compose up -d
        ```
    6. Navigate to the project directory:
        ```bash
        cd personal_assistant
        ```
    7. Apply migrations:
        ```bash
        python manage.py migrate
        ```

    ## Usage

    To start the development server, run:
    ```bash
    python manage.py runserver
    ```

    ## Contributing

    Contributions are welcome! Please open issues or submit pull requests for improvements.

    <!-- ## License

    This project is licensed under the MIT License.

    ## Contact

    For questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com). -->