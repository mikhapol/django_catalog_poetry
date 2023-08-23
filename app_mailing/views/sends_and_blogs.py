from django.views.generic import TemplateView

from app_blog.models import Blog
from app_mailing.models import MailingSettings, Buyer


class SendsAndBlogsView(TemplateView):
    template_name = 'app_mailing/sends_and_blogs.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailing'] = MailingSettings.objects.all().count()
        context_data['count_mailing_active'] = MailingSettings.objects.filter(
            status=MailingSettings.STATUS_STARTED).count()
        context_data['count_unique_buyer'] = Buyer.objects.distinct().count()
        context_data['mailing_blog'] = Blog.objects.filter(published=True)[:3]

        return context_data
