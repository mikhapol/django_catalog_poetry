from django.views.generic import TemplateView


class ContactTemplateView(TemplateView):
    template_name = 'catalog_app/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'Новое сообщение от {name} ({phone}): {message}')
        return super().get_context_data(**kwargs)
