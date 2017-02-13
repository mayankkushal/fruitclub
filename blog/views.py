from django.shortcuts import render
from blog.models import Article, Comment, Like
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
	article_list = Article.objects.all().order_by("-date_created")
	context_dict = {'article_list':article_list}
	return render(request, 'blog/index.html', context_dict)

def article(request, article_slug):
	comment_form = CommentForm()
	comment_list = None
	article = Article.objects.get(slug=article_slug)
	count = Like.objects.filter(article=article).count()
	comment_list = Comment.objects.filter(article=article).order_by('-time')
	return render(request, 'blog/article.html', {'article':article, 'comment_list':comment_list, 'comment_form':comment_form, 'count':count})

@login_required
def add_comment(request):
	if request.method == 'POST':
		comment = request.POST['comment']
		pid = request.POST['pid']
		article = Article.objects.get(id=pid)
		if article:
			Comment.objects.create(
					article=article,
					comment=comment,
					poster=request.user
				)
			article.comments += 1
			article.save()
			comm_count = article.comments
			data = {'comm_count':comm_count}
			data['comment'] = comment
			data['user'] = request.user.username
			return HttpResponse(json.dumps(data), content_type='application/json')
		else:
			return HttpResponse("No such post")

@login_required
def like_article(request):
	if request.method == "GET":
		pid = request.GET['pid']
		article = Article.objects.get(id=pid)
		if article:
			new_like, created = Like.objects.get_or_create(user=request.user, article_id=pid)
			if not created:
				new_like.delete()
			count = Like.objects.filter(article=article).count()
			data = {'count':count}
			return HttpResponse(json.dumps(data), content_type='application/json')

def check_like(request):
	pid = request.GET['pid']
	try:
		like = Like.objects.get(user=request.user, article=Article.objects.get(id=pid))
	except Like.DoesNotExist:
		like = None
	if like:
		liked = True
	else:
		liked = False
	return HttpResponse(json.dumps(liked), content_type='application/json')