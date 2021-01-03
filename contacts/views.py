from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,FormView,DetailView

from contacts.utils import send_whatsapp_message
from .models import Contact
from .forms import ContactForm,MessageForm
from django.urls import reverse_lazy
from django.http import JsonResponse,HttpResponse
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
    def post(self,request,*args,**kwargs):
        form = MessageForm(request.POST)

        if form.is_valid():
            message_to = self.get_object()
            body = form.cleaned_data.get('body')
            send_whatsapp_message(body,message_to)
            return HttpResponse(f"we've sent a message {body} to {message_to}")





class AddContactView(FormView):
    form_class = ContactForm
    template_name = 'contacts/add.html'
    success_url = reverse_lazy('contact-list')