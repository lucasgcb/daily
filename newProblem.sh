#!/bin/sh
TODAY=$(date '+%B-%d-%g')
mkdir "$TODAY"
echo '# Problem for '$TODAY > "$TODAY"/README.md
cp -r boilerplates/* "$TODAY"