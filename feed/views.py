from django.contrib import messages
from django.views.generic import TemplateView,DetailView,FormView
from .forms import PostForm,ContactUsForm
from .models import Post,ContactUs

# Creating views for our site
# Home page view
class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
# Post Detail view
class PostDetail(DetailView):
    template_name = "detail.html"
    model = Post

# post view for user to post/upload an image
class AddPostView(FormView):
    template_name = "form.html"
    form_class = PostForm
    success_url = "/"
    
    def dispatch(self,request,*args,**kwargs):
        self.request = request
        return super().dispatch(request,*args,**kwargs)
    
    def form_valid(self,form):
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request,messages.SUCCESS,"Post Uploaded Successfully !")
        return super().form_valid(form)
    
# About us page
class AboutView(TemplateView):
    template_name = "about.html"

# Coming soon view for our website
class ComingSoonView(TemplateView):
    template_name = "coming-soon.html"

class ContactUsView(FormView):
    template_name = "contact.html"
    form_class = ContactUsForm
    success_url = "/"
    
    def dispatch(self,request,*args,**kwargs):
        self.request = request
        return super().dispatch(request,*args,**kwargs)
    
    def form_valid(self,form):
        new_object = ContactUs.objects.create(
            email = form.cleaned_data['email'],
            mobile = form.cleaned_data['mobile'],
            message = form.cleaned_data['message']  
        )
        messages.add_message(self.request,messages.SUCCESS,"Message sent Successfully !")
        return super().form_valid(form)

