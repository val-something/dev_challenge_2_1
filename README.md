This is a README file to help structure projects. Sections marked with **Sample** should be replaced. Feel free to add/remove sections as needed.

# Project Title
**Developer Challenge 2_1, 2021**
This project is a response to Developer Challenge 2_1, used to assess backend developers. It is a web application using [Python 3.7.12](https://www.python.org/downloads/release/python-3712/) that uses [Django](https://www.djangoproject.com/) for a web server to expose basic CRUD operations on a [PostgreSQL](https://www.postgresql.org/) database, storing sample [piracy](https://www.kaggle.com/n0n5ense/global-maritime-pirate-attacks-19932020) data. Users are able to run a script from the command line (the *Python CLI*) to import a file and view the imported data in the admin page (the *Django Admin Site*).

## Design
### Data Model
<Add a discussion on designing the data model here>

**Sample:** 
Initial instinct was to just load everything into Postgres as a JSON blob object. But no. I've worked with enough relational databases a while back to know that's [not a good idea](https://www.2ndquadrant.com/en/blog/postgresql-anti-patterns-unnecessary-jsonhstore-dynamic-columns/). Relational databases exhibit better performance when indexing and querying for data in tabular format, so I normalise the semistructured csv data into different tables depending on the field 'type'. There are only 4 types documented in the [file format specifications](), making otherwise very wide/jagged tables a valid construction for implementing exclusive belongs-to relations. A discussion on alternatives is outlined below.

<Include an EER diagram if needed>

### Data Assumptions
<List all assumptions here>

**Sample:**
- Date/time data given in ingested files is already in UTC (no mention of timezone is provided in the file format document - time format checks and conversions are handled in Python rather than enforced by Postgres).
- The delimiter `#` can be used in composite key naming.

### Application Architecture
<Add a discussion on designing the application here>

<Include a UML diagram if needed>

### Application Assumptions
<List all assumptions here>

## Getting Started
These instructions will get a copy of the project up and running on a local machine. These instructions were written for WSL running Ubuntu 18.04 LTS.

### Prerequisites
1. Python 3.7.12 (https://www.python.org/downloads/release/python-3712)
2. Django (https://www.djangoproject.com/)
3. PostgreSQL (https://www.postgresql.org/)

Optional
- pyenv (https://github.com/pyenv/pyenv)

### Installing
These instructions will outline the components used in the project.

A basic copy of the project can be cloned via ssh using:
`git clone ssh://innersource.accenture.com/not_val/dev_challenge_2_1`

#### Python
Python is an interpreted programming language used to integrate all the components. A virtual environment (implemented via [pyenv](https://github.com/pyenv/pyenv)) is used to force Python 3.7.

The following commands will get a virtual environment set up.
Note: these instructions have been compiled from multiple sources.

1. Install pyenv dependencies:
```
apt install git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev zlib1g-dev libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev
```
2. Download and install pyenv:
```
curl https://pyenv.run | bash
```
3. Append the following lines to `~/.bashrc` to enable pyenv to shim (intercept and translate) Python, making sure to enter the correct username:
```
export PATH="/home/<<username>>/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
4. Source `~/.bashrc` to save these changes:
```
source ~/.bashrc
```
5. Install the required version of Python via pyenv:
```
pyenv install 3.7.12
```
6. Navigate to the project directory and create a virtual environment using Python 3.7.12:
```
cd dev_challenge_2_1/; pyenv virtualenv 3.7.12 dev_challenge_2_1_env
```
7. Activate the shimming to make sure Python 3.7.12 is used whenever the Python command is called:
```
pyenv local dev_challenge_2_1_env
```
*Great! Now whenever scripts are run inside the dev_challenge_2_1/ directory, Python 3.7.12 will automatically be used.*

#### Django
Django is a web application framework (a set of libraries and standards) in Python containing a lot of features out of the box. In this instance, the default admin site is used as the primary front-end interface.

The following commands will install dependencies and perform credentials setup for the Django component.

1. Install Django dependencies locally (make sure this is being run inside the `dev_challenge_2_1/` directory to ensure it's installing to the correct Python version):
```
pip install django django-admin psycopg2-binary pytest
```
2. Create a `credentials.py` file in `dev_challenge_2_1/sample_app/` to store service account credentials to enable Postgres integration (follow the specfile `dev_challenge_2_1/sample_app/credentials.py.spec`):
```
cp sample_app/credentials.py.spec sample_app/credentials.py; vi sample_app/credentials.py;
```
3. Run migrations to populate data models:
```
python manage.py migrate
```
4. Create a superuser to allow access to the admin page:
```
python manage.py createsuperuser
```
*Cool! Django has been installed and configured - the rest of the cloned project should be accessible now!*

#### PostgreSQL
PostgreSQL is a relational database management system (RDBMS) used here as a data store.

The following commands will get the PostgreSQL database set up.
Note: these instructions have been compiled from multiple sources.

1. Install postgres:
```
apt install postgresql postgresql-contrib
```
2. Start the postgres service:
```
service postgresql start
```
3. Set the password for the preset 'postgres' user to allow it to connect:
```
passwd postgres
```
4. Switch user:
```
su - postgres
```
5. Enter the Postgres CLI:
```
psql
```
6. Create the database `sample_data` to be used by the project:
```
create database sample_data;
```
7. Connect to the newly created database:
```
\c sample_data
```
8. Run the queries in `sample/queries.sql`. By the end, the output should look as:
```
<Insert verification data here>
```
9. Quit psql:
```
quit
```
10. Logout of the postgres user once back in the bash shell:
```
logout
```
*Neat! PostgreSQL is now set up and running on WSL with data to verify success.*

## Deployment
### Django Admin Site
1. Start the Postgres service if needed using `service postgresql start`.
2. Start the Django server using `python manage.py runserver 5431`.
3. Using a browser, navigate to `localhost:5431`.
4. Login to the admin page.
5. Validate.

- Live test instances: none
- Test data: none

### Python CLI
1. Run the command line import utility using `./python import_data.py <<path_to_data_file>>`.

## Testing
### Django Admin Site
Run unit test cases from the package home directory using `./python manage.py test`.

Test cases enumerated:
<Add numbered test cases here>

### Python CLI
Run a sample database connection from the package home directory using `./python import_data_unittests.py sample/xxx.csv test`.

Test cases enumerated:
<Add numbered test cases here>

## Contributing
Send me an [email](mailto:val.adrien.li@accenture.com)

### Limitations/Future work
<Add in missed items & improvements here>

**Sample:**
- ~~Complete the import command line function (branch: post_submission-1)~~
- Write unit test cases (branch: post_submission-2)
- Implement OOP practices on the data access functions (post_submission-3)

## Troubleshooting
- Awaiting feedback

## Authors
- **Val** - [val.adrien.li](mailto:val.adrien.li@accenture.com)

## License
This project is unlicensed.

## Acknowledgments
<Include any people & resources here>
