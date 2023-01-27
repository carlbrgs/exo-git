#!/bin/bash
# Change the following values to suit your local setup.
# Add this file on your .git/hooks/ and name it as 'pre-commit'
#
# The name of a database user with read access to the database.
DBUSER=carl
# The password associated with the above user. Leave commented if none.
DBPASS=psw
# The database associated with this repository.
DBNAME=dbtest
DBHOST=localhost
# The path relative to the repository root in which to store the sql dump.
DBPATH=sqldump
read -p "Sauvegarde de la base dans ce commit (y/[n]) ?" yn < /dev/tty
yn=${yn:n}
case $yn in
 [Yy]* )
 echo mysqldump -h $DBHOST -u $DBUSER -p$DBPASS $DBNAME > $DBPATH/$DBNAME.sql
 mysqldump -h $DBHOST -u $DBUSER -p$DBPASS $DBNAME > $DBPATH/$DBNAME.sql
 zip $DBPATH/$DBNAME.sql.zip $DBPATH/$DBNAME.sql
 git add $DBPATH/$DBNAME.sql.zip
 exit 0;;
 [Nn]* )
 exit 0;;
esac
exit 0