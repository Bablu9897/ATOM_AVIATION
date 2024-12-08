from django.shortcuts import render
from .models import BlogPost
from .utils import get_user_country
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request): 
    country = get_user_country(request=request)
    posts = BlogPost.objects.all()
    filtered_posts = posts.filter(country=country)

    paginator_post = Paginator(posts.order_by('created_at'), 8)  
    page_number = request.GET.get('page',1) 

    if page_number:
        try:
            page_obj_post = paginator_post.page(page_number)
        except PageNotAnInteger:
            page_obj_post = paginator_post.page(1)
        except EmptyPage:
            page_obj_post = paginator_post.page(1)
    else:
        page_obj_post = paginator_post.get_page(2)


    #for filter

    paginator = Paginator(filtered_posts.order_by('created_at'), 8)  
    page_of_number = request.GET.get('page',1) 

    if page_number:
        try:
            page = paginator.page(page_of_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(1)
    else:
        page = paginator.get_page(2)

    return render(request, 'blog/post_list.html', {
        'posts': page_obj_post,
        'filtered_posts': page,
        'country': country,
    })
