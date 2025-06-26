from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from datetime import timedelta

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, 'diary/calendar.html', {'events': events})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            if event.is_recurring:
                date = event.recurrence_start
                while date <= event.recurrence_end:
                    if date.weekday() == event.date.weekday() and date != event.date:
                        Event.objects.create(
                            user=request.user,
                            title=event.title,
                            location=event.location,
                            date=date,
                            time=event.time,
                            is_recurring=False
                        )
                    date += timedelta(days=1)

            return redirect('calendar:calendar_view')
    else:
        form = EventForm()
    return render(request, 'diary/event_form.html', {'form': form})

@login_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('calendar:calendar_view')
    return render(request, 'diary/event_confirm_delete.html', {'event': event})