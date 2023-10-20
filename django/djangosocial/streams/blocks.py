"""Stream block definitions."""

from wagtail.blocks import StructBlock, CharBlock, TextBlock, ListBlock, DateBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class HeroImageBlock(StructBlock):
    """Hero image block."""

    image = ImageChooserBlock(help_text="The image to display.", required=True)

    class Meta:
        """Meta attributes."""

        icon = "image"
        template = "blocks/hero_image_block.html"


class TimelineMomentBlock(StructBlock):
    date = DateBlock()
    title = CharBlock()
    description = TextBlock()

    class Meta:
        template = "blocks/timeline_moment_block.html"

class TimelineBlock(StructBlock):
    "Timeline Block"

    timeline_moments = ListBlock(TimelineMomentBlock())
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


class ContentListItemBlock(StructBlock):
    title = CharBlock()
    lead_paragraph = TextBlock()
    link = PageChooserBlock()

class ContentListBlock(StructBlock):
    "ContentList Block"
    title = CharBlock()
    lead_paragraph = TextBlock()
    image = ImageChooserBlock()

    list_title = CharBlock()
    list_type = CharBlock(help_text="What does the list of represent? (eg roles, events)")
    content_list = ListBlock(ContentListItemBlock())

    more_list_text = CharBlock()
    more_list_link = PageChooserBlock()

    class Meta:
        template = "blocks/content_with_list.html"

class ContentWithImagesBlock(StructBlock):
    "Content With Images Block"

    title = CharBlock()
    lead_paragraph = TextBlock()
    secondary_paragraph = TextBlock()

    top_image = ImageChooserBlock()
    bottom_left_image = ImageChooserBlock()
    bottom_center_image = ImageChooserBlock()
    bottom_right_image = ImageChooserBlock()

    class Meta:
        template = "blocks/content_with_images_block.html"


class LogoCloudBlock(StructBlock):
    "Logo Cloud Block"

    title = CharBlock()
    lead_paragraph = TextBlock()
    logos = ListBlock(ImageChooserBlock())

    class Meta:
        template = "blocks/logocloud_block.html"
