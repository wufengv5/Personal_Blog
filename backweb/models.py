from django.db import models


#博主信息表
class Users(models.Model):
    username = models.CharField(max_length=20,unique=True,null=False,verbose_name='用户名')
    password = models.CharField(max_length=255,unique=True,null=False,verbose_name='密码')
    # article = models.CharField(max_length=30,verbose_name='文章')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创造时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'users'

class UserTicket(models.Model):
    user = models.ForeignKey(Users)
    ticket = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        db_table ='user_ticket'

# 栏目表
class Blog_category(models.Model):
    name = models.CharField(max_length=30,unique=True)

    class Meta:
        db_table ='Blog_category'

#文章表
class Blog_article(models.Model):
    title = models.CharField(max_length=50)
    user =models.ForeignKey(Users)
    content = models.TextField(max_length=500,default='')
    click_count = models.IntegerField(default=0)
    data_publish = models.DateTimeField(auto_now_add=True)
    category =models.ForeignKey(Blog_category)
    tag = models.CharField(max_length=20)
    img = models.ImageField(upload_to='upload',null=True,verbose_name='图片')
    # users_like = models.ManyToManyField()


    class Meta:
        db_table = 'Blog_article'

# 标签表
class Blog_tag(models.Model):
    name = models.ManyToManyField(Blog_article)
    class Meta:
        db_table = 'Blog_tag'

# 公告表
class Notice(models.Model):
    title = models.CharField(max_length=30,unique=True)
    author = models.ForeignKey(Users)
    content = models.CharField(max_length=255,)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table ='Notice'

#评论表
class Comment(models.Model):
    observer = models.CharField(max_length=20,null=False)
    content = models.CharField(max_length=200,null=False)
    belong_article = models.ForeignKey(Blog_article)
    # author = models.ForeignKey(Users,null=True)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'