Project: Tournament Results  - Marianna Kreidler
================================

Required Libraries and Dependencies
-----------------------------------
This database only requires the included classes in Python 2.7’s library and the instructions below assume you also have Vagrant and Virtual Box installed on your machine.


How to Run Project
------------------
Fork the repository on github
Clone this project to your local machine
Open a terminal window
Change directory to vagrant/fullstack/vagrant/
Run command 'vagrant up' to start the virtual server
Run command 'vagrant ssh' to communicate with the server
Run command 'cd /vagrant'
Run command 'cd tournament'
Run command 'psql' to run Postgresql commands and communicate with the database
Run command '\i tournament.sql' to import the database file from this project and set up the database on your local machine
Exit Postgresql by pressing Ctrl+D
Run command 'python tournament_test.py' to test the tournament


Extra Credit Description
------------------------
Hopefully in the coming weeks I'll attempt the extra credit portions and resubmit.