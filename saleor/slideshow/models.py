from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.translation import pgettext_lazy
from draftjs_sanitizer import clean_draft_js

from ..core.db.fields import SanitizedJSONField
from ..core.models import PublishableModel, PublishedQuerySet
from ..core.utils import build_absolute_uri
from ..core.utils.draftjs import json_content_to_raw_text
from ..core.utils.translations import TranslationProxy
from ..seo.models import SeoModel, SeoModelTranslation
from versatileimagefield.fields import PPOIField, VersatileImageField

class Slideshow(SeoModel, PublishableModel):
    content = models.TextField(blank=True)
    image = VersatileImageField(
        upload_to="slideshow", blank=False, null=False
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created",)
        permissions = (
            ("manage_slideshow", pgettext_lazy("Permission description", "Manage slideshow.")),
        )

    def __str__(self):
        return self.content