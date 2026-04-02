from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def get_published_posts(queryset=None):
    """Возвращает только опубликованные посты"""
    if queryset is None:
        queryset = Post.objects.all()
    return queryset.filter(
        is_published__exact=True,
        category__is_published__exact=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template = 'blog/index.html'
    post_list = get_published_posts().select_related(
        'category', 'location', 'author'
    ).order_by('-pub_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts().select_related('category', 'location', 'author'),
        pk=pk
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_published_posts(
        category.posts.all()
    ).select_related('category', 'location', 'author')

    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, template, context)
