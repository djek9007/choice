# from rest_framework import routers
#
# from alternative.views import AlternativeViewSet
# from catalog.views import RegionViewSet, DistrictViewSet, LocalityViewSet, TerritorialAffiliationViewSet, \
#     LanguageViewSet, ClassRoomView
# from order.views import OrderViewSet, CommentViewSet, StatusOrderViewSet
# from organizations.views import OrganizationsViewSet
# from publishingHouse.views import PublishingHouseViewSet, TextBookViewSet, YearPublishingViewSet
# from teachers.views import TeacherViewSet
#
# router = routers.DefaultRouter()
#
#
# #app organizations
# router.register('organization', OrganizationsViewSet)
#
# #app alternative
# router.register('alternative', AlternativeViewSet)
#
#
#
# router.register('locality', LocalityViewSet)
# router.register('territorial', TerritorialAffiliationViewSet)
# router.register('language', LanguageViewSet)
# router.register('classroom', ClassRoomView)
# #
# # #app publishingHouse
# router.register('pubhouse', PublishingHouseViewSet)
# router.register('textbook', TextBookViewSet)
# router.register('yearpub', YearPublishingViewSet)
# #
# # #app order
# router.register('order', OrderViewSet)
# router.register('status', StatusOrderViewSet)
# router.register('comment', CommentViewSet)
# #
# # #app teachers
# router.register('teacher', TeacherViewSet)