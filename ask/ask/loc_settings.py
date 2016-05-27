
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME' : 'mydb',
#         'USER' : 'myuser',
#         'PASSWORD' : 'mypasswd',
#         'HOST' : 'localhost',
#     }
# }
import os

LOGGING = {
'version': 1,
'disable_existing_loggers': False,
#'filters': {
#'require_debug_false': {
#'()': 'django.utils.log.RequireDebugFalse'
#}
#},
'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
         },
         'applogfile': {
              'level':'DEBUG',
              'class':'logging.handlers.RotatingFileHandler',
              'filename': os.path.join('/home/zserg/projects/web', 'requests.log'),
              'maxBytes': 1024*1024*15, # 15MB
              'backupCount': 10,
         },
},
'loggers': {
    'api.request.logger': {
         'handlers': ['applogfile',],
         'level': 'DEBUG',
      },
}
}
