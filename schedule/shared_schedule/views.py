from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Event, Resource
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from bootstrap_datepicker_plus import DateTimePickerInput

# Create your views here.
def SharedSch(request):
	all_events = Event.objects.all()
	all_resources = Resource.objects.all()

	context = {"events":all_events, "resources":all_resources}

	return render(request, 'shared_schedule/calendar.html', context)


def vSharedSch(request):
	all_events = Event.objects.all()
	all_resources = Resource.objects.all()

	context = {"events": all_events, "resources": all_resources}

	return render(request, 'shared_schedule/vcalendar.html', context)

class EventCreate(SuccessMessageMixin, CreateView):
	model = Event
	fields = '__all__'
	success_message = "Event %(title)s added successfully!"

	def get_form(self):
		form = super().get_form()
		form.fields['start'].widget = DateTimePickerInput()
		form.fields['end'].widget = DateTimePickerInput()
		return form

class EventUpdate(SuccessMessageMixin, UpdateView):
	model = Event
	fields = '__all__'
	template_name_suffix = '_update_form'
	success_message = "Event %(title)s updated successfully!"
	# success_url = '/'

	def get_form(self):
		form = super().get_form()
		form.fields['start'].widget = DateTimePickerInput()
		form.fields['end'].widget = DateTimePickerInput()
		return form

class EventDetail(DetailView):
	context_object_name = 'Event_details'
	model = Event
	template_name = 'shared_schedule/event_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class EventDelete(SuccessMessageMixin, DeleteView):
	model = Event
	success_url = reverse_lazy('sharedSch')
	success_message = "Event %(title)s deleted successfully."

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(EventDelete, self).delete(request, *args, **kwargs)


# Resource Views
class ResourceCreate(SuccessMessageMixin, CreateView):
	model = Resource
	fields = '__all__'
	success_message = "Resource: %(title)s added successfully!"


class ResourceUpdate( SuccessMessageMixin, UpdateView):
	model = Resource
	fields = '__all__'
	template_name_suffix = '_update_form'
	success_message = "Resource: %(title)s updated successfully!"
	# success_url = '/'


class ResourceDetail(DetailView):
	context_object_name = 'Resource_details'
	model = Resource
	template_name = 'shared_schedule/resource_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
