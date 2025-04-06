from django.shortcuts import render, redirect
from .forms import *

def vote_page(request):
    if 'vote_counts' not in request.session:
        request.session['vote_counts'] = {'A': 0, 'B': 0, 'C': 0}
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.cleaned_data['vote']
            # MUST TRIGGER SESSION UPDATE
            cur = request.session['vote_counts']
            cur[vote] += 1
            request.session['vote_counts'] = cur
            return redirect('results');

    else:
        form = VoteForm()
    return render(request, 'vote_page.html', {'form': form})

def results(request):
    vote_counts = [(k, v) for k,v in request.session['vote_counts'].items()]
    return render(request, 'results.html', {'data': vote_counts})