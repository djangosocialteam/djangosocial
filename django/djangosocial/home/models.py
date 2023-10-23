"""Home page models."""

from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from djangosocial.streams.blocks import (
    ContentListBlock,
    ContentWithImagesBlock,
    HeroBlock,
    HeroImageBlock,
    LogoCloudBlock,
    StatsBlock,
    TimelineBlock,
)


class HomePage(Page):
    """Home page model."""

    body = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("hero_image", HeroImageBlock()),
            ("timeline", TimelineBlock()),
            ("stats", StatsBlock()),
            ("hero", HeroBlock()),
            ("content_list", ContentListBlock()),
            ("content_with_images", ContentWithImagesBlock()),
            ("logo_cloud", LogoCloudBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    content_panels = (
        *Page.content_panels,
        FieldPanel("body"),
    )

    parent_page_types = []
    subpage_types = ["home.AboutPage"]


class AboutPage(Page):
    "About Page Model"

    body = StreamField(
        [
            ("rich_text", blocks.RichTextBlock()),
            ("hero_image", HeroImageBlock()),
            ("timeline", TimelineBlock()),
            ("stats", StatsBlock()),
            ("hero", HeroBlock()),
            ("content_list", ContentListBlock()),
            ("content_with_images", ContentWithImagesBlock()),
            ("logo_cloud", LogoCloudBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    content_panels = (
        *Page.content_panels,
        FieldPanel("body"),
    )

    parent_page_types = ["home.HomePage"]
    subpage_types = []


@register_snippet
class Footer(ClusterableModel):
    """Footer model."""

    text = RichTextField(help_text="Footer text.", null=True)

    panels = (
        FieldPanel("text"),
        InlinePanel("footer_links", label="Footer Links"),
    )


@register_snippet
class NavBar(ClusterableModel):
    logo = models.ImageField(upload_to="images/logos/")

    panels = [FieldPanel("logo"), InlinePanel("nav_links", label="Nav Links")]


class Link(models.Model):
    nav_bar = ParentalKey(NavBar, related_name="nav_links", null=True, blank=True)
    footer = ParentalKey(Footer, related_name="footer_links", null=True, blank=True)

    text = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel("url"),
        FieldPanel("text"),
    ]
