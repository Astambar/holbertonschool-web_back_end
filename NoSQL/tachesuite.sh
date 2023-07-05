sudo service mongod start
./tasks/reset_data.sh
cat 0-list_databases | mongo
cat 1-use_or_create_database | mongo
cat 2-insert | mongo my_db
echo "cat 3-all | mongo my_db"
cat 3-all | mongo my_db
cat 4-match | mongo my_db
cat 5-count | mongo my_db
cat 6-update | mongo my_db
cat 4-match | mongo my_db
#cat 7-delete | mongo my_db
cat 4-match | mongo my_db
./8-main.py
./9-main.py
echo "./10-main.py"
./10-main.py
