install docker 
docker pull postgres
docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=postgres -d postgres
docker exec --it postgres bash
    psql -U postgres" 
        create database trends;
        create user trends_user with password 'password';
        grant all privileges on database trends to trends_user;  

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python track_trends.py
python manage.py runserver
http://127.0.0.1:8000/