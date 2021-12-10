*****************************************************************************************
*											                                            *
*	OOAD Projekt by: Kevin Lucas Simon, Christina Bernhardt, Nelson Morais		        *
*	Python version: 3.9								                                    *
*	Django version: 3.2+								                                *
*	Ubuntu version: 20.04 or greater 						                            *
*											                                            *
*****************************************************************************************


Step 1- Ubuntu 20.04 oder ein neuren version installieren.

	1.1- Ubuntu updaten:
		$sudo apt update
		und anschliessend
		$sudo apt upgrade

 	1.2- OOADProjekt-SourceCode.zip entpacken.


Step 2- MySql installieren: $ sudo apt install mysql-server 

	2.1- MySql ausführen mit: 
		$ sudo mysql -u root.

	2.2- root user löschen: 
		mysql> DROP USER 'root'@'localhost';

	2.3- neuen root ohne psw erzeugen: 
		mysql> CREATE USER 'root'@'localhost' IDENTIFIED BY '';

	2.3- MySql Datenbank names "ShareCare_data" einrichten: 
		mysql> CREATE DATABASE ShareCare_data;

	2.4- MySql Previleges vergeben: 
		mysql> GRANT ALL ON ShareCare_data.* TO 'root'@'localhost';

	2.5- MySql Previleges flush:
		mysql> FLUSH PRIVILEGES;


Step 3- Python 3 und pip installieren: 

	3.1- $ sudo apt install python3.9

	3.2- $ sudo apt install python3-pip

	3.3- $ sudo apt-get install python3-mysqldb libmysqlclient-dev python-dev


Step 4- Django installieren:

	4.1- $ python3 -m pip install Django


Step 5- mit Terminal zur OOADProjekt ordner navigieren: $ cd dir_zu_OOADProjekt_ordner/

	5.1- Virtual enviorment starten: 
		$ source bin/activate

	5.2- MySql client installieren: 
		(ShareCare)$ pip3 install mysql-client

	5.3- Datenbank Tables erzeugen:
		(ShareCare)$ python3 manage.py migrate

	5.4- Server Starten:
		(ShareCare)$ python3 manage.py runserver	
	

Step 6- Web Browser öffnen und http://127.0.0.1:8000/ aufrufen.
