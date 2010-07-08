
from htmlentitydefs import name2codepoint
from re import sub


def decode_html_entities(html): 
    """
    Remove HTML entities from a string.
    Adapted from http://effbot.org/zone/re-sub.htm
    """
    def decode(m):
        html = m.group(0)
        if html[:2] == "&#":
            try:
                if html[:3] == "&#x":
                    return unichr(int(html[3:-1], 16))
                else:
                    return unichr(int(html[2:-1]))
            except ValueError:
                pass
        else:
            try:
                html = unichr(name2codepoint[html[1:-1]])
            except KeyError:
                pass
        return html
    return sub("&#?\w+;", decode, html.replace("&amp;", "&"))

