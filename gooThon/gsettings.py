#!/usr/bin/env python
# -*- coding: utf-8 -*-
import goo

class gsettings:
    def __init__(self, fileId, site):
        self.fileId=fileId
        self.site = site
        self.settings = goo.main('settings', fileId, None)
        self.folderId = self.getId()
                
    def get(self):
        return self.settings
        
    def getId(self):
        rows = self.settings.split("\n")
        for r in rows:
            column = r.split(',')
            if column[1] == self.site:
                return column[2]
        
        
if __name__ == "__main__":
    pass
