import re

from django.utils.translation import get_language, ugettext_lazy as _
from django.conf import settings


def is_multilingual():
    return 'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware' in settings.MIDDLEWARE_CLASSES


def get_lang_name(lang):
    return _(dict(settings.LANGUAGES)[lang])


def has_lang_prefix(path):

    if settings.CMS_LANGUAGES:
        HAS_LANG_PREFIX_RE = re.compile(r"^/(%s)/.*" % "|".join([re.escape(l[0]) for l in settings.CMS_LANGUAGES]))
        check = HAS_LANG_PREFIX_RE.match(path)
        if check is not None:
            return check.group(1)
    else:
        return False


def add_current_root(url):
    if is_multilingual() and not has_lang_prefix(url):
        new_root = "/%s" % get_language()
        url = new_root + url
    return url
