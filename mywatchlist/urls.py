from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_mywatchlist_json
from mywatchlist.views import show_mywatchlist_xml
from mywatchlist.views import show_mywatchlist_json_byid
from mywatchlist.views import show_mywatchlist_xml_byid

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('xml/<int:id>', show_mywatchlist_xml_byid, name='show_mywatchlist_xml_byid'),
    path('json/<int:id>', show_mywatchlist_json_byid, name='show_mywatchlist_json_byid'),
]