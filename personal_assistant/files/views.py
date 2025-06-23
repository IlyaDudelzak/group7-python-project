"""Views for the files app."""

# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import UploadedFile
from .forms import UploadFileForm
from .utils import get_category
from unidecode import unidecode
from django.conf import settings

# Removed Supabase client creation
file_storage = FileSystemStorage()
MAX_FILE_SIZE = 50 * 1024 * 1024

# @login_required
def file_manager(request):
    """
    Handle file uploads and display uploaded files with optional category filtering.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered file manager page.
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.cleaned_data["file"]
            if f.size > MAX_FILE_SIZE:
                form.add_error("file", "File is too large. Maximum allowed is 50 MB.")
            else:
                try:
                    file_bytes = f.read()
                    # path = f.name  # или f"user_{request.user.id}/{f.name}"
                    path=unidecode(f.name)

                    # Removed Supabase upload logic
                    file_storage.save(path, file_bytes)

                    # Replaced with Django's FileSystemStorage public URL logic
                    public_url = file_storage.url(path)

                    UploadedFile.objects.create(
                        # user=request.user,
                        filename=f.name,
                        url=public_url,
                        category=get_category(f.name)
                    )
                    return redirect("file-manager")
                except Exception as e:
                    form.add_error("file", f"Upload failed: {str(e)}")
    else:
        form = UploadFileForm()

    category = request.GET.get("category")
    files = UploadedFile.objects.all()
    if category:
        files = files.filter(category=category)

    return render(request, "files/file_manager.html", {
        "form": form,
        "files": files,
        "selected_category": category,
    })
