#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

# COMMIT_MSG_FILE=$1
# COMMIT_SOURCE=$2
# SHA1=$3

import sys, os
import re

from git_utils import *

commit_msg_filepath = sys.argv[1]

branch_name = get_branch_name()

commit_msg = ""
if branch_name.startswith("fix/bug"):
	with open(commit_msg_filepath, 'r') as f:
		lines = f.readlines()
		for line in lines:
			if line.startswith("#"):
				break
			commit_msg += line
		commit_msg = commit_msg.rstrip()	
		searchObj = re.search("--bug=[0-9]+", commit_msg)
		if not searchObj:
			print "Commit Failed (～￣(OO)￣)ブ  , no bugid" + "\n\nInvalid Message:\n" + commit_msg
			exit(1)
elif branch_name.startswith("feature/"):
	with open(commit_msg_filepath, 'r') as f:
		lines = f.readlines()
		for line in lines:
			if line.startswith("#"):
				break
			commit_msg += line
		commit_msg = commit_msg.rstrip()
		searchObj = re.search("--story=[0-9]+", commit_msg)
		if not searchObj:
			print "Commit Failed (～￣(OO)￣)ブ  , no storyid" + "\n\nInvalid Message:\n" + commit_msg
			exit(1)

	