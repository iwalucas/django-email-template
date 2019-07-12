I few months ago, I ran into this post https://blog.anvileight.com/posts/django-email-templates-with-context-stored-in-database/
and decided to make it into a lib after using it on one of my projects

Quick start
-----------

1. Add "django-email-template" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-email-template',
    ]

2. Run `python manage.py migrate` to create the polls models.

You should see it under admin
