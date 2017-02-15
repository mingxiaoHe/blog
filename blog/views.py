#coding=utf-8
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db.models import Count
from django.conf import settings
from models import *
import logging
logger = logging.getLogger('blog.views')
from blog import html_helper,common
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def global_setting(request):
    category_list = Category.objects.all()
    archive_list = Article.objects.distinct_date()
    article = Article.objects.all()
    tag_list = Tag.objects.all()
    return locals()

def index(request,page):
    murl = 'index'
    page = common.try_int(page,1)
    count = Article.objects.all().count()
    pageObj = html_helper.PageInfo(page,count,per_item=10)
    data = Article.objects.all()[pageObj.start:pageObj.end]
    page_string = html_helper.Pager(page,pageObj.all_page_count,murl)
    return render(request,'index.html',locals())

def tag(request,tag,page):
    murl = str('tag/' + tag)
    page = common.try_int(page, 1)
    tag = Tag.objects.get(name=tag)
    count = Article.objects.filter(tag=tag.id).count()
    pageObj = html_helper.PageInfo(page, count, per_item=10)
    data = Article.objects.filter(tag=tag.id)[pageObj.start:pageObj.end]
    page_string = html_helper.Pager(page, pageObj.all_page_count, murl)

    return render(request, 'tag.html', locals())

def category(request,category,page):
    murl = str('category/' + category)
    page = common.try_int(page,1)
    category = Category.objects.get(name=category)
    count = Article.objects.filter(category=category.id).count()
    pageObj = html_helper.PageInfo(page,count,per_item=10)
    data = Article.objects.filter(category=category.id)[pageObj.start:pageObj.end]
    page_string = html_helper.Pager(page,pageObj.all_page_count,murl)
    return render(request, 'category.html', locals())

def archive(request,year,month,page):
    murl = str('archive/' + year + '/' + month)
    page = common.try_int(page,1)
    archive_y_m = year + "年"+ month + "月"
    count = Article.objects.filter(date_publish__icontains=year+'-'+month).count()
    pageObj = html_helper.PageInfo(page,count,per_item=20)
    data = Article.objects.filter(date_publish__icontains=year+'-'+month)[pageObj.start:pageObj.end]
    page_string = html_helper.Pager(page,pageObj.all_page_count,murl)
    return render(request, 'archive.html', locals())

def article(request):
    try:
        id = request.GET.get('id', None)
        try:
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    except Exception as e:
        logger.error(e)
    return render(request, 'article.html', locals())

def about(request):
    return render(request,'about.html')


