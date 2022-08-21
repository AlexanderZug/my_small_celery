# my_small_celery

Small project written with celey. It has one model and can create new model objects each 15 seconds.

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

> Install Python (if it's not installed), preferably starting with version 3.8<br>
> [Download Python3](https://www.python.org/downloads/release/python-3910/)

Clone the repository:
```
git clone https://github.com/AlexanderZug/my_small_celery
```


Go to folder:
```
cd my_small_celery
```

Install requirements:
```
pip3 install -r requirements.txt
```

Do migrations:
```
python3 manage.py migrate
```

To start the project you should start Docker first, then introduce the following commands in different seals of the terminal:
```
python3 manage.py runserver
```
```
docker-compose up
```
```
celery -A proj beat
```
```
celery -A proj worker -l INFO --pool=solo
```
