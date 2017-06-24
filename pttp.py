import curses, sys, getopt, subprocess, visualizer
version_number = "ALFA 0.1"


class FileParser:

   def __init__(self,filename):
      print "Init file parser"
      self.filename = filename
      self.pages = []

   def get_pages(self):
      print "in get pages"
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
      print "Add line " + line
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
         self.eop = true
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
    print "Init ctrl"
    self.filename = filename
    self.vis = visualizer_class()
    self.cur_page = 0

  def close(self):
    self.vis.close

  def run(self):
     print "loading pages from " + self.filename
     self.reload_file = False
     parser = FileParser(self.filename)
     print parser
     self.pages = parser.get_pages()
     if self.cur_page >= self.pages.size:
         self.cur_page = self.pages.size - 1
     self.vis.clear()
     self.vis.new_page()
     self.do_run()
     # while self.reload_file

  def do_run(self):

    loop do
      wait = False
      self.vis.draw_slidenum(self.cur_page + 1, self.pages.size, False)
      # read and visualize lines until the visualizer says "stop" or we reached end of page
      begin
        line = self.pages[self.cur_page].next_line
        eop = self.pages[self.cur_page].eop?
        wait = self.vis.visualize(line)
      end while not wait and not eop
      # draw slide number on the bottom left and redraw:
      self.vis.draw_slidenum(self.cur_page + 1, self.pages.size, eop)
      self.vis.do_refresh()

      # read a character from the keyboard
      # a "break" in the when means that it breaks the loop, i.e. goes on with visualizing lines
      loop do
        ch = self.vis.get_key()
        case ch
          when :quit
            return
          when :redraw
            # @todo: actually implement redraw
          when :lastpage
            self.cur_page = self.pages.size - 1
            break
          when :edit
            if self.vis.getLastFile()
              screen = self.vis.store_screen
              Kernel.system("vim " + @vis.getLastFile)
              self.vis.restore_screen(screen)
            end
            break
          when :firstpage
            self.cur_page = 0
            break
          when :jumptoslide
            screen = self.vis.store_screen
            p = self.vis.read_newpage(self.pages,self.cur_page)
            if p >= 0 and p < self.pages.size
              self.cur_page = p
              slef.pages[self.cur_page].reset_eop
              self.vis.new_page
            else
              self.vis.restore_screen(screen)
            end
            break
          when :reload
            self.reload_file = True
            return
          when :help
            screen = self.vis.store_screen()
            self.vis.show_help_page()
            ch = self.vis.get_key()
            self.vis.clear()
            self.vis.restore_screen(screen)
          when :keyright
            if self.cur_page + 1 < self.pages.size and eop then
              self.cur_page += 1
              self.pages[@cur_page].reset_eop()
              self.vis.new_page()
            end
            break
          when :keyleft
            if self.cur_page > 0 then
              self.cur_page -= 1
              self.pages[self.cur_page].reset_eop
              self.vis.new_page
            end
            break
          when :keyresize
            self.vis.setsizes()
        end
      end
    end # loop
  end

end




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
      ctrl = InteractiveController(input,visualizer.NcursesVisualizer)
   elif type ==  "autoplay":
      ctrl = AutoplayController(input,time,visualizer.NcursesVisualizer)
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

   print "Starting ctrl"
   ctrl.run()
   ctrl.close
 
   exit(0)


if __name__ == "__main__":
   main(sys.argv[1:])
