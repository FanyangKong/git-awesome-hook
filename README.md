# git-awesome-hook

## 用法

1.  `git clone https://github.com/FanyangKong/git-awesome-hook`
2.  `cd git-awesome-hook`
3. `./install.sh`
4. `cd [your git project root path]`
5. `githook` # 在需要使用hook的git项目根路径执行githook命令，实现在默认git-hook路径和本项目git-hook工具路径间来回切换

本项目脚本只考虑了macOS的使用场景，Windows系统暂未支持。项目旨在利用git提供的hook功能对提交的信息进行检查。脚本的功能依赖于本项目的存放路径，如果本项目存放路径发生了改变，请重新执行用法的2-5步骤。

## 已经生效的hook命令

+ pre-commit
+ prepare-commit-msg
+ commit-msg

### pre-commit

在本地代码仓库进行临时性修改操作，包括：注释代码/修改默认值/放开日志时，可以在修改的内容旁添加`@debug`注释。在代码提交前(commit前)脚本会检查暂存区文件的代码差异，如果新增的代码行中包含了"@debug"字符串，那么本次提交将被拒绝。因为这些修改不应该被提交到代码库中去。

### prepare-commit-msg

使用`git commit`方式进行代码提交时，对于有固定命名规则的bug分支，在生成commit信息时直接从分支名字中提取出bugid附加到提交信息中。对于无固定命名规则的feature分支，如果分支名中包含了`story([0-9]*)_`格式的信息，也会提取出来附加到commit信息中。

### commit-msg

提交commit信息时，如果bug分支没有添加`--bug=xxx`或者feature分支没有添加`--story=xxx`信息，那么提交将被拒绝。之前输入的commit信息会输出到终端里避免再次commit时需要重新输入提交内容。
