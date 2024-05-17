"""Stream block definitions."""

from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    DateBlock,
    ListBlock,
    PageChooserBlock,
    StructBlock,
    TextBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class HeroImageBlock(StructBlock):
    """Hero image block."""

    image = ImageChooserBlock(help_text="The image to display.", required=True)

    class Meta:
        """Meta attributes."""

        icon = "image"
        template = "blocks/hero_image_block.html"


class GalleryImageBlock(StructBlock):
    """Individual gallery image block."""

    image = ImageChooserBlock(help_text="Choose an image.", required=True)
    caption = CharBlock(help_text="An optional caption for the image.", required=False)

    class Meta:
        """Meta attributes."""

        icon = "image"
        template = "blocks/gallery_image_block.html"


class GalleryBlock(StructBlock):
    """Gallery block."""

    title = CharBlock(
        help_text="An optional title for the gallery.",
        required=False,
        max_length=50,
    )
    images = ListBlock(GalleryImageBlock())

    class Meta:
        """Meta attributes."""

        icon = "image"
        template = "blocks/gallery_block.html"


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


class Stat(StructBlock):
    number = CharBlock()  # not an actual number to give flexibility in formatting
    title = CharBlock()
    description = TextBlock()
    size = ChoiceBlock(
        choices=[
            ("small", "Small"),
            ("medium", "Medium"),
            ("large", "Large"),
        ],
    )


class StatsBlock(StructBlock):
    "Stats Block"

    title = CharBlock()
    lead_paragraph = TextBlock()
    stats = ListBlock(Stat(), max_num=3)

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
    content_list = ListBlock(ContentListItemBlock(), max_num=3)

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
