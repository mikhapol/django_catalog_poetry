from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog_app.models import Blog


# Create your views here.


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name_blog', 'body', 'image', 'published')
    success_url = reverse_lazy('blog_app:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name_blog)
            new_mat.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    extra_context = {
        'title': 'Подробности блога'
    }


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name_blog', 'body', 'image', 'published')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.name_blog)
            new_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_app:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_app:list')


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.published:
        blog_item.published = False
    else:
        blog_item.published = True

    blog_item.save()

    return redirect(reverse('blog_app:list'))
