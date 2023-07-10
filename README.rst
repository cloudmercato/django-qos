==========
Django QoS
==========

Third app to run live tests on your projects


Install
=======

Install the package:::

  pip install django-qos  # not yet
  pip install https://github.com/cloudmercato/django-qos/archive/refs/heads/master.zip


Add QoS to your project configuration:::

  INSTALLED_APPS = [
      ...
      'django_qos',
      'django_qos.db',
  ]


Usage
=====

QoS is organized like `unittests`
1. You write a subclass of `django_qos.qos.QosTestCase`
2. Your run `./manage.py qos`


Tests (dev)
===========

::

  make test
