from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import BaseInlineFormSet

from accounts.models import UserProfile


class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    formset = RequiredInlineFormSet

    fields = (('confirmed',
               'gender',
               'birthday',),
              'phone_number',
              'address',
              'admin_comments')


class UserAdminExtra(UserAdmin):
    inlines = [UserProfileInline]
    list_display = ('first_name',
                    'last_name',
                    'is_active',
                    'email',
                    )

    ordering = ('-date_joined',)
    list_per_page = 40

    form = UserChangeForm
    add_form = UserCreationForm

    search_fields = ['email', 'username', 'first_name', 'last_name']

    list_filter = ('is_active', 'profile__confirmed', 'profile__closed')


# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdminExtra)

