from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage
from django.contrib.syndication.views import Feed
from django.template import RequestContext
from blogengine.models import Post, Category
from django.contrib.syndication.views import Feed
from django.template import Context, loader
from django.http import HttpResponse
import datetime
import time

def home(request, page):
    posts = Post.objects.all()
    return render(request, "blogengine/post_list.html", {'object_list':posts})

def getPost(request, postSlug):
    # Get specified post
    post = Post.objects.filter(slug = postSlug)

    # Display specified post
    return render_to_response('single.html', {'posts':post}, context_instance = RequestContext(request))

def getCategory(request, categorySlug, selected_page = 1):
    # Get specified category
    posts = Post.objects.all().order_by('-pub_date')
    category_posts = []
    for post in posts:
        if post.categories.filter(slug = categorySlug):
            category_posts.append(post)

    # Add pagination
    pages = Paginator(category_posts, 1000)

    # Get the category
    category = Category.objects.filter(slug = categorySlug)[0]

    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the posts
    return render(request, 'category.html', { 'posts': returned_page.object_list, 'page': returned_page, 'category': category})

class PostsFeed(Feed):
    title = "My Django Blog posts"
    link = "feeds/posts/"
    description = "Blog"

    def items(self):
        return Post.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
