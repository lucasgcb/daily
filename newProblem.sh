#!/bin/sh
TODAY=$(date '+%B-%d-%g')
mkdir challenges/"$TODAY"
echo '# Problem for '$TODAY > challenges/"$TODAY"/README.md
cp -r boilerplates/* challenges/"$TODAY"