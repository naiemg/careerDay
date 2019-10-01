from django.shortcuts import render
from accounts.models import UserProfile, User
from studentview.forms import unknownWordForm, studentZipcode
import requests
import json
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = studentZipcode(request.POST)
        if form.is_valid():
            my_zip_code = form.cleaned_data['zip_code']
            return results(request, my_zip_code)
    else:
        form = studentZipcode()
    return render(request, 'studentView/search.html', {'form': form})

def results (request, my_zip_code):
    context_dict={}
    users = User.objects.filter(userprofile__zip_code = my_zip_code)
    context_dict['user_data']=users
    context_dict['unknownWordForm']=unknownWordForm
    if request.method == 'POST':
        form = unknownWordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['unknownWord']
            context_dict["word"] = word
            context_dict['definition'] = getDefinition(word)
    else:
        form = unknownWordForm()
    return render(request, 'studentview/results.html', context_dict)

def getDefinition(word):
    app_id = "3295402c"
    app_key = "ac0368276521e08e6d015569f0e010cc"
    language = "en-gb"
    word_id = str(word)
    fields = 'definitions'
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower() + '?fields=' + fields
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    parsed = json.loads(r.text)
    words = parsed["results"]
    definition = (words[0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
    if definition is '':
        return ''
    else:
        return definition