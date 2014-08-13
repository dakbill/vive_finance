from django.conf.urls import patterns,  url
from django.contrib.auth.decorators import login_required
from susu import views

login_url='/susu'

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(),name='home'),
    url(r'^sign-in$', views.sign_in,name='sign-in'),
    url(r'^sign-out$', views.sign_out,name='sign-out'),
    url(r'^manager-home$', login_required(views.ManagerHomeView.as_view(),login_url=login_url),name='manager-home'),
    url(r'^register$', login_required(views.MemberRegistrationView.as_view(),login_url=login_url),name='register'),
    url(r'^print-vouchers$', login_required(views.VouchersView.as_view(),login_url=login_url),name='print-vouchers'),
    url(r'^balance$', login_required(views.BalanceView.as_view(),login_url=login_url),name='balance'),
    url(r'^deposit$', views.DepositView.as_view(),name='deposit'),

)