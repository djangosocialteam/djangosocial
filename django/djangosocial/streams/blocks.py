"""Stream block definitions."""

from wagtail.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock


class HeroImageBlock(StructBlock):
    """Hero image block."""

    image = ImageChooserBlock(help_text="The image to display.", required=True)

    class Meta:
        """Meta attributes."""

        icon = "image"
        template = "blocks/hero_image_block.html"
