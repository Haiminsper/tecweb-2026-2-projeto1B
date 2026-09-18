from django.shortcuts import redirect, render

from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_name = request.POST.get('tag', '').strip()

        tag = None
        if tag_name:
            tag, _ = Tag.objects.get_or_create(name=tag_name)

        Note.objects.create(title=title, content=content, tag=tag)
        return redirect('index')

    all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})


def delete(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')


def edit(request, note_id):
    note = Note.objects.get(id=note_id)

    if request.method == 'POST':
        tag_name = request.POST.get('tag', '').strip()

        tag = None
        if tag_name:
            tag, _ = Tag.objects.get_or_create(name=tag_name)

        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.tag = tag
        note.save()
        return redirect('index')

    return render(request, 'notes/edit.html', {'note': note})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': tags})


def tag_detail(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})
