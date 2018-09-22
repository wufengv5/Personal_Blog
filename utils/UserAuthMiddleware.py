from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from backweb.models import UserTicket, Users


class UserMiddleware(MiddlewareMixin):
    #重构拦截请求的方法
    #名字不能修改
    def process_request(self,request):
        #首先先排除不需要登陆就能访问的网站

        not_login_path = [
            '/back_web/login/',
            '/back_web/register/',
            ]
        #得到当前的路径，并且排除是否是不需要登陆的网站
        path = request.path
        for url in not_login_path:
            if url == path:
                #如果相等，则不需要验证登陆,则之间返回none 进行下一步
                return  None
        # #得到请求绑定的ticket
        # ticket = request.COOKIES.get('ticket')
        # #如果没有ticket 则转向登陆界面
        # if not ticket:
        #     return HttpResponseRedirect(reverse('back_web:login'))
        # user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        # #如果没有在userticket中获取到对应的ticket，则也转向登陆界面
        # if not user_ticket:
        #     return HttpResponseRedirect(reverse('back_web:login'))
        #返回一个全局的user

        if  request.session.get('user_id'):
            request.user = Users.objects.filter(id=request.session.get('user_id'))
            return None
        else:
            return HttpResponseRedirect(reverse('back_web:login'))






