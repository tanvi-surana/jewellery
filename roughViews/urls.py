from django.conf.urls import url,patterns,include
from roughViews.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
				url(r'^$',initialPage,name='initial_page'),
				url(r'^jwellery/$',jwelleryPage,name='jwellery_page'),
				url(r'^jwellery/product',productPage,name='product'),
				url(r'^solitares/$',solitaresPage,name='solitares_page'),
				url(r'^goldCoins/$',goldCoinsPage,name='goldCoins_page'),
				url(r'^collections/$',collectionsPage,name='collections_page'),
				url(r'^gifts/$',giftsPage,name='gifts_page'),
		#		url(r'^fb/$',fbPage,name='fb_page'),
				url(r'^jwellery/(?P<code>[a-zA-Z0-9_.-=$]+)/$',product_detail_page),
				url(r'^customer/account/create/$',account_create),
				url(r'^checkout/twopage/$',order_payment),
				url(r'^footer/$',footer),

			)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
