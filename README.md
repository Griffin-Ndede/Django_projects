# Django Projects
This repository contains a collection of Django projects that I am currently working on. Each project is housed in its own directory and has its own set of dependencies and configurations. Below is a brief overview of each project and instructions on how to set them up.

## Table of Contents

- [Project 1: ShareSpace_Blog]


## Project 1: Sharespace_Blog

### Overview
A simple blog application where users can read and write articles. This project demonstrates basic CRUD operations, user authentication, and template usage.

### Setup
1. Navigate to the project directory:
   ```bash
   cd sharespace_blog
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```



## Contribution Guidelines

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
