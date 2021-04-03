# 获取脚本所在当前路径
shell_path=$(cd "$(dirname "$0")";pwd)

# 移除掉已存在的软链接
file=/usr/local/bin/githook
if [ -f "$file" ]
then
    rm /usr/local/bin/githook
fi

# 把githook脚本链接到用户命令目录
ln -s ${shell_path}/githook /usr/local/bin

# 将git-awesome-hook的路径写到用户路径下
description="${shell_path}\n#这是git-awesome-hook仓库用来记录hook脚本路径的文件"
echo ${description} > ~/.git_hook_path

echo "Install Success！"
