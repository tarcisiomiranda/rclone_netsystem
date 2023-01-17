# https://rclone.org/flags/
# https://rclone.org/commands/
# https://forum.rclone.org/t/help-with-filtering-excluding-syntax-please/12005/18


# Script Python
50 19   * * *   root /usr/bin/python3 /srv/rclone/godrive.py >> /var/log/pycloud/godrive.log 2>&1
# 55 23   * * *   root /usr/bin/python3 /srv/rclone/dropbox.py >> /var/log/pycloud/dropbox.log 2>&1
