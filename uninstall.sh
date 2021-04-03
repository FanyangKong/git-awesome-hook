# 移除掉已存在的软链接
hookCmd=/usr/local/bin/githook
if [ -f "$hookCmd" ]
then
    rm $hookCmd
fi

projPath=~/.git_hook_path
if [ -f "$projPath" ]
then
    rm $projPath
fi

echo "Uninstall Success！\n\nRun 'git config --local --unset core.hooksPath' to reset your project's git-hook path"
