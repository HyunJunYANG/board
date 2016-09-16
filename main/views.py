from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import Context
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html')
def board_index(request):
    post_list=Post.objects.all().filter(created_at__gte=timezone.now()).order_by('-created_at')
    page_data=Paginator(Post.objects.all(),5)
    page=request.GET.get('page')
    if page is None:
        page=1

    try:
        posts=page_data.page(page)
    except PageNotAnInteger:
        posts=page_data.page(1)
    except EmptyPage:
        posts=page_data.page(page_data.num_pages)

    return render(request, 'board_index.html',{'post_list':post_list,'post_list':posts, 'current_page': int(page), 'total_page':range(1, page_data.num_pages+1),})
def post_detail(request, pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request, 'post_detail.html',{'post':post,})
def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.created_at=timezone.now()
            post.save()
            return redirect('main.views.post_detail', pk=post.pk)
    else:
        form=PostForm()
    return render(request, 'write.html', {'form': form,})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('main.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'write.html', {'form': form})
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('main.views.board_index')
def comment_new(request,pk):
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=Post.objects.get(pk=pk)
            comment.save()
            return redirect('main.views.post_detail', pk)
    else:
        form=CommentForm()
    return render(request, 'post_form.html', {'form': form,})
def comment_edit(request, post_pk,pk):
    comment=Comment.objects.get(pk=pk)

    if request.method=="POST":
        form= CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('main.views.post_detail', post_pk)  
    else:
        form=CommentForm(instance=comment)
    return render(request, 'post_form.html',{'form':form,})
