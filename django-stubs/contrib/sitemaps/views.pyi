# Stubs for django.contrib.sitemaps.views (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.core.handlers.wsgi import WSGIRequest
from django.template.response import TemplateResponse
from typing import Callable, Dict, Optional, Type, Union

def x_robots_tag(func: Callable) -> Callable: ...
def index(
    request: WSGIRequest,
    sitemaps: Dict[str, Type[Sitemap]],
    template_name: str = ...,
    content_type: str = ...,
    sitemap_url_name: str = ...,
) -> TemplateResponse: ...
def sitemap(
    request: WSGIRequest,
    sitemaps: Dict[str, Union[Type[Sitemap], Type[FlatPageSitemap], GenericSitemap]],
    section: Optional[str] = ...,
    template_name: str = ...,
    content_type: str = ...,
) -> TemplateResponse: ...