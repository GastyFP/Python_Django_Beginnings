from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# def january(request):
#     return HttpResponse("HELLO JANUARY!!!")


# def february(req):
#     return HttpResponse("HELLO FEBRUARY!!!")


# def march(req):
#     return HttpResponse("HELLO MARCH!!")

challenges = {
    "january": "EAT A PIE JAN",
    "february": " this is Feb",
    "march": " this is Mar",
    "april": " this is april",
    "may": " this is may",
    "june": " this is june",
    "july": " this is july",
    "august": " this is aug",
    "september": " this is sept",
    "october": " this is oct",
    "november": " this is nov",
    "december": " this is dec",
}


def index(req):
    months = list(challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     href_path = reverse("month-challenge", args=[month])
    #     ref_list += f"<li><a href={href_path}>{capitalized_month}</a></li>"

    return render(req, "challenges/index.html" , {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(challenges.keys())
    try:
        forward_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound(f"month with the number {month} not found!!!")


def monthly_challenges(request, month):
    try:
        response = challenges.get(month)

        return render(request, "challenges/challenge.html", {
            "month": month.capitalize(),
            "text": response
        })
    except:
        return HttpResponseNotFound(f"{month} not supported!!!")
