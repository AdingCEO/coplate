from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView
from coplate.models import Review, User
from coplate.forms import ReviewForm, ProfileForm
from coplate.functions import confirmation_required_redirect
# Create your views here.

class IndexView(ListView):
    model = Review
    template_name = 'coplate/index.html'
    context_object_name = 'reviews'
    paginate_by = 4
    ordering = ['-dt_created']

    
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'coplate/review_detail.html'
    pk_url_kwarg = 'review_id'
    
    
class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    
    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect
    
    def form_valid(self,form): #입력받은 데이터 유효할때 데이터로 채워진 모델 오브젝트 만들고 저장함
        form.instance.author = self.request.user #form의 인스턴스에 author를 추가해줌. 클래스형 뷰에서 현재유저 접근할때는 self.으로 접근해야함
        return super().form_valid(form) #super는 CreateView 클래스 뜻함
    
    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id':self.object.id}) #새로 생성된 오브젝트는 self.object로 접근가능
    
    def test_func(self, user): #이메일 인증 했는지 테스트 로직
        return EmailAddress.objects.filter(user=user, verified=True).exists()
    
    
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    pk_url_kwarg = 'review_id'
    
    raise_exception = True
    # redirect_unauthenticated_users = False 기본값이 False임
    
    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id':self.object.id})
    
    def test_func(self, user):
        review = self.get_object()
        return review.author == user
    
    
class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "coplate/review_confirm_delete.html"
    pk_url_kwarg = 'review_id'
    
    raise_exception = True
    
    def get_success_url(self):
        return reverse('index')
    
    def test_func(self, user):
        review = self.get_object()
        return review.author == user
    
    
class ProfileView(DetailView):
    model = User
    template_name = 'coplate/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile_user'
    
    def get_context_data(self, **kwargs): #해당 유저의 최신 4개 리뷰 가져오는 context 만들기
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        context['user_reviews'] = Review.objects.filter(author__id=user_id).order_by('-dt_created')[:4]
        return context
    
    
class UserReviewListView(ListView):
    model = Review
    template_name = 'coplate/user_review_list.html'
    context_object_name = 'user_reviews'
    paginate_by = 4
    
    #모든 오브젝트가 아닌 특정 유저가 작성한 리뷰들만 리턴하도록 만들기
    def get_queryset(self): #url 파라미터는 self.kwargs로 접근가능
        user_id = self.kwargs.get('user_id')
        return Review.objects.filter(author__id = user_id).order_by('dt_created')
    
    def get_context_data(self, **kwargs): #해당 유저의 최신 4개 리뷰 가져오는 context 만들기
        context = super().get_context_data(**kwargs)
        context['profile_user'] = get_object_or_404(User, id=self.kwargs.get("user_id")) #url로 없는 유저 페이지에 들어갈 수 있으므로
        return context

    
class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'coplate/profile_set_form.html'
    
    def get_object(self, queryset=None): #여러 오브젝트 다룰때는 get_queryset 하나만 다룰때는 get_object
        return self.request.user
    
    def get_success_url(self):
        return reverse('index')
    
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'coplate/profile_update_form.html'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse('profile', kwargs=({'user_id':self.request.user.id}))
    
    
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse('profile', kwargs=({'user_id':self.request.user.id}))
    
