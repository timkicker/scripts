#! /bin/bash

# get current path -> parameter as "run autopull.sh /path/to/repo/"
repo_path="$1"

if [[ -z "$repo_path" ]]; then

echo "filepath is empty!";

else

cd $repo_path
git submodule update --recursive --remote

# for updating
update_submodule="git submodule update --recursive --remote";
kill_container="docker kill `docker ps -aqf "name=classic-blog"`";
start_container="docker compose up --build -d";

cron_job="30 * * * * cd $repo_path && $update_submodule && $kill_container && $start_container";

crontab -l | { cat; echo "$cron_job"; } | crontab -

echo "git submodule will update every half hour in path $repo_path using the command $cron_job";

fi





