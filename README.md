django-email-auth: email_auth
==

The `email_auth` application adds e-mail login capabilities to Django.

Installation
--

In your settings file:

Add `email_auth` to `INSTALLED_APPS`
Add `email_auth.backends.EmailBackend` to `AUTHENTICATION_BACKENDS`

Replace all usage of `django.contrib.auth.forms.AuthenticationForm` with `email_auth.forms.AuthenticationForm`.

For example, you could add this to your root urls.py:

    import email_auth.forms.AuthenticationForm

    urlpatterns += patterns('',
        url(r'/accounts/login/', 
         'django.contrib.auth.views.login', 
         {'authentication_form': email_auth.forms.AuthenticationForm }
	    ),
	)
