mysql -u root -e 'create database ask;'
mysql -u root -e "create user 'myuser'@'localhost' identified by 'mypasswd';"
mysql -u root -e "grant alll privileges on *.* to 'myuser'@'localhost';"


