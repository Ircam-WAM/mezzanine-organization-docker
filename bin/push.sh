#!/bin/bash

echo "----------------------------"
echo `date +\%Y\%m\%d-\%H-\%M-\%S`
docker-compose exec db /srv/bin/db/backup.sh
cd var
git add .
git commit -a -m "update DB and media"
git pull
git push
