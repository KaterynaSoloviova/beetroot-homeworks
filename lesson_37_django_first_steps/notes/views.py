from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from notes.forms import NoteForm
from notes.models import Note


# Create your views here.
@login_required
def note_list(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.filter(user=request.user).order_by("-created_date")
    template = loader.get_template("notes/index.html")
    list = []
    for note in notes:
        date = note.created_date.strftime("%B %d, %Y")
        note_item = {
            "pk": note.pk,
            "date": date,
            "text": note.text,
            "author": note.author,
            "title": note.title,
            "category": note.category.title.lower(),
        }
        list.append(note_item)
    context = {"notes": list}
    return HttpResponse(template.render(context, request))

@login_required
def note_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes:note_list')
        else:
            return HttpResponseBadRequest('Form is incorrectly filled')
    else:
        form = NoteForm()

    return render(request, "notes/form.html", {"form": form})

@login_required
def note_edit(request: HttpRequest, pk: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_list')
        else:
            return HttpResponseBadRequest('Form is incorrectly filled')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/form.html', {'form': form})

@login_required
def note_delete(request: HttpRequest, pk: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
