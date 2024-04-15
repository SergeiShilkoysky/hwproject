import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Main page accessed')
    return render(request, 'myhwapp/base.html')


def about(request):
    logger.info('about page accessed')
    return render(request, 'myhwapp/about.html')


def contacts(request):
    logger.info('contacts page accessed')
    return render(request, 'myhwapp/contacts.html')
