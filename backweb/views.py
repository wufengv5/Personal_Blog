from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.forms import UserForm
from backweb.models import Users, UserTicket, Blog_category, Blog_article, Notice,Comment
from utils.functions import get_ticket

#注册
def register(request):
    if request.method == 'GET':
        return render(request,'BackWeb/register.html')
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            # 加密密码
            password = make_password(cd['password'])
            Users.objects.create(username=cd['username'], password=password)
            return HttpResponseRedirect(reverse('back_web:login'))
        else:
            return HttpResponseRedirect(reverse('back_web:register'))

#登陆
def login(request):
    if request.method == 'GET':
        return render(request, 'BackWeb/login.html')
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            # 获取登陆的user对象
            cd = user_form.cleaned_data
            user = Users.objects.filter(username=cd['username']).first()
            if user:
                # 账户名验证通过，验证密码  使用check_password()方法
                if check_password(cd['password'], user.password):
                    # 验证通过 账号和密码都正确
                    # 设置随机参数ticket
                    # res = HttpResponseRedirect(reverse('back_web:index'))
                    # res = render(request,'BackWeb/index.html')
                    # ticket = get_ticket()
                    # res.set_cookie('ticket', ticket, max_age=1000)
                    # # 在user_ticket存储ticket和user的关系
                    # UserTicket.objects.create(ticket=ticket, user=user)
                    # 返回一个绑定ticket的地址
                    request.session['user_id'] = user.id
                    # return render(request,'BackWeb/index.html')
                    return HttpResponseRedirect(reverse('back_web:index'))

                else:
                    # 密码错误
                    return render(request, 'BackWeb/login.html')
            else:
                # 账号错误
                return render(request, 'BackWeb/login.html')

#注销
def logout(request):
    if request.method == 'GET':
        request.session.flush()
        return HttpResponseRedirect(reverse('back_web:login'))
    else:
        return render(request,'BackWeb/index.html')
#总览
def index(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        articles = Blog_article.objects.filter(user_id=user_id)
        notices = Notice.objects.filter(author_id=user_id)
        comments = Comment.objects.filter(belong_article__in=articles)
        return render(request,'BackWeb/index.html',{'articles':articles,'notices':notices,'comments':comments})

#文章
def article(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        articles_list = Blog_article.objects.filter(user_id=user_id)
        page_num = int(request.GET.get('page',1))
        paginator = Paginator(articles_list,3)
        page = paginator.page(page_num)
        articles = page.object_list
        return render(request,'BackWeb/article.html',{'articles':articles,'page':page,'articles_list':articles_list,})
#新增文章
def add_article(request):
    if request.method == 'GET':
        #显示栏目
        categorys = Blog_category.objects.all()
        return  render(request,'BackWeb/add-article.html',{'categorys':categorys,})
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = request.POST
        Blog_article.objects.create(
            title=user.get('title'),
            content=user.get('content'),
            category_id=user.get('category'),
            user_id=user_id,
            img=request.FILES.get('img'))
        return HttpResponseRedirect(reverse('back_web:article'))
#删除文章
def del_article(request,num):
    if request.method == 'GET':
        Blog_article.objects.filter(id=num).delete()
        return HttpResponseRedirect(reverse('back_web:article'))
#查看文章
def show_article(request,num):
    if request.method == 'GET':
        article = Blog_article.objects.filter(id=num).first()
        id=article.user_id
        user = Users.objects.filter(id=id).first()
        return render(request,'BackWeb/show_article.html',{'article':article,'user':user})

#更新文章
def update_article(request,num):
    if request.method == 'GET':
        article = Blog_article.objects.filter(id=num).first()
        categorys = Blog_category.objects.all()
        id = article.user_id
        user = Users.objects.filter(id=id).first()
        return render(request, 'BackWeb/update_article.html', {'article': article, 'user': user,'categorys':categorys})
    if request.method == 'POST':
        article = Blog_article.objects.filter(id=num).first()
        user = request.POST
        article.title = user.get('title')
        article.content = user.get('content')
        article.category_id = user.get('category')
        if request.FILES.get('img'):
            article.img = request.FILES.get('img')
        article.save()
        return HttpResponseRedirect(reverse('back_web:article'))

#删除文章图片
def del_img(request):
    if request.method == 'GET':
        pass

#公告
def notice(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        notice_list = Notice.objects.filter(author_id=user_id)
        page_num = int(request.GET.get('page', 1))
        paginator = Paginator(notice_list, 3)
        page = paginator.page(page_num)
        notices = page.object_list
        return render(request,'BackWeb/notice.html',{'notices':notices,'page':page,'notice_list':notice_list})

#增加公告
def add_notice(request):
    if request.method == 'GET':
        return render(request,'BackWeb/add-notice.html')
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        notice = request.POST
        Notice.objects.create(
            title=notice.get('title'),
            content=notice.get('content'),
            author_id=user_id)
        return HttpResponseRedirect(reverse('back_web:notice'))

#删除公告
def del_notice(request,num):
    if request.method == 'GET':
        Notice.objects.filter(id=num).delete()
        return HttpResponseRedirect(reverse('back_web:notice'))

# 查看公告
def show_notice(request, num):
    if request.method == 'GET':
        notice = Notice.objects.filter(id=num).first()
        id = notice.author_id
        user = Users.objects.filter(id=id).first()
        return render(request, 'BackWeb/show_notice.html', {'notice': notice, 'user': user})

#评论
def comment(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        articles =Blog_article.objects.filter(user_id=user_id)
        articles_title = articles.values('title')
        comments = Comment.objects.filter(belong_article__in=articles_title)
        return render(request,'BackWeb/comment.html',{'comments':comments})

#删除评论
def del_comment(request,num):
    Comment.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('back_web:comment'))


#栏目
def category(request):
    if request.method == 'GET':
        categorys = Blog_category.objects.all()

        return render(request,'BackWeb/category.html',{'categorys':categorys})
#增加栏目
def add_category(request):
    if request.method == 'POST':
        new_category = request.POST.get('new_category')
        Blog_category.objects.create(name=new_category)
        return HttpResponseRedirect(reverse('back_web:category'))
#删除栏目
def del_category(request,num):
    Blog_category.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('back_web:category'))
