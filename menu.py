import curses


class PopUpWindow():
    # all draw_func must have (stdscr, x, y) signature
    def __init__(self, stdscr, x=10, y=7, width=100, height=27,
                 name="pop-up window", draw_func=None, update_func=None):
        self.stdscr = stdscr
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.drawFunc = draw_func
        self.updateFunc = update_func
        self.is_visible = False
        # horizontal line
        self.top_h_line = u'\u250c{0}\u2510'.format((self.width-2)*u'\u2500')
        self.bottom_h_line = u'\u2514{0}\u2518'.format((self.width-2)*u'\u2500')
        self.blank_space = (self.width-4)*' '
        self.content_line = u'\u2502 {0} \u2502'.format(self.blank_space)

    def draw(self):
        if self.is_visible is True:
            self.stdscr.addstr(self.y, self.x, self.top_h_line)
            self.stdscr.addstr(self.y, self.x + 5, self.name)
            for i in range(1, self.height):
                self.stdscr.addstr(self.y + i, self.x, self.content_line)
            self.stdscr.addstr(self.y + self.height, self.x, self.bottom_h_line)
            self.drawFunc(self.stdscr, self.x, self.y)

    def update(self, input_key):
        self.updateFunc(input_key)


if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    window1 = PopUpWindow(stdscr, 10, 10, 100, 30, 'Inventory')
    window1.is_visible = True

    while True:
        window1.draw()
        c = stdscr.getch()
        if c == ord("q"):
            break
