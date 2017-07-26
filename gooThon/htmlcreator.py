#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(content, mime, name):
    if mime == 'text/csv':
        pass
    if mime == 'text/html':
        content = insertMetas(content, name)
        # content = deleteTag(content, "<head>.*?<\/head>")

    return content
    
    
def deleteTag(content, tag):
    import re
    m = re.search(tag, content)
    if m:
        content = content.replace(m.group(0), '')

    return content


def insertMetas(content, name):
    import re
    from datetime import date
    rx = "<p class=\"title\".*?><span.*?>(.*?)</span></p>"
    m = re.search(rx, content)
    title = name
    now = date.today()
    d = now.strftime("%Y-%m-%d")
    if m:
        title = m.group(1)
    newhead = '<head><title>' + title + '</title><meta name="date" content="' + d + '" />'
    content = content.replace('<head>', newhead)
    return content
    
    
