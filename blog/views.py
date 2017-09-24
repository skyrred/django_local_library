from django.shortcuts import render_to_response ,render,get_object_or_404
from blog.models import Post,Post2
import webbrowser
import smtplib as p


def index(request):
	return render(request ,'index.html')
def blog(request):
	posts = Post.objects.filter(published = True)
	posts2 = Post2.objects.filter(published = True)
	return render(request , 'blog.html' , {'posts':posts,'posts2':posts2})
def view_blog_post(request , slug):
	post = get_object_or_404(Post , slug = slug)
	return render(request,'post.html',{'post':post})

def view_post_2(request , slug):
	post = get_object_or_404(Post2 , slug = slug)
	return render_to_response('post.html',{'post':post})
def post(request,slug):
	post = get_object_or_404(Post ,slug=slug)
	return render(request,'post.html',{'post':post})
def about(request):
	return render(request,'about.html')
def sending(request):
	if (request.method == 'POST'):
		name = request.POST.get('name',None)
		about = request.POST.get('about',None)
		description = request.POST.get('description',None)
		msg ="""From: From skyteam.work@gmail.com
To: %r
MIME-Version: 1.0
Content-type: text/html
Subject: BUG repport about (%a)
<h1> Message :</h1>
<p>%s</p>

"""	% (name,about,description)	
		server = p.SMTP("smtp.gmail.com",587)
		server.starttls()
		server.login("teamsky.work@gmail.com","teamskywork123")
		server.sendmail("teamsky.work@gmail.com","sky.red2212@gmail.com",msg)
		return render(request , 'done.html')
def send(request):
	return render(request , 'sending.html')

# Create your views here.
