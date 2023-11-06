#!/bin/bash

n=$1  # Replace with the number of days ago you want

new_date="$(date -d "@$(( $(date +%s) - n * 86400 ))" "+%Y-%m-%d %H:%M:%S")"

GIT_COMMITTER_DATE="$new_date" git commit --amend --no-edit

