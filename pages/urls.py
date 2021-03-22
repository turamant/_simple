from django.urls import path


from pages.views import HomePageView, PostListView, RubricListView, PostDetailView, \
    RubricDetailView, AllImageView, PostCreate, PostUpdate, RubricCreate, PostDelete, RubricDelete, RubricUpdate

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),

    path('rubrics/',RubricListView.as_view(), name='rubric_list'),
    path('rubrics/new/',RubricCreate.as_view(), name='rubric_new'),
    path('rubrics/<slug:slug>/',RubricDetailView.as_view(), name='rubric_detail'),
    path('rubrics/<slug:slug>/delete/',RubricDelete.as_view(), name='rubric_delete'),
    path('rubrics/<slug:slug>/update/',RubricUpdate.as_view(), name='rubric_update'),

    path('posts/',PostListView.as_view(), name='post_list'),
    path('posts/new/',PostCreate.as_view(), name='post_new'),
    path('posts/<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug:slug>/delete/',PostDelete.as_view(), name='post_delete'),
    path('posts/<slug:slug>/update/',PostUpdate.as_view(), name='post_update'),

    path('gallery/',AllImageView.as_view(), name='gallery'),
]