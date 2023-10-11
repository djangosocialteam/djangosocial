"""Home page models."""

from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from djangosocial.streams.blocks import HeroImageBlock


class HomePage(Page):
    """Home page model."""

    body = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("hero_image", HeroImageBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    content_panels = (
        *Page.content_panels,
        FieldPanel("body"),
    )
