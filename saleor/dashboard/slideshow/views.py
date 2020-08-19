from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from ...core.utils import get_paginator_items
from ...slideshow.models import Slideshow
from ..views import staff_member_required
# from .filters import ShippingZoneFilter
from .forms import SlideshowForm


@staff_member_required
@permission_required("slideshow.manage_slideshow")
def slideshow_list(request):
    slides = Slideshow.objects.all()

    return TemplateResponse(request, "dashboard/slideshow/list.html", {"slides": slides})

@staff_member_required
@permission_required("slideshow.manage_slideshow")
def slideshow_upload(request):
    if request.method == 'POST':
        form = SlideshowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard:slideshow-list")
    else:
        form = SlideshowForm()
    return TemplateResponse(request, "dashboard/slideshow/slide_upload.html", {
        'form': form
    })


@staff_member_required
@permission_required("slideshow.manage_slideshow")
def slideshow_edit(request, pk):
    slide = get_object_or_404(Slideshow, pk=pk)
    form = SlideshowForm(request.POST or None, instance=slide)
    if form.is_valid():
        zone = form.save()
        msg = pgettext_lazy("Dashboard message", "Updated Slideshow")
        messages.success(request, msg)
        return redirect("dashboard:slideshow-list")
    ctx = {"form": form, "slide": slide}
    return TemplateResponse(request, "dashboard/slideshow/slide_edit.html", ctx)

@staff_member_required
@permission_required("slideshow.manage_slideshow")
def slideshow_delete(request, pk):
    slide = get_object_or_404(Slideshow, pk=pk)
    form = SlideshowForm(request.POST or None, instance=slide)
    if request.method == "POST":
        slide.delete()
        msg = pgettext_lazy("Dashboard message", "Slide Image successfully removed")
        messages.success(request, msg)
        return redirect("dashboard:slideshow-list")
    ctx = {"form": form, "slide": slide}
    return TemplateResponse(request, "dashboard/slideshow/slide_delete.html", ctx)