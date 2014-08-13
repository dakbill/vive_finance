from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from susu.models import Voucher


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Home'
        return context


def sign_in(request):
    if request.POST:
        uname = request.POST['uname']
        pword = request.POST['pword']
        user = authenticate(username=uname, password=pword)
        if user is not None:
            if user.is_active:
                login(request, user)
                return {
                    'm': redirect(reverse('susu:manager-home')),
                    'a': redirect(reverse('susu:home')),
                    'c': redirect(reverse('susu:home')),
                }[user.member.role]
            else:  # Return a 'disabled account' error message
                pass
        else:
            pass
            # Return an 'invalid login' error message.
    return redirect(reverse('susu:home'))


def sign_out(request):
    logout(request)
    return redirect(reverse('susu:home'))


class ManagerHomeView(TemplateView):
    template_name = 'manager/home.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ManagerHomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Manager'
        return context


class MemberRegistrationView(TemplateView):
    template_name = 'manager_agent/register.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MemberRegistrationView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Register'
        return context


class AgentView(TemplateView):
    template_name = 'susu/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Home'
        return context


class ClientView(TemplateView):
    template_name = 'susu/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Home'
        return context


class DepositView(TemplateView):
    template_name = 'home/deposit.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DepositView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Deposit'
        return context


class BalanceView(TemplateView):
    template_name = 'manager_agent_client/balance.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BalanceView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Deposit'
        return context


class VouchersView(ListView):
    template_name = 'manager/vouchers.html'
    model = Voucher



    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VouchersView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Vouchers'
        return context

