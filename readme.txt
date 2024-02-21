
    ______     _            __              __         __        __  _           
   / ____/__  (_)___  _____/ /_____ ___  __/ /_  _____/ /_____ _/ /_(_)___  ____ 
  / /_  / _ \/ / __ \/ ___/ __/ __ `/ / / / __ \/ ___/ __/ __ `/ __/ / __ \/ __ \
 / __/ /  __/ / / / (__  ) /_/ /_/ / /_/ / /_/ (__  ) /_/ /_/ / /_/ / /_/ / / / /
/_/    \___/_/_/ /_/____/\__/\__,_/\__,_/_.___/____/\__/\__,_/\__/_/\____/_/ /_/ 
                                                                                 

clone the repo to your local computer:
--  go to dir
--  git clone https://github.com/danielhaendel/feinstaubstation
--

Hallo Laura


How to use django:

User the .env file from Teams:
--  copy the file in the project folder 

Change the pyvenv.cfg in the venv folder
-- home = C:\in\your\dir\Local\Programs\Python\Python312
-- executable = C:\in\your\dir\Local\Programs\Python\Python312\python.exe
-- command = C:\in\your\dir\Programs\Python\Python312\python.exe -m venv C:\in\your\dir\Documents\dev\feinstaubstation\venv

Acivate the virtual enviroment:
--  venv\Scripts\activate

Start the django server:
--  python manage.py runserver (ggf. den port ändern und zb 9000 verwenden)

Make database Change:
--  python manage.py makemigrations
--  python manage.py migrate