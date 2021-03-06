

class SearchWay:
    """
    The path algorithm. Yep, it is ugly for now
    """
    depth_maplist = []
    path = []

    def addDepth(self, x, y, i):
        max_x, max_y = 64, 32
        # everything what is not a "-" is a wall
        if x > -1 and y > -1 and x < max_x and y < max_y  \
                and self.depth_maplist[y][x] == "-":
            self.depth_maplist[y][x] = str(i)

    def trackItDown(self, x, y):
        current_x = x
        current_y = y
        # if target not in vision field (-)

        if self.depth_maplist[y][x] == '-':
            # can't make the path
            self.path = []
        else:
            i = int(self.depth_maplist[y][x])
            while i > 0:
                self.path.append([current_x, current_y])
                i = i - 1
                if current_x > - 1 and current_y > - 1 and current_x + 1 < 63 \
                        and current_y < 31 and \
                        self.depth_maplist[current_y][current_x + 1] == str(i):
                    current_x = current_x + 1
                elif current_x - 1 > - 1 and current_y > - 1 and current_x < 63 \
                        and current_y < 31 \
                        and self.depth_maplist[current_y][current_x - 1] == str(i):
                    current_x = current_x - 1
                elif current_x > - 1 and current_y > - 1 and current_x < 63 \
                        and current_y + 1 < 31 and \
                        self.depth_maplist[current_y + 1][current_x] == str(i):
                    current_y = current_y + 1
                elif current_x > - 1 and current_y - 1 > - 1 and current_x < 63 \
                        and current_y < 31 and \
                        self.depth_maplist[current_y - 1][current_x] == str(i):
                    current_y = current_y - 1
                elif current_x > - 1 and current_y > - 1 and current_x + 1 < 63 \
                        and current_y + 1 < 31 \
                        and self.depth_maplist[current_y + 1][current_x + 1] == str(i):
                    current_x += 1
                    current_y += 1
                elif current_x - 1 > -1 and current_y-1 > -1 and current_x < 63 \
                        and current_y < 31 \
                        and self.depth_maplist[current_y-1][current_x - 1] == str(i):
                    current_x -= 1
                    current_y -= 1
                elif current_x - 1 > -1 and current_y > -1 and current_x < 63 \
                        and current_y + 1 < 31 and \
                        self.depth_maplist[current_y + 1][current_x - 1] == str(i):
                    current_x -= 1
                    current_y += 1
                elif current_x > -1 and current_y - 1 > -1 and current_x + 1 < 63 \
                        and current_y < 31 \
                        and self.depth_maplist[current_y - 1][current_x + 1] == str(i):
                    current_x += 1
                    current_y -= 1
            self.path.reverse()

    def wave(self, x1, y1, x2, y2, npcs, maplist):
        self.path.clear()
        self.depth_maplist = list(maplist[:])
        for element in npcs:
            if element.is_dead is False:
                self.depth_maplist[element.y][element.x] = "#"
        i = 1
        self.depth_maplist[y1][x1] = "0"
        self.addDepth(x1 + 1, y1, 1)
        self.addDepth(x1, y1 + 1, 1)
        self.addDepth(x1, y1, 1)
        self.addDepth(x1 - 1, y1, 1)
        self.addDepth(x1 + 1, y1 + 1, 1)
        self.addDepth(x1, y1 - 1, 1)
        self.addDepth(x1 - 1, y1 - 1, 1)
        self.addDepth(x1 + 1, y1 - 1, 1)
        self.addDepth(x1 - 1, y1 + 1, 1)
        min_x = x1 - 10
        if min_x < 0:
            min_x = 0
        max_x = x1 + 10
        if max_x > 63:
            max_x = 63
        min_y = y1 - 10
        if min_y < 0:
            min_y = 0
        max_y = y1 + 10
        if max_y > 31:
            max_y = 31
        for iii in range(0, 10):
            ix = 0
            for ix in range(min_x, max_x):
                iy = 0
                for iy in range(min_y, max_y):
                    if self.depth_maplist[iy][ix] == str(i):
                        ii = i + 1
                        self.addDepth(ix+1, iy, ii)
                        self.addDepth(ix + 1, iy + 1, ii)
                        self.addDepth(ix, iy + 1, ii)
                        self.addDepth(ix-1, iy, ii)
                        self.addDepth(ix - 1, iy - 1, ii)
                        self.addDepth(ix, iy - 1, ii)
                        self.addDepth(ix + 1, iy-1, ii)
                        self.addDepth(ix - 1, iy + 1, ii)
            i = i + 1
        self.trackItDown(x2, y2)
