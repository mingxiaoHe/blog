#coding=utf-8
from django.utils.safestring import mark_safe
class PageInfo:

    def  __init__(self, current_page, all_count, per_item = 5):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item
    @property
    def start(self):
        return (self.CurrentPage - 1) * self.PerItem
    @property
    def end(self):
        return self.CurrentPage * self.PerItem
    @property
    def all_page_count(self):
        temp = divmod(self.AllCount, self.PerItem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return all_page_count



def Pager(page,all_page_count,murl):
    '''
    page = 当前页
    all_page_count = 总页数
    :param page:
    :param all_page_count:
    :return:
    '''
    '''
    :param page:
    :param all_page_count:
    :return:
    '''

    page_html = []
    # first_html = ("<a href='/index/%d'>first</a>") % (1,)
    # page_html.append(first_html)

    if page <= 1:
        priv_html = "<a href='#' class='unavailable' >«上一页</a>"
    else:
        priv_html = ("<a href='/%s/%d' class='unselected' >«上一页</a>") % (murl,page-1,)
    page_html.append(priv_html)



    begin = page - 6
    end = page + 5
    #每夜11页码

    if all_page_count < 11:
        begin =0
        end = all_page_count
        #总页数大于11
    else:
        #当前页小于6
        if page < 6:
            begin = 0
            end = 11
        else:
            if page + 6 > all_page_count:
                begin = page - 6
                end = all_page_count
            else:
                begin = page - 6
                end = page + 5

    for i in range(begin,end):
        #当前页
        if page == i+1:
            a_html = "<a class='selected' 'href='/%s/%d'>%d</a>" %(murl,i+1,i+1)
        else:
            a_html = "<a  href='/%s/%d' class='unselected'>%d</a>" %(murl,i+1,i+1)
        # print a_html
        page_html.append(a_html)

    # if page == all_page_count:
    #     next_html = ("<a href='#' class='unavailable' >«下一页» </a>")
    # else:
    #     next_html = ("<a href='/%s/%d'class='unselected' >下一页» </a>") % (murl,page+1,)
    # page_html.append(next_html)

    if page == all_page_count:
        next_html = ("<a href='#' class='unavailable' >下一页» </a>")
    elif page > all_page_count:
        next_html = ("<a href='/%s/%d'class='unselected' >下一页» </a>") % (murl,all_page_count,)
    else:
        next_html = ("<a href='/%s/%d'class='unselected' >下一页» </a>") % (murl, page + 1,)
    page_html.append(next_html)


    # end_html = ("<a href='/index/%d'>last</a>") % (all_page_count,)
    # page_html.append(end_html)

    page_string = mark_safe(''.join(page_html))
    return page_string
