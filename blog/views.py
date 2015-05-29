from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Comment
from blog.forms import CreatePostForm, CreateCommentForm


def home(request, page=1):
    all_posts_actual = Post.objects.order_by('-date_published')
    paginator = Paginator(all_posts_actual, 3)

    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html',
                  {'posts': page_posts})


def post_detail(request, post_pk):
    if request.method == 'POST':
        comment_form = CreateCommentForm(request.POST)
        if comment_form.is_valid():
            post = get_object_or_404(Post, pk=post_pk)
            author = comment_form.cleaned_data['author']
            email = comment_form.cleaned_data['email']
            text = comment_form.cleaned_data['text']
            new_comment = Comment(post=post, author=author, email=email,
                                  text=text)
            new_comment.save()
            messages.info(request, 'Comment created.')
            return redirect(reverse('blog:post_detail',
                                    kwargs={'post_pk': post_pk}))
    else:
        comment_form = CreateCommentForm()
    return render(request, 'blog/post_detail.html',
                  {'post': get_object_or_404(Post, pk=post_pk),
                   'comment_form': comment_form,
                   'comments': Comment.objects.filter(post_id=post_pk)})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            date_published = form.cleaned_data['date_published']
            new_post = Post(title=title, date_published=date_published,
                            text=text)
            new_post.save()
            messages.info(request, 'Post created.')
            return redirect(reverse('blog:post_detail',
                                    kwargs={'post_pk': new_post.pk}))
    else:
        form = CreatePostForm()
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def update_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CreatePostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.info(request, 'Post updated.')
        return redirect(reverse('blog:post_detail',
                                kwargs={'post_pk': post.pk}))
    return render(request, 'blog/update_post.html',
                  {'form': form, 'post': post})


@login_required
def delete_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    messages.info(request, 'Post deleted.')
    return redirect('blog:home')


def search(request):
    if request.method == 'GET':
        if 'query' in request.GET:
            query = request.GET['query']
            matching_posts = Post.objects.filter(text__icontains=query)
    return render(request, 'blog/search_results.html',
                  {'posts': matching_posts})


@login_required
def hide_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.is_hidden = not comment.is_hidden
    comment.save()
    return redirect(reverse('blog:post_detail',
                            kwargs={'post_pk': comment.post.pk}))
