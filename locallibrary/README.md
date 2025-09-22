1 клонировать
git clone https://github.com/emimagomerzaev987/simpleLibrary.git
2 создать виртуальное окружение
python -m venv venv
python .venv\Scripts\activate
pip install -r requirements.txt
3 выполнить миграции
python manage.py makemigrations
python manage.py migrate
4 создать суперпользователя
python manage.py runserver 
5 запустить
python manage.py runserver 



