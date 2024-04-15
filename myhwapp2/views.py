import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('hw2 page accessed')
    return HttpResponse("<h3> hw2 page </h3>")
