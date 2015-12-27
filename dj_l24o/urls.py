from django.conf.urls import url

import l24o.views

urlpatterns = [
    url(r'^serials/', l24o.views.serials_list_view.as_view()),
]
