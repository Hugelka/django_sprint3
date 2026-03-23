from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published__exact=True,
        category__is_published__exact=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(
        Q(is_published__exact=True)
        & Q(pub_date__lte=timezone.now())
        & Q(category__is_published__exact=True)
    ), pk=pk)

    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    post_list = Post.objects.filter(
        is_published__exact=True,
        category__slug=category_slug,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, template, context)
