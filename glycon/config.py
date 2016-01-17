from glycon.models import Page, Article, Block
from glycon_summaries.models import Summary, SummaryBlock
from glycon_menu_blocks.models import MenuBlock
from glycon_disqus.models import DisqusBlock

SITENAME = "Ben Collier"
GLYCON_MEDIA_URL = "/media/"
HOME_URL = "front"


CONTENT_TYPES = {
    "Page": Page,
    "Article": Article,
    "Summary": Summary
}

BLOCK_TYPES = {
    "Block": Block,
    "SummaryBlock": SummaryBlock,
    "MenuBlock": MenuBlock,
    "DisqusBlock": DisqusBlock
}