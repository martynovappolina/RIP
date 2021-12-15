from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from cd.models import CD
from cd.models import CD_lib


def index(request):
    libs = CD_lib.objects.all()
    disks = CD.objects.all()
    return render(request, "index.html", {"libs": libs, "disks": disks})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        dl = CD_lib()
        dl.name = request.POST.get("name_lib")
        dl.save()
    return HttpResponseRedirect("/")


def create_disk(request):
    if request.method == "POST":
        d = CD()
        d.name = request.POST.get("name")
        d.capacity = request.POST.get("capacity")
        d.cdLib = CD_lib.objects.get(name=request.POST.get("cdLib"))
        d.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        disk = CD.objects.get(id=id)

        if request.method == "POST":
            disk.name = request.POST.get("name")
            disk.capacity = request.POST.get("capacity")
            disk.cdLib = CD_lib.objects.get(name=request.POST.get("cdLib"))
            disk.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"disk": disk})
    except CD.DoesNotExist:
        return HttpResponseNotFound("<h2>Disk not found</h2>")


def edit_lib(request, id):
    try:
        lib = CD_lib.objects.get(id=id)

        if request.method == "POST":
            lib.name = request.POST.get("name")
            lib.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_lib.html", {"lib": lib})
    except CD_lib.DoesNotExist:
        return HttpResponseNotFound("<h2>Library not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        disk = CD.objects.get(id=id)
        disk.delete()
        return HttpResponseRedirect("/")
    except CD.DoesNotExist:
        return HttpResponseNotFound("<h2>Disk not found</h2>")


def delete_lib(request, id):
    try:
        lib = CD_lib.objects.get(id=id)
        lib.delete()
        return HttpResponseRedirect("/")
    except CD.DoesNotExist:
        return HttpResponseNotFound("<h2>Library not found</h2>")