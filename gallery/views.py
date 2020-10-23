from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import JsonResponse

from profiles.models import UserProfile
from gallery.forms import ReviewForm
from products.models import Product
from gallery.models import UserReview

# Create your views here.


def gallery(request):
    """Render GALLERY Page"""
    product = Product.objects.all()
    reviews = UserReview.objects.all()
    review_form = ReviewForm()

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        if request.user == user.user:
            context = {
                'user': user,
                'product': product,
                'reviews': reviews,
                'review_form': review_form,
            }
            return render(request, 'gallery/gallery.html', context)

    else:
        context = {
            'gallery_page': 'active',
            'product': product,
            'reviews': reviews,
        }
    return render(request, 'gallery/gallery.html', context)


def new_review(request):

    user_profile = UserProfile.objects.get(user=request.user)

    if request.user.is_authenticated:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                if len(request.POST["review_content"]) <= 0 or len(
                        request.POST["product"]) <= 0:
                    messages.error(
                        request, "You haven't completed the review form! \
                                    Please add content and try again.")
                    return redirect(reverse("gallery"))
                new_review = review_form.save(commit=False)
                new_review.user_profile = user_profile
                review_form.save()
                messages.success(request, 'Your review has \
                                        been added.')
                return redirect(reverse("gallery"))
            else:
                messages.error(request, 'Your review could not be added. \
                                    Please check that your review is valid.')

    template = 'gallery/gallery.html'
    context = {
        'review_form': review_form,
    }

    return render(request, template, context)


def edit_review(request, review_id):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    review = get_object_or_404(UserReview, id=review_id)
    review_form = ReviewForm(instance=review)

    if request.user == user_profile.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                if len(request.POST["product" or "review_content"]) <= 0:
                    messages.error(
                        request, "You have not completed the review form. \
                                            Please add content and try again.")
                    return redirect(reverse("gallery"))
                else:
                    review = review_form.save(commit=False)
                    user_profile = user_profile
                    review_form.save()
                    messages.success(request, 'Your review has \
                                                    been updated.')
                    return redirect(reverse("gallery"))
        else:
            review_form = ReviewForm(instance=review)

    template = 'gallery/includes/edit_review.html'
    context = {
        'review_form': review_form,
        'user_profile': user_profile,
        'review': review,
    }

    return render(request, template, context)


def delete_review(request, review_id):

    review = get_object_or_404(UserReview, id=review_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.user.is_authenticated:
        if request.user == user_profile.user:
            review.delete()
            messages.success(request, 'Your review has \
                                    been deleted.')
            return redirect(reverse("gallery"))

        elif request.user.is_superuser:
            review.delete()
            messages.success(request, 'You have deleted this review.')
            return redirect(reverse("gallery"))

        else:
            messages.error(request, 'This review can only be deleted \
                                    by the author.')
            return redirect(reverse("gallery"))

    else:
        messages.error(request, 'You must be signed in.')
        return redirect(reverse("gallery"))

    template = 'gallery/gallery.html'
    context = {
        'review': review,
        'user_profile': user_profile,
    }

    return render(request, template, context)
