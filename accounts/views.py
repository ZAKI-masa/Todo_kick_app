from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm  # forms.pyからインポート


class SignUpView(generic.CreateView):
    form_class = SignUpForm  # カスタムフォームを使用
    template_name = 'accounts/signup.html'  # テンプレートパスはそのまま
    success_url = reverse_lazy('login')