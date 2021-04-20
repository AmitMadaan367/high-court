from django.urls import path
from footer import views
from .views import *

app_name = 'footer'




urlpatterns =[
    path('Contact_Us/', views.FooterView.contact, name="contact"),
    path('About/', views.FooterView.about, name="about"),
    path('Affiliates/', views.FooterView.affiliates, name="affiliates"),
    path('terms_of_use/', views.FooterView.terms, name="terms"),
    path('Privacy/', views.FooterView.privacy, name="privacy"),
    #path('Security', views., name="security"),
    path('Survivor_Rules/', views.FooterView.survivor, name="survivor"),
    path('Bounty_Rules/', views.FooterView.bounty, name="bounty"),
    path('Squads_Rules/', views.FooterView.squads, name="squads"),
    path('Steps_Rules/', views.FooterView.steps, name="steps"),
    path('Daily_Rules/', views.FooterView.daily, name="daily"),
    path('Account_Security/', views.FooterView.account_security, name="security"),
    path('GICS/', views.FooterView.gics, name="gics"),
    path('Exchanges/', views.FooterView.av_markets, name="exchanges"),
    path('technicality/', views.FooterView.technicalities, name="technicality"),
    path('Investments/', views.FooterView.investments, name="investments"),
    path('Holidays/', views.FooterView.holidays, name="holidays"),
    path('404/', views.FooterView.for_o_four, name="for_o_four"),
    path('rewards/', views.FooterView.rewards_view, name="rewards_view"),
    path('withdraw/', views.FooterView.withdraw, name="withdraw"),
    path('<str:fobject>/search_a_player/', views.search_a_player, name='search_a_player'),
    ]
