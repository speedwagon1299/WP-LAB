from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            course = form.cleaned_data['course']
            feedback_text = form.cleaned_data['feedback']
            return render(request, 'feedback_success.html', {
                'name': name,
                'subject': subject,
                'course': course,
                'feedback_text': feedback_text,
            })
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})
