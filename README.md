# 个人博客项目

项目说明:项目分为后台管理和前端展示两个部分。

## 1.后台管理

后台管理分为了总览，文章，公告，评论，栏目，登录，注册

文章实现的功能为查看当前登录账号下的所有文章，可以新加文章，修改文章，删除文章，查看文章，并且添加了ediotr.md插件 文章可以改用MackDown格式，并且也可以附上图片。

公告实现的功能是增删查改公告，并且会在前端展示页面上显示最新的公告。

评论实现的公告是查看游客给当前用户的文章的评论，并且有删除评论的功能。

栏目实现的功能是增删查改所有的栏目，并且可以查看任意栏目下的所有文章

## 2.前端展示

前端最主要的就是展示博客主写的文章。

新添的功能是每一篇文章下面会有一个评论，但是并没有实现游客注册，所以评论只需要输入用户名和评论，提交后就会立刻显示在评论栏。


不足的地方：1 没有实现游客注册登录进行查看文章进行留言功能。
           2  排版问题
           3 没有使用api数据接口，数据暴露。

