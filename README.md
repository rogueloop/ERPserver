# ERP backend setup 


1. Setup python poetry localy 
https://python-poetry.org/docs/#installing-with-the-official-installer

2. Run `poetry install` (installs the dependenies just like yarn of npm)
2. Run  `poetry shell` (setting up virtual env )
3. Run `poetry run python manage.py runserver`


* For adding more packages use `poetry add` command instead of using pip
# successfully cloned by ajmal 

# Apps created
1. Marketing (25/2/23) by ajmal


# configuration of postgresql

    ## user
         CREATE USER sammy WITH PASSWORD 'pa$$word';


# Making migrations 
1. create migratiosns 
`poetry run python manage.py makemigrations`
2. Run the following command to apply the migrations to your database
```poetry run python manage.py migrate```