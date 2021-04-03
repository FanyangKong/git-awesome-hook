# -*- coding: UTF-8 -*-

import subprocess


# git 操作工具方法

"""
获取分支名称
"""
def get_branch_name():
    branch_cmd = "git symbolic-ref --short -q HEAD"
    branch = subprocess.Popen(branch_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret = branch.communicate()
    branch_name = ret[0]
    return branch_name