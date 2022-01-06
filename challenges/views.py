from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This is january.",
    "february": "This is february.",
    "march": "This is march.",
    "april": "This is april.",
    "may": "This is may.",
    "june": "This is june.",
    "july": "This is july.",
    "august": "This is august.",
    "september": "This is september.",
    "october": "This is october.",
    "november": "This is november.",
    "december": "This is december.",

}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys()) # [jan, feb, mar, apr, may, ...]

    return render(request, "challenges/index.html", {"months": months})
    # for m in months: # jan, feb
    #     capitalize_month = m.capitalize() # Jan, Feb
    #     month_path = reverse("monthly-challenges", args=[m]) # /challenges/february
    #     list_items += f"<li><a href='{month_path}'>{capitalize_month}</a></li>"

    #     """
    #     <ul>
    #         <li><a href="/challenges/january">January</a></li>
    #         <li><a href="/challenges/february">February</a></li>
    #          <li><a href="/challenges/january">January</a></li>
    #         <li><a href="/challenges/february">February</a></li>
    #          <li><a href="/challenges/january">January</a></li>
    #         <li><a href="/challenges/february">February</a></li>
    #          <li><a href="/challenges/january">January</a></li>
    #         <li><a href="/challenges/february">February</a></li>
    #          <li><a href="/challenges/january">January</a></li>
    #         <li><a href="/challenges/february">February</a></li>
    #          <li><a href="/challenges/january">January</a></li>
    #         <li><a href="/challenges/february">February</a></li>
    #     </ul>

    #     """
    
    # response_data = f"<ul>{list_items}</ul>" # li, li, li, li, li

    # return HttpResponse(response_data)

def monthly_activities(request, month):
    try:
        challenge = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"month_name": month, "challenge_name": challenge}) # DTL: Django Template Language
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")

def monthly_activities_by_number(request, month): # 1
    months = list(monthly_challenges.keys()) 
    # { jan, feb, mar, apr, may, ... } => months = [ jan, feb, mar, apr, may, ... ]
    # months.length = 12

    if month > len(months): # 1 > 12
        return HttpResponseNotFound("Invalid month.")

    redirect_month = months[month - 1] # redirect_month = months[0] = jan
    redirect_path = reverse("monthly-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path) # /challenges/january