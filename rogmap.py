# -*- coding: utf-8 -*-
import dungen
class rogmap:
    maplist = []
    room_list = []
    width, height = 64, 32
    def init(self):
        gen = dungen.Generator(self.width,self.height,7)
        gen.gen_level()
        self.maplist = gen.get_tiles_level()
        self.room_list =gen.room_list
    def getmaplist(self):
        return(self.maplist)
