### Setup and Run Instructions
## Prerequisites
Python 3.11.3
# Django (install via pip install django)
Installation

# Clone the repository:

git clone [git@github.com:azizhmd74/NewsApi.gitt cd Test](https://github.com/azizhmd74/NewsApi.git)

# # Create a virtual environment (optional but recommended):
( all after installing it - but in my case its already installed) 
python -m venv venv source venv/bin/activate # On Windows, use 'venv\Scripts\activate'

## Install dependencies:

pip install -r requirements.txt

##  Apply database migrations:

python manage.py makemigration
python manage.py migrate


# an important thing to do to make the update of the news in the database automatically via the django_crone library u need to run this commande : 
python manage.py crontab add  

### and u can test it by calling for the command :

python manage.py Save_update_news

###  Run the Application Start the development server:

python manage.py runserver

Open your browser and navigate to (http://127.0.0.1:8000/)

## Additional Steps
Create a superuser account for admin access:

python manage.py createsuperuser

Access the Django admin panel at (http://127.0.0.1:8000/admin/) using the superuser credentials.

and all links are mentioned in urlspy inside the application news_proxy 


#an important thing to do to make the update of the news in the database automatically via the django_crone library u need to run this commande :  python manage.py crontab add     
