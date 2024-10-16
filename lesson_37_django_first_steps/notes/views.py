from django.template import loader
from django.http import HttpResponse, HttpRequest
from notes.models import Note

# Create your views here.

def notes(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.order_by("-created_date")
    template = loader.get_template("notes/index.html")
    list = []
    for note in notes:
        date = note.created_date.strftime("%B %d, %Y")
        note_item = {
            "date": date,
            "text": note.text,
            "author": note.author,
        }
        list.append(note_item)
    context = {"notes": list}
    return HttpResponse(template.render(context, request))


