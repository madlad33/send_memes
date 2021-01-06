from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView, DetailView

from contacts.utils import send_whatsapp_message
from .models import Contact
from .forms import ContactForm, MessageForm
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect


class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/main.html'


class MessageDetailView(DetailView):
    model = Contact
    template_name = 'contacts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm
        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if request.method == 'POST':
            # import function to run
            from .scrape import get_memes
            get_memes()
        if form.is_valid():
            message_to = self.get_object()
            body = form.cleaned_data.get('body')
            send_whatsapp_message(body, message_to)

            return redirect('success')

    def get_success_url(self):
        return reverse('success')


class AddContactView(FormView):
    form_class = ContactForm
    template_name = 'contacts/add.html'
    success_url = reverse_lazy('contact-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def success_view(request):
    return render(request, 'contacts/success.html',context={})
