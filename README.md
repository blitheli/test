# test

# 20230402  初次创建

# 问题

- 使用vsc 界面的提交按钮无法提交

#
# 代理
代理文件地址: file:C:/Users/DELL/.gitconfig

git config --list --show-origin

#
# 基本配置
## 配置用户名
git config --global user.name "name"
## 配置邮箱
git config --global user.email "name@mail.com"

#
# Git命令
## 从远程clone到本地

git clone https://github.com/blitheli/***.git


## 本地修改，添加到本地暂存区
git add dir/filename # 添加指定文件
git add . # 添加所有已修改文件

## 提交到本地仓库
git commit -m "注释文字"

## 推送到远程仓库
git push    //推送到远程仓库
git push -u origin master # master可以更换为其他分支

## 从远程仓库拉取
git pull
git pull origin master # master可以更换为其他分支

