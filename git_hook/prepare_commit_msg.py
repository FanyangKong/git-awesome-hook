#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
import sys, os
import shutil
import re

from git_utils import *

""" 三个参数的意义
It takes one to three parameters. The first is the name of the file that contains the commit log message. 
The second is the source of the commit message, and can be: 
	message (if a -m or -F option was given); 
	template (if a -t option was given or the configuration option commit.template is set);
	merge (if the commit is a merge or a .git/MERGE_MSG file exists); 
	squash (if a .git/SQUASH_MSG file exists); 
	or commit, followed by a commit SHA-1 (if a -c, -C or --amend option was given).
"""

def get_file_content(file_path):
	content = ""
	with open(file_path, "rb") as f:
		content = f.read()
	return content

def write_commit_msg(file_path, extra_info):
	bakPath = file_path + ".bak"
	shutil.copyfile(file_path, bakPath)

	with open(file_path, 'w') as f:
		f.write(extra_info)
		f.write(get_file_content(bakPath))

def main():
	commit_msg_filepath = sys.argv[1]
	commit_source = sys.argv[2]
	commit_sha1 = sys.argv[3]
	
	if len(commit_source) != 0: # 现在只处理 git commit这一种形式，其它的用原始的git处理
		exit(0)

	branch_name = get_branch_name()
	extra_info = ""
	if branch_name.startswith("fix/bug"):
		matchObj = re.match("fix/bug([0-9]*)_",branch_name)
		if matchObj:
			extra_info = "\n--bug=" + matchObj.group(1) + "\n"

		write_commit_msg(commit_msg_filepath, extra_info)

	elif branch_name.startswith("feature/"): # feature分支如果拿不到id，就算了
		matchObj = re.search("story([0-9]*)_",branch_name)
		if matchObj:
			extra_info = "\n--story=" + matchObj.group(1) + "\n"
			
		write_commit_msg(commit_msg_filepath, extra_info)

if __name__=="__main__":
	main()