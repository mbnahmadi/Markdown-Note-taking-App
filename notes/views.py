from django.shortcuts import render
from notes.models import Notes
from notes.forms import NoteForm
import language_tool_python
import markdown
# Create your views here.

def upload_notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save()
            markdown_path = note.markdown_file.path
            with open(markdown_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
                tool = language_tool_python.LanguageTool('en-US')
                matches = tool.check(markdown_content)
                grammar_errors = [match.message for match in matches] if matches else ["No grammar errors found."]

                html_content = markdown.markdown(markdown_content)

                return render(request, 'notes/note_detail.html', {
                'note': note,
                'html_content': html_content,
                'grammar_errors': grammar_errors
                })  
    else:
        form = NoteForm()
        return render(request, 'notes/upload.html', {'form': form})