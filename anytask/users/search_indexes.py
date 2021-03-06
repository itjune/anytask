from haystack import indexes

from users.models import UserProfile


class UserProfileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user_id = indexes.IntegerField(model_attr='user__id')

    fullname_auto = indexes.NgramField()
    login_auto = indexes.NgramField(model_attr='user__username')
    ya_login_auto = indexes.NgramField(model_attr='ya_login')
    email_auto = indexes.NgramField(model_attr='user__email')

    def get_model(self):
        return UserProfile

    def prepare_fullname_auto(self, obj):
        return u'{0}'.format(obj.user.get_full_name())

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
