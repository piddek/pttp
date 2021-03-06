import curses
 # Maps color names to constants and indexes.
class ColorMap:

    # Maps color name _color_ to a constant
    def get_color(this, color):
        colors = { "white" : curses.COLOR_WHITE,
                   "yellow" : curses.COLOR_YELLOW,
                   "red" : curses.COLOR_RED,
                   "green" : curses.COLOR_GREEN,
                   "blue" : curses.COLOR_BLUE,
                   "cyan" : curses.COLOR_CYAN,
                   "magenta" : curses.COLOR_MAGENTA,
                   "black" : curses.COLOR_BLACK,
                   "default" : -1 }
        return colors[color]
       
    # Maps color name to a color pair index
    def get_color_pair(this, color):
        colors = { "white" : 1,
                   "yellow" : 2,
                   "red" : 3,
                   "green" : 4,
                   "blue" : 5,
                   "cyan" : 6,
                   "magenta" : 7,
                   "black" : 8,
                   "default" : -1}
        return curses.color_pair(colors[color])
