from django.shortcuts import render, get_object_or_404, redirect

from actstream import models

from raspberryio.userprofile.models import Profile


def profile_related_list(request, username, relation):
    "Render the list of a users folllowers or who the user is following"
    profile = get_object_or_404(Profile, user__username__iexact=username)
    if profile.user.username != username:
        return redirect(profile, permanent=True)
    user = profile.user

    # get a queryset of users described by this relationship
    if relation == 'followers':
        related_users = models.followers(user)
    elif relation == 'following':
        related_users = models.following(user)
    return render(request, "accounts/account_profile_related.html", {
        'user': user,
        'profile': profile,
        'related_users': related_users,
    })


def profile_actions(request, username):
    "Custom renderer for user profile activity stream"
    profile = get_object_or_404(Profile, user__username__iexact=username)
    if profile.user.username != username:
        return redirect(profile, permanent=True)
    user = profile.user
    return render(request, "accounts/account_profile_actions.html", {
        'user': user,
        'profile': profile,
        'actions': models.actor_stream(user),
    })
