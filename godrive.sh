#!/bin/bash

/usr/bin/rclone copy --update \
    --verbose --transfers 30 \
    --checkers 8 --contimeout 60s \
    --timeout 300s --retries 3 \
    --low-level-retries 10 \
    --stats 20s \
    --log-file /var/log/rclone/godrive.log \
    "/srv/" --exclude-from "/srv/rclone/exclude.txt" "godrive:storage"