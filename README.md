This repository contains my personal scripts for daily usage.
To obtain a specifc one, you may use  `curl -o <filename> <raw-link-to-file>`

**Scripts**

Name | Description| Lang 
---|---|---
[auto_submodule.sh](./scripts/classic-blog-auto-pull/) | Creates a cron job that updates all git submodules every 30min in a specific folder/repo. Used in my [alternative frontend](https://github.com/timkicker/classic-blog)| bash 
[image-sorter](./scripts/image-sorter/) | Sort images into year-folders, also tries to determine the date if not saved in metadata| c# 
[maloja-duplicate-finder](./scripts/maloja-duplicate-finder/) | Find duplicate scrobbles in a maloja database| python 
[maloja-import-converter](./scripts/maloja-import-converter/) | Parse maloja importfiles from [last.fm](https://lastfm.ghan.nl/export/) into new format | python 
[reassign-workspaces](./scripts/reassign-workspaces/) | Move i3-workspaces from disconnected monitor to active one | bash 

**Additional**

Name | Description
---|---
[Manual maloja scrobbler](https://github.com/timkicker/maloja-manual-scrobbler) | Script for manually scrobbling to my maloja instance. Not included as this project has its own repo