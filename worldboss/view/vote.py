from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from worldboss.models import UploadedData, UserVote
from django.db.utils import IntegrityError


@login_required
def vote(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            spawn = UploadedData.objects.get(id=id)
            vote_type = request.POST.get('voteType')

            # Check if the user has already voted for this spawn
            try:
                user_vote = UserVote.objects.get(user=request.user, spawn=spawn)
                previous_vote = user_vote.vote_type
            except UserVote.DoesNotExist:
                previous_vote = None

            # Determine the new vote type and update the vote count
            if previous_vote == vote_type:
                # User is changing their vote
                if vote_type == 'up':
                    spawn.thumbs_up += 1
                    spawn.thumbs_down -= 1
                elif vote_type == 'down':
                    spawn.thumbs_down += 1
                    spawn.thumbs_up -= 1
            else:
                # User is casting a new vote
                if vote_type == 'up':
                    spawn.thumbs_up += 1
                    if previous_vote == 'down':
                        spawn.thumbs_down -= 1
                elif vote_type == 'down':
                    spawn.thumbs_down += 1
                    if previous_vote == 'up':
                        spawn.thumbs_up -= 1

            # Save the changes
            try:
                spawn.save()
            except IntegrityError:
                response = {'success': False, 'message': "You've already voted this way."}
                return JsonResponse(response)

            # Create or update the UserVote instance
            if previous_vote is None:
                UserVote.objects.create(user=request.user, spawn=spawn, vote_type=vote_type)
            else:
                user_vote.vote_type = vote_type
                user_vote.save()

            # Return a JSON response indicating the success of the vote
            response = {'success': True, 'message': 'Vote submitted successfully'}
            return JsonResponse(response)
        except UploadedData.DoesNotExist:
            response = {'success': False, 'message': 'Spawn does not exist'}
            return JsonResponse(response)
    else:
        response = {'success': False, 'message': 'Invalid request'}
        return JsonResponse(response)
