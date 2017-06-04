import curses, sys, getopt
version_number = "ALFA 0.1"

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
  print "\t This is pttp and pyton port of tpp " + version_number
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
   type = "ncurses"
   output = ""
   try:
      opts, args = getopt.getopt(argv,"t:o:s:vh",["type=","outputfile","seconds=","version","help"])
   except getopt.GetoptError:
      usage();
   print opts
   print args
   if (len(args) == 0 and len(opts) ==0) or (len(args) > 1):
      usage();
   for opt, arg in opts:
      if opt in( "-h","--help"):
         usage()
      if opt in( "-v","--version"):
         version()
      elif opt in ("-t", "--type"):
         type = arg
      elif opt in ("-o", "--outputfile"):
         output = arg
      elif opt in ("-s", "--seconds"):
         time = int(arg)
   input = args[0]
   print 'Input file is ', input
   print 'Type is ', type

   if type == "ncurses":   # No swich case in python
      ctrl = InteractiveController.new(input,NcursesVisualizer)
   elif type ==  "autoplay":
      ctrl = AutoplayController.new(input,time,NcursesVisualizer)
   elif type ==  "txt":
      if output == "":
         print "Missing output file!"
         usage()
      else:
         ctrl = ConversionController.new(input,output,TextVisualizer)
   elif type == "latex":
       if output == "":
          print "Missing output file!"
          usage()
       else:
          ctrl = ConversionController.new(input,output,LatexVisualizer)
   else:
      usage()


if __name__ == "__main__":
   main(sys.argv[1:])
