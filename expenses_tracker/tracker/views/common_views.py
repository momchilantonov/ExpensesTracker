from django.shortcuts import render, redirect


def get_id(obj, pk):
    return obj.objects.get(pk=pk)


def show_form(req, form, temp):
    context = {
        'form': form,
    }
    return render(req, temp, context)


def save_form(req, form, temp, red):
    if form.is_valid():
        form.save()
        return redirect(red)
    return show_form(req, form, temp)
