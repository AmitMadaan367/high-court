from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render
from stock_definition.models import Stock
from itertools import chain
from user_profile.models import Account, Mission_Tracker, Inbox
from myteam.models import Template
from django.views.generic import TemplateView
from user_profile.serializers import AccountSerializer
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

class FooterView(TemplateView):
    model = Account

    def initial_tree(self, request):
        print("initial tree")
        my_dict = {}
        user = request.user
        if request.user.is_authenticated:
            account = Account.objects.filter(custom_user=user.id).prefetch_related('templates').prefetch_related('watchlist').prefetch_related('contacts').prefetch_related('squads').select_related('exp_bar').first()
            account.check_if_unread_mail()
            watchlist_all = account.watchlist.all()
            my_dict.update({"watchlist":watchlist_all})
            trackers = Mission_Tracker.objects.filter(account=account)
            i = 0
            for tracker in trackers:
                title = "tracker_" + str(i)
                my_dict.update({title:tracker})
                i += 1
            inbox = get_object_or_404(Inbox, account=account)
            if account.unread_mail == True:
                my_dict.update({'unread_mail':inbox.number_of_unread_messages})
            templates = account.templates.all().order_by("id")
            template = templates.order_by("id").first()
            my_dict.update({"template":template, "account":account, "inbox":inbox})
            return my_dict

    def contact(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "If you have questions, comments or if you just want to contact the founder of the site, please email us at rodeofinancials@yahoo.com"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/contact_us.html', context=my_dict)

    def about(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "Rodeo Financial is a fantasy inspired financial simulation. It was launched in 2020 in Montreal by Giancarlo Avolio and Alexis Chenard."
        text_line2 = "Our mission is to support a competitive platform where users will sharpen their financial skills and better their brokerage account management abilities."
        my_dict.update({'text1':text_line1, 'text2':text_line2})
        return render(request, 'footer/about.html', context=my_dict)

    def affiliates(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "We are unfortunately not affiliated to any partners at the moment but we are very open to collaborations. Please email us a rodeofinancials@yahoo.com for more details."
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/affiliates.html', context=my_dict)

    def privacy(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "The protection of your personal information is very dear to the Rodeo Financial team. We pledge to never sell any of your personal information to third parties and protect all your data to the best of our abilities."
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/privacy.html', context=my_dict)

    def terms(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = ""
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/terms_of_use.html', context=my_dict)

    def survivor(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = ""
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/survivor_rules.html', context=my_dict)

    def bounty(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = ""
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/bounty_rules.html', context=my_dict)

    def squads(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = ""
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/squads_rules.html', context=my_dict)

    def steps(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = ""
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/steps_rules.html', context=my_dict)

    def daily(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = ""
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/daily_rules.html', context=my_dict)

    def account_security(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "This is the account security page"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/account_security.html', context=my_dict)


    def gics(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "This page explains the gics"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/gics.html', context=my_dict)

    def av_markets(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "This page lists the stock markets supported by Rodeo"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/av_markets.html', context=my_dict)

    def technicalities(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "I do not know the purpose of this page"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/technicalities.html', context=my_dict)

    def investments(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "This page will help you find the right investing platform for you"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/investments.html', context=my_dict)

    def holidays(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "This will list the days where the market is closed"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/holidays.html', context=my_dict)


    def for_o_four(request):
        my_dict = FooterView().initial_tree(request)
        return render(request, '404.html', context=my_dict)

    def rewards_view(request):
        print("triggered")
        my_dict = FooterView().initial_tree(request)
        return render(request, 'footer/rewards.html', context=my_dict)

    def withdraw(request):
        my_dict = FooterView().initial_tree(request)
        text_line1 = "A minimum of 10$ is required before you can withdraw"
        my_dict.update({'text1':text_line1})
        return render(request, 'footer/withdraw.html', context=my_dict)

##It returns all_accounts to the "Search A Player" in new_base.html so it can slice through them
def search_a_player(request, *args, **kwargs):
    if request.is_ajax():
        if request.user.is_authenticated:
            user = request.user
            account = get_object_or_404(Account, custom_user=user.id)
            all_accounts = Account.objects.all().order_by("-reputation").exclude(name=account.name)
            serialized = AccountSerializer(all_accounts, many=True)
            return JsonResponse(serialized.data, safe=False)
