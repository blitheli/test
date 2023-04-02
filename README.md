# test

# 20230402  初次创建


# git过程测试
- 不用打开代理，直接使用vsc拉取按钮成功更新了本地33
- 不用打开代理，直接使用git命令推送按钮成功更新了本地44
- 打开代理，浏览器不用打开代理，直接使用vsc拉取按钮成功更新了本地33
- vsc 推送按钮成功！
- 笔记本修改，测试！
- 在线修改，again!

- 使用vsc 界面的提交按钮无法提交

#
## 代理
代理文件地址: file:C:/Users/DELL/.gitconfig

git config --list --show-origin

#
## 基本配置
### 配置用户名
git config --global user.name "name"
### 配置邮箱
git config --global user.email "name@mail.com"

#
## Git命令

### 不设置代理，试试看 
git config --global --unset https.proxy

git config --global --unset http.proxy

### 从远程clone到本地

git clone https://github.com/blitheli/***.git

### 本地修改，添加到本地暂存区
git add dir/filename # 添加指定文件
git add . # 添加所有已修改文件

### 提交到本地仓库
git commit -m "注释文字"

### 推送到远程仓库
git push    //推送到远程仓库(多试几次)
git push -u origin master # master可以更换为其他分支

### 从远程仓库拉取
git pull
git pull origin master # master可以更换为其他分支

