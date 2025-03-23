from django.shortcuts import render
from .forms import ReviewForm

def index(request):
	if 'vote_counts' not in request.session:
		request.session['vote_counts'] = {'good': 0, 'satis': 0, 'bad': 0}
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.cleaned_data['review']
			vote_counts = request.session['vote_counts']
			vote_counts[review] += 1  
			request.session['vote_counts'] = vote_counts
			total_votes = sum(vote_counts.values())
			percentages = {key: (value / total_votes) * 100 for key, value in vote_counts.items()} if total_votes > 0 else {'good': 0, 'satis': 0, 'bad': 0}

			body = {
				'percentages': percentages,
				'total_votes': total_votes
			}
			return render(request, 'results.html', body)
	else:
		form = ReviewForm()

	return render(request, 'index.html', {'form': form})
