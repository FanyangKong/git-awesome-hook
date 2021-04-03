#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import subprocess

TEMP_CODE = "@debug"

# staged_files_cmd = "git ls-files | grep '.txt' '.java' '.gradle' '.xml' '.sh'"
staged_files_cmd = "git diff --cached --name-only --diff-filter=ACM -- '*.txt' '*.java' '*.gradle' '*.xml' '*.sh'"
diff_cmd = "git diff --cached {}"

# 获取暂存的文件列表
staged_files_ret = subprocess.Popen(staged_files_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# 逐个检查暂存文件新增的代码行是否有禁止提交的内容
staged_files = staged_files_ret[0].strip().split('\n')

hasDebugInfo = False
for file in staged_files:
	# print diff_cmd.format(file)
	diff_ret = subprocess.Popen(diff_cmd.format(file), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	diff_lines = diff_ret[0].strip().split('\n')
	# print diff_lines
	for i in range(len(diff_lines)):
		if diff_lines[i].startswith("+") and TEMP_CODE in diff_lines[i]:
			hasDebugInfo = True
			# 最多给出五行提示信息
			msg = (
				"\n" + diff_lines[i] + "\n" +
				((diff_lines[i + 1] + "\n") if i + 1 < len(diff_lines) else "") +
				((diff_lines[i + 2] + "\n") if i + 2 < len(diff_lines) else "") +
				((diff_lines[i + 3] + "\n") if i + 3 < len(diff_lines) else "") +
				((diff_lines[i + 4] + "\n") if i + 4 < len(diff_lines) else "")
				)

			print "@debug should not be commit in file:\n" + file + msg
        

if hasDebugInfo:
	exit(1)