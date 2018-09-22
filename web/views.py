from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from backweb.models import Blog_category, Blog_article, Users,Comment

from django.http import HttpResponseRedirect



#主页
def index(request):
    if request.method == 'GET':
        categorys = Blog_category.objects.all()
        user_id = request.session.get('user_id')
        articles_list = Blog_article.objects.filter(user_id=user_id).order_by('-id')
        page_num = int(request.GET.get('page', 1))
        paginator = Paginator(articles_list, 10)
        page = paginator.page(page_num)
        articles = page.object_list
        return render(request, 'web/index.html',
                      {'articles': articles, 'page': page, 'articles_list': articles_list,'categorys':categorys })
#查看指定文章
def show_article(request,num):
    if request.method == 'GET':
        article_title = Blog_article.objects.filter(id=num).first()
        comments = Comment.objects.filter(belong_article=article_title)
        article = Blog_article.objects.filter(id=num).first()
        id=article.user_id
        user = Users.objects.filter(id=id).first()
        return render(request,'web/show_article.html',{'article':article,'user':user,'comments':comments})


#根据栏目查看文章
def category_article(request,num):
    if request.method == 'GET':
        articles = Blog_article.objects.filter(category_id=num)
        category = Blog_category.objects.filter(id=num).first()
        return render(request,'web/category_article.html',{'articles':articles,'category':category})

#增加评论
def add_comment(request,num):
    if request.method == 'POST':
        comment_get = request.POST
        observer = comment_get.get('observer')
        content = comment_get.get('content')
        article = Blog_article.objects.filter(id=num).first()
        Comment.objects.create(observer=observer,content=content,belong_article=article)
        return HttpResponseRedirect(reverse('web:show_article',kwargs={'num':num}))
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('web:show_article',kwargs={'num':num}))


def list(request,num):
    if request.method == 'GET':
        if request.session.get('user_id'):
            user_id = request.session.get('user_id')
        if num:
            user_id =num
        categorys = Blog_category.objects.all()
        articles_list = Blog_article.objects.filter(user_id=user_id).order_by('-id')
        page_num = int(request.GET.get('page', 1))
        paginator = Paginator(articles_list, 10)
        page = paginator.page(page_num)
        articles = page.object_list
        return render(request,'web/list.html',{'categorys':categorys,'articles': articles, 'page': page, 'articles_list': articles_list,})