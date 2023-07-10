from django.dispatch import Signal
from django.core.mail import send_mail
from django.template.loader import get_template

from django_qos import settings


pre_run_tests = Signal()
post_run_tests = Signal()


def post_run_tests_email(sender, suite, result, **kwargs):
    """
    This function must be registered as a `django_qos.signals.post_run_tests` signal.
    It sends an email to `settings.QOS_EMAILS with the report.
    """
    def format_failures(failures):
        data = {
            test.id(): {
                'name': test.id(),
                'doc': test._testMethodDoc,
                'traceback': traceback,
                'message': traceback.splitlines()[-1].split(':')[-1].strip(),
            }
            for test, traceback in failures
        }
        return data

    if not result.failures and not result.errors:
        state = 'OK'
    elif result.errors:
        state = 'Error'
    elif result.failures:
        state = 'Failed'

    context = {
        'suite': suite,
        'result': result,
        'state': state,
        'failures': format_failures(result.failures),
        'errors': format_failures(result.errors),
    }
    message = get_template('django_qos/report_mail.txt').render(context)
    html_message = get_template('django_qos/report_mail.html').render(context)
    send_mail(
        subject=f"QoS report: {state}",
        message=message,
        html_message=html_message,
        from_email=settings.SERVER_EMAIL,
        recipient_list=settings.MAILS,
        fail_silently=False
    )
