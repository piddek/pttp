import pdb
import curses, sys, getopt, subprocess, visualize
version_number = "ALFA 0.1"


class FileParser:

   def __init__(self,filename):
      # print "Init file parser"
      self.filename = filename
      self.pages = []

   def get_pages(self):
      # print "in get pages"
      try:
         f = open(self.filename)
      except (IOError, OSError) as e:
         print "Could not open file " + self.filename
	 print e
         sys.exit(1)
      number_pages = 0
      cur_page = Page("Title")
      for line in f:
         line = line.rstrip()
         if line.startswith("--##"): 
            pass # ignore comments
         elif line.startswith("--newpage"): 
            print "Got new page"
            self.pages.append(cur_page)
            number_pages += 1
	    name = line[9:] # Remove --newpage(9 characters) and check if anything is left
            if name == "":
               name = "slide " + str(number_pages+1)
            else:
               name.rstrip()
            cur_page = Page(name)
         else:
            cur_page.add_line(line)
      print self.pages
      return(self.pages)

class Page:

   def __init__(self,title):
      print "in init page"
      self.lines = []
      self.title = title
      self.cur_line = 0
      self.eop = 0

   # Appends a line to the page, but only if _line_ is not null
   def add_line(self,line):
      # print "Add line " + line
      if line != "":
         self.lines.append(line)
         prefix = ""
         if line.startswith("$$") or line.startswith("$%"):
            if line.startswith("$%"):
               prefix = "%"
            cmd = line[2:]
            try:
               output = subprocess.check_output(cmd.split())
               for row in output.split('\n'):
                  self.lines.append(prefix+row)
                  print "Adding cmd output " + prefix + row
            except Exception as e:
               print e
               self.lines.append(e)


      
   # Returns the next line. In case the last line is hit, then the end-of-page marker is set.
   def next_line(self):
      line = self.lines[self.cur_line]
      self.cur_line = self.cur_line + 1
      if self.cur_line >= len(self.lines):
         self.eop = True
      return(line)

   def is_eop(self):
      return(self.eop)


   # Resets the end-of-page marker and sets the current line marker to the first line
   def reset_eop(self):
      self.cur_line=0
      self.eop = False

   # Returns all lines in the page.
   def lines(self):
      return(self.lines)

   # Returns the page's title
   def title(self):
      return(self.title)
    


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


class TppControler: #Abstract class for any controller

   def __init__(self):
      print "Error: TppController.initialize has been called directly!"
      sys.exit(1)
   def close(self):
      print "Error: TppController.initialize has been called directly!"
      sys.exit(1)
   def run(self):
      print "Error: TppController.initialize has been called directly!"
      sys.exit(1)


class InteractiveController(TppControler):

  def __init__(self,filename,visualizer_class):
    # print "Init ctrl"
    self.filename = filename
    self.vis = visualizer_class()
    self.cur_page = 0

  def close(self):
    self.vis.close

  def run(self):
     try: 
        # print "loading pages from " + self.filename
        self.reload_file = False
        parser = FileParser(self.filename)
        print parser
        self.pages = parser.get_pages()
        if self.cur_page >= len(self.pages):
           self.cur_page = len(self.pages) - 1
        self.vis.clear()
        self.vis.new_page()
        self.do_run()
        # while self.reload_file
     except Exception as e:
        self.close()
        print e

  def do_run(self):
    try:
      while(True):
          wait = False
          # pdb.set_trace()
          self.vis.draw_slidenum(self.cur_page + 1, len(self.pages), False)
          # read and visualize lines until the visualizer says "stop" or we reached end of page
          iterate = True #emulating do while
          while iterate: 
            # pdb.set_trace()
            line = self.pages[self.cur_page].next_line()
            # print "Da line: ", line
            # pdb.set_trace()
            eop = self.pages[self.cur_page].eop
            # pdb.set_trace()           
            wait = self.vis.visualize(line)
            # pdb.set_trace()
            iterate =  not wait and not eop
          # draw slide number on the bottom left and redraw:
          self.vis.draw_slidenum(self.cur_page + 1, len(self.pages), eop)
          self.vis.do_refresh()

          # read a character from the keyboard
          # a "break" in the when means that it breaks the loop, i.e. goes on with visualizing lines
          while(True):
            ch = self.vis.get_key()
            if ch == "quit":
                return
            elif ch =="redraw":
                # @todo: actually implement redraw
                pass
            elif ch == "lastpage":
                self.cur_page = len(self.pages) - 1
                break
            elif ch == "edit":
                if self.vis.getLastFile():
                  screen = self.vis.store_screen()
                  Kernel.system("vim " + self.vis.getLastFile)
                  self.vis.restore_screen(screen)
                break
            elif ch == "firstpage":
                self.cur_page = 0
                break
            elif ch == "jumptoslide":
                screen = self.vis.store_screen
                p = self.vis.read_newpage(self.pages,self.cur_page)
                if p >= 0 and p < len(self.pages):
                  self.cur_page = p
                  self.pages[self.cur_page].reset_eop()
                  self.vis.new_page()
                else:
                  self.vis.restore_screen(screen)
                break
            elif ch == "reload":
                self.reload_file = True
                return
            elif ch == "help":
                screen = self.vis.store_screen()
                self.vis.show_help_page()
                ch = self.vis.get_key()
                self.vis.clear()
                self.vis.restore_screen(screen)
            elif  ch == "keyright":
                if (self.cur_page + 1 < len(self.pages)) and eop:
                  self.cur_page += 1
                  self.pages[self.cur_page].reset_eop()
                  self.vis.new_page()
                break
            elif ch == "keyleft":
                if self.cur_page > 0:
                  self.cur_page -= 1
                  self.pages[self.cur_page].reset_eop()
                  self.vis.new_page()
                break
            elif ch == "keyresize":
                self.vis.setsizes()
            else:
                pass # unknown key, do nothing
    except Exception as e:
        self.close()
        print e


def main(argv):
   type = "ncurses"
   output = ""
   try:
      opts, args = getopt.getopt(argv,"t:o:s:vh",["type=","outputfile","seconds=","version","help"])
   except getopt.GetoptError:
      usage();
   # print opts
   # print args
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
   # print 'Input file is ', input
   # print 'Type is ', type

   if type == "ncurses":   # No swich case in python
      # pdb.set_trace()
      ctrl = InteractiveController(input,visualize.NcursesVisualizer)
   elif type ==  "autoplay":
      ctrl = AutoplayController(input,time,visualize.NcursesVisualizer)
   elif type ==  "txt":
      if output == "":
         print "Missing output file!"
         usage()
      else:
         ctrl = ConversionController(input,output,TextVisualizer)
   elif type == "latex":
       if output == "":
          print "Missing output file!"
          usage()
       else:
          ctrl = ConversionController(input,output,LatexVisualizer)
   else:
      usage()

   # print "Starting ctrl"
   ctrl.run()
   ctrl.close
 
   exit(0)


if __name__ == "__main__":
   main(sys.argv[1:])
