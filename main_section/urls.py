from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='emailscraper-home'),
    path('search', views.search, name='emailscraper-search'),
    #path('email-scraper-bot-on-google', views.email_scraper_bot_on_google, name='emailscraper-bot-on-google'),
    #path('search-bot-on-google', views.search_bot_on_google, name='search-bot-on-google'),
    path('complete-website-email-scraper', views.complete_website_email_scraper, name='complete-website-email-scraper'),
    path('search-complete-website', views.search_complete_website, name='search-complete-website'),
]
