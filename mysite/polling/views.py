from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
print('[DKA /polling/views.py]') # DKA
def list_view(request):
    print('[DKA /polling/views.py list_view()]') # DKA
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)

def detail_view(request, poll_id):
    print('[DKA /polling/views.py detail_view()]') # DKA
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)
