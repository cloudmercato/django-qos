from django.contrib.sites.models import Site
from django_qos.sites import models


def post_record_site(
    sender,
    suite,
    result,
    test,
    test_result,
    **kwargs
        ):
    import ipdb; ipdb.set_trace()
    site = Site.objects.get(domain='foo')
    models.SiteResult.objects.get_or_create(
        site=site,
        result=test_result,
    )
