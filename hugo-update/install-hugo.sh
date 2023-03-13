#! /usr/bin/env bash

cd /path/to/hugo/deb/file

# Install deb from the last 24 hours
find *.deb -maxdepth 1 -mmin -1440 | xargs -d '\n' dpkg -i

# Remove debs more than 2 days old
find *.deb -maxdepth 1 -mtime +2 | xargs -d '\n' rm -rf 
