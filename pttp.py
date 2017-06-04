import curses, sys, getopt

#  Prints a nicely formatted usage message.
def usage():
  print "usage: pttp [-t <type> -o <file>] <file>\n"
  print "\t -t <type>\tset filetype <type> as output format"
  print "\t -o <file>\twrite output to file <file>"
  print "\t -s <seconds>\twait <seconds> seconds between slides (with -t autoplay)"
  print "\t --version\tprint the version"
  print "\t --help\t\tprint this help"
  print  "\n\t currently available types: ncurses (default), autoplay, latex, txt"
  sys.exit(1)

def version():
  print "\t This is pttp and pyton port of tpp Alfa 0.1"
  sys.exit(1)


def pttp():
        begin_x = 20; begin_y = 7
        height = 5; width = 40
        win = curses.newwin(height, width, begin_y, begin_x)
        stdscr.addstr(5, 7, "Current mode: Typing mode", curses.A_REVERSE)
        stdscr.refresh()
        while 1:
                c = stdscr.getch()
                if c == ord('p'):
                        PrintDocument()
                elif c == ord('q'):
                        break  # Exit the while()



def statr():
   stdscr = curses.initscr()
   curses.noecho()
   curses.cbreak()
   stdscr.keypad(1)
   try:
      ptttp();
   except Exception as e:
      print("hoppsan!");

   curses.nocbreak()
   stdscr.keypad(0)
   curses.echo()
   curses.endwin()
   exit(0)


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"t:o:s:vh",["--type=","--file","--seconds=","--version","--help"])
   except getopt.GetoptError:
      usage();
   if (len(args) == 0 and len(opts) ==0):
      usage();
   for opt, arg in opts:
      if opt in( '-h',"--help"):
         usage()
      if opt in( '-v',"--version"):
         version()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile


if __name__ == "__main__":
   main(sys.argv[1:])




