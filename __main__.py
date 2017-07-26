#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

site=None
if len(sys.argv) == 1:
    print "Name of site is missing. usage : $ python WebPo mySite"
    pass
else:
    site=sys.argv[1]
    sys.argv.remove(sys.argv[1])

MAIN_GFOLDER = '0BziWsJYs4XsYa0R1Z0UyYjBGcVk'
SITEMAPPING = '1G2r5JHioBuV3otbZO5KVurKfhHY5b7EmDafoc3WjB0E'

if site:
    from gooThon.gsettings import gsettings
    import gooThon.goo
    #get Gdrive folder ID
    folderId = gsettings(SITEMAPPING, site).getId()

    # get list of files inside folder ID
    files = gooThon.goo.main('list', folderId, None)
    for f in files:
        #get the content of the file
        mime = 'text/plain'
        if f['mime'] == 'application/vnd.google-apps.spreadsheet':
            mime = 'text/csv'
        elif f['mime'] == 'application/vnd.google-apps.document':
            mime = 'text/html'

        content = gooThon.goo.main('content', f['id'], mime)

        # #convert the content to usable html
        import gooThon.htmlcreator
        content = gooThon.htmlcreator.main(content, mime, f['name'])
        print content

        #push html file to pelican folder
        import os
        BASEDIR = os.getcwd()
        dirfile = BASEDIR + '/WebPo/pelican/content/'+f['name']+'.html'
        fi = open(dirfile, 'w')
        fi.write(content)
        fi.closed


print "DONE!!"

