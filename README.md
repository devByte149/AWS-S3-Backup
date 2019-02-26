# AWS-S3-Backup
Python script used to get the directiry structure of path given folder and upload contents to Amazon web service secure storage

~Need to add the local path of contents needed to be backed up.
~Initially used to backup a workserver to amazon's secure storage through their AWS CLI. There is a copy command, cp, that can be used but
this script uses sync as it can sync all contents to existing folders and upload new folders as well. The cp command was throwing an error and not
finishing due to enormous file size of our server, 4tb.
