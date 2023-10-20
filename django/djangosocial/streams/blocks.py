"""Stream block definitions."""

from wagtail.blocks import StructBlock, CharBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock


class HeroImageBlock(StructBlock):
    """Hero image block."""

    image = ImageChooserBlock(help_text="The image to display.", required=True)

    class Meta:
        """Meta attributes."""

        icon = "image"
        template = "blocks/hero_image_block.html"


class TimelineBlock(StructBlock):
    "Timeline Block"


    class Meta:
        template = "blocks/timeline_block.html"

class StatsBlock(StructBlock):
    "Stats Block"


    class Meta:
        template = "blocks/stats_block.html"

class HeroBlock(StructBlock):
    "Hero Block"

    title = CharBlock()
    lead_paragraph = TextBlock()
    image = ImageChooserBlock(help_text="The image to display.", required=True)

    class Meta:
        template = "blocks/hero_block.html"

class ContentListBlock(StructBlock):
    "ContentList Block"


    class Meta:
        template = "blocks/content_with_list.html"

class ContentWithImagesBlock(StructBlock):
    "Content With Images Block"


    class Meta:
        template = "blocks/content_with_images_block.html"


class LogoCloudBlock(StructBlock):
    "Logo Cloud Block"

    class Meta:
        template = "blocks/logocloud_block.html"
