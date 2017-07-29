import datetime, curses,time,pdb,colormap,sys,tempfile, random

class TppVisualizer:

  def __init__(self, stdsct):
    pass

  # Splits a line into several lines, where each of the result lines is at most
  # _width_ characters long, caring about word boundaries, and returns an array
  # of strings.
  def split_lines(self,text,width):
    lines = []
    if text != "":
		while len(text) > 0:
			i = width
                        # pdb.set_trace()
			if len(text) <= i: # text length is OK -> add it to array and stop splitting
			  lines.append(text)
			  text = ""
			else:
			  # search for word boundary (space actually)
			  while i > 0 and text[i] != ' ':
				i -= 1
			  # if we can't find any space character, simply cut it off at the maximum width
			  if i == 0:
				i = width
			  # extract line
			  x = text[:i]
			  # remove extracted line
			  text = text[i+1:]
			  # added line to array
			  lines.append(x)
    return lines

  def do_footer(self, footer_text):
    print "Error: TppVisualizer#do_footer has been called directly."
    sys.exit(1)
  

  def do_header(self, header_text):
    print "Error: TppVisualizer#do_header has been called directly."
    sys.exit(1)
  


  def do_refresh(self):
    print "Error: TppVisualizer#do_refresh has been called directly."
    sys.exit(1)
  

  def new_page(self):
    print "Error: TppVisualizer#new_page has been called directly."
    sys.exit(1)
  

  def do_heading(self, text):
    print "Error: TppVisualizer#do_heading has been called directly."
    sys.exit(1)
  

  def do_withborder(self):
    print "Error: TppVisualizer#do_withborder has been called directly."
    sys.exit(1)
  

  def do_horline(self):
    print "Error: TppVisualizer#do_horline has been called directly."
    sys.exit(1)
  

  def do_color(self, text):
    print "Error: TppVisualizer#do_color has been called directly."
    sys.exit(1)
  

  def do_center(self, text):
    print "Error: TppVisualizer#do_center has been called directly."
    sys.exit(1)
  

  def do_right(self, text):
    print "Error: TppVisualizer#do_right has been called directly."
    sys.exit(1)
  

  def do_exec(self, cmdline):
    print "Error: TppVisualizer#do_exec has been called directly."
    sys.exit(1)
  

  def do_wait(self):
    print "Error: TppVisualizer#do_wait has been called directly."
    sys.exit(1)
  

  def do_beginoutput(self):
    print "Error: TppVisualizer#do_beginoutput has been called directly."
    sys.exit(1)
  

  def do_beginshelloutput(self):
    print "Error: TppVisualizer#do_beginshelloutput has been called directly."
    sys.exit(1)
  

  def do_endoutput(slef):
    print "Error: TppVisualizer#do_endoutput has been called directly."
    sys.exit(1)
  

  def do_endshelloutput(self):
    print "Error: TppVisualizer#do_endshelloutput has been called directly."
    sys.exit(1)
  

  def do_sleep(self, time2sleep):
    print "Error: TppVisualizer#do_sleep has been called directly."
    sys.exit(1)
  

  def do_boldon(self):
    print "Error: TppVisualizer#do_boldon has been called directly."
    sys.exit(1)
  

  def do_boldoff(self):
    print "Error: TppVisualizer#do_boldoff has been called directly."
    sys.exit(1)
  

  def do_revon(self):
    print "Error: TppVisualizer#do_revon has been called directly."
    sys.exit(1)
  

  def do_revoff(self):
    print "Error: TppVisualizer#do_revoff has been called directly."
    sys.exit(1)
  

  def do_ulon(self):
    print "Error: TppVisualizer#do_ulon has been called directly."
    sys.exit(1)
  

  def do_uloff(self):
    print "Error: TppVisualizer#do_uloff has been called directly."
    sys.exit(1)
  

  def do_beginslideleft(self):
    print "Error: TppVisualizer#do_beginslideleft has been called directly."
    sys.exit(1)
  

  def do_endslide(self):
    print "Error: TppVisualizer#do_endslide has been called directly."
    sys.exit(1)
  

  def do_beginslideright(self):
    print "Error: TppVisualizer#do_beginslideright has been called directly."
    sys.exit(1)
  

  def do_beginslidetop(self):
    print "Error: TppVisualizer#do_beginslidetop has been called directly."
    sys.exit(1)
  

  def do_beginslidebottom(self):
    print "Error: TppVisualizer#do_beginslidebottom has been called directly."
    sys.exit(1)
  

  def do_sethugefont(self):
    print "Error: TppVisualizer#do_sethugefont has been called directly."
    sys.exit(1)
  

  def do_huge(self, text):
    print "Error: TppVisualizer#do_huge has been called directly."
    sys.exit(1)
  

  def print_line(self, line):
    print "Error: TppVisualizer#print_line has been called directly."
    sys.exit(1)
  

  def do_title(self, title):
    print "Error: TppVisualizer#do_title has been called directly."
    sys.exit(1)
  

  def do_author(self, author):
    print "Error: TppVisualizer#do_author has been called directly."
    sys.exit(1)
  

  def do_date(self, date):
    print "Error: TppVisualizer#do_date has been called directly."
    sys.exit(1)
  

  def do_bgcolor(self, color):
    print "Error: TppVisualizer#do_bgcolor has been called directly."
    sys.exit(1)
  

  def do_fgcolor(self, color):
    print "Error: TppVisualizer#do_fgcolor has been called directly."
    sys.exit(1)
  

  def do_color(self, color):
    print "Error: TppVisualizer#do_color has been called directly."
    sys.exit(1)
  

  # Receives a _line_, parses it if necessary, and dispatches it
  # to the correct method which then does the correct processing.
  # It returns whether the controller shall wait for input.
  def visualize(self, line):
      # print "The value of line is: ",line
      # pdb.set_trace()
      if line.startswith("--heading"):
        text = line.replace("--heading ","")
        self.do_heading(text)
      elif line.startswith("--withborder"):
        self.do_withborder()
      elif line.startswith("--horline"):
        self.do_horline()
      elif line.startswith("--color "):
        text = line.replace("--color ","")
        text = text.rstrip()
        self.do_color(text)
      elif line.startswith("--center "):
        text = line.replace("--center ","")
        self.do_center(text)
      elif line.startswith("--right "):
        text = line.replace("--right ","")
        self.do_right(text)
      elif line.startswith("--exec "):
        cmdline = line.replace("--exec ","")
        self.do_exec(cmdline)
      elif line.startswith("---"):
        # pdb.set_trace()


        self.do_wait()
        return True
      elif line.startswith("--beginoutput"):
        self.do_beginoutput()
      elif line.startswith("--beginshelloutput"):
        self.do_beginshelloutput()
      elif line.startswith("--endoutput"):
        self.do_endoutput()
      elif line.startswith("--endshelloutput"):
        self.do_endshelloutput()
      elif line.startswith("--sleep "):
        time2sleep = line.replace("--sleep ","")
        self.do_sleep(time2sleep)
      elif line.startswith("--boldon"):
        self.do_boldon()
      elif line.startswith("--boldoff"):
        self.do_boldoff()
      elif line.startswith("--revon"):
        self.do_revon()
      elif line.startswith("--revoff"):
        self.do_revoff()
      elif line.startswith("--ulon"):
        self.do_ulon()
      elif line.startswith("--uloff"):
        self.do_uloff()
      elif line.startswith("--beginslideleft"):
        self.do_beginslideleft()
      elif line.startswith(("--endslideleft", "--endslideright", "--endslidetop", "--endslidebottom")):
        self.do_endslide()
      elif line.startswith("--beginslideright"):
        self.do_beginslideright()
      elif line.startswith("--beginslidetop"):
        self.do_beginslidetop()
      elif line.startswith("--beginslidebottom"):
        self.do_beginslidebottom()
      elif line.startswith("--sethugefont "):
        params = line.replace("--sethugefont ","")
        self.do_sethugefont(params.strip())
      elif line.startswith("--huge "):
        figlet_text = line.replace("--huge ","")
        #TODO implement HUDGE/FIGLET 
        # self.do_huge(figlet_text)
      elif line.startswith("--footer "):
        self.footer_txt = line.replace("--footer ","")
        self.do_footer(self.footer_txt)
      elif line.startswith("--header "):
        self.header_txt = line.replace("--header ","")
        self.do_header(self.header_txt)
      elif line.startswith("--title "):
        title = line.replace("--title ","")
        self.do_title(title)
      elif line.startswith("--author "):
        author = line.replace("--author ","")
        self.do_author(author)
      elif line.startswith("--date "):
        date = line.replace("--date ","")
        if (date == "today"):
		  date = datetime.datetime.now().strftime("%b %d %Y") #now with default format
        elif date.startswith("today "):  # this is for now with custom date format
          date = datetime.datetime.now().strftime(date.replace("today ",""))
        self.do_date(date)
      elif line.startswith("--bgcolor "):
        color = line.replace("--bgcolor ","").rstrip()
        self.do_bgcolor(color)
      elif line.startswith("--fgcolor "):
        color = line.replace("--fgcolor ","").rstrip()
        self.do_fgcolor(color)
      elif line.startswith("--color "):
        color = line.replace("--color ","").rstrip()
        self.do_color(color)
      elif line.startswith("--include-file "):
        self.lastFileName = line.replace("--include-file ","").rstrip()
        self.do_beginoutput()
        self.print_line(self.lastFileName)
        self.do_beginoutput()
        f = open(self.lastFileName)
        for line in f:
          line.rstrip()
          if line != "":
            self.print_line(line)
        self.do_endoutput()
      else:
        self.print_line(line)
      return False

def close(self):
    pass

# Implements an interactive visualizer which builds on top of curses.
class NcursesVisualizer(TppVisualizer):

  def __init__(self,stdscr):
   b=0
   try:
    self.cm = colormap.ColorMap()
    self.figletfont = "standard"
    self.slideoutput = False
    # self.screen = curses.initscr()
    self.screen =  stdscr
    curses.curs_set(0)
    curses.cbreak() # unbuffered input
    curses.noecho() # turn off input echoing
    b=1
    curses.intrflush(False)
    b=2
    self.screen.keypad(True)
    b=3
    self.lastFileName = ""
    self.footer_txt = ""
    self.voffset = 5
    self.indent = 3
    self.header_txt = ""
    b=4
    b=5
    self.setsizes()
    b=6
    curses.start_color()
    b=7
    curses.use_default_colors()
#    for i in range(0,curses.COLORS):
 #      curses.init_pair(i+1, i, curses.COLOR_RED)
#    self.screen.addstr('Abban is a kaffit', curses.color_pair(4))
#    self.screen.getch()
#    pdb.set_trace()
    b=8
#    curses.init_color(curses.COLOR_BLUE,0,0, 100)
    self.do_bgcolor("black")
    b=9
    self.do_fgcolor("white")
    b=10
    # self.fgcolor = self.cm.get_color_pair("black")
    print b
    self.cur_line = self.voffset
    self.output = self.shelloutput = False
   except Exception as e:
    curses.nocbreak()
    # self.screen.keypad(False)
    curses.echo()
    curses.endwin()
    print e
    print "Nu blev det rumpa: " +str(b)
    sys.exit()


  def get_key(self):
    ch = self.screen.getch()
    if ch in [ord('d'), ord('D'), ord('j'), ord('J'), ord('l'), ord('L'), curses.KEY_DOWN, curses.KEY_RIGHT]:
        return "keyright"
    if ch in [ord('a'), ord('A'), ord('b'), ord('B'), ord('h'), ord('H'), ord('k'), ord('K'), curses.KEY_UP, curses.KEY_LEFT]:
        return "keyleft"
    if ch in [ord('z'), ord('Z')]:
        return "keyresize"
    if ch in [ord('r'), ord('R')]:
        return "reload"
    if ch in [ord('q'), ord('Q')]:
        return "quit"
    if ch in [ord('s'), ord('S')]:
        return "firstpage"
    if ch in [ord('e'), ord('E')]:
        return "edit"
    if ch in [ord('g'), ord('G')]:
        return "jumptoslide"
    if ch in [ord('?')]:
        return "help"
    else:
        return "keyright"

  def clear(self):
    self.screen.clear()
    self.screen.refresh()

  def do_refresh(self):
    self.screen.refresh()

  def do_withborder(self):
    self.withborder = True
    self.draw_border()
    self.withborder = True

  def setsizes(self):
    self.termheight, self.termwidth  = self.screen.getmaxyx() # set sizes

  def draw_border(self):
    self.screen.addstr(0,0,".")
    for i in range (self.termwidth-2):
        self.screen.addstr("-")
    self.screen.addstr(".")
    # self.screen.move(self.termheight-2,0)
    self.screen.addstr(self.termheight-2,0,"`")
    for i in range(self.termwidth-2):
        self.screen.addstr("-")
    self.screen.addstr("'")
    for y in range(1, self.termheight -2): #python does not include stop value    
      # self.screen.move(y,0)
      self.screen.addstr(y,0,"|")
    for y in range(1, self.termheight -2): #python does not include stop value    
      # self.screen.move(y,self.termwidth-1)
      self.screen.addstr(y, self.termwidth-1,"|")

  def new_page(self):
    self.cur_line = self.voffset
    self.output = self.shelloutput = False
    self.setsizes()
    self.screen.clear()

  def do_heading(self, line):
    self.screen.attron(curses.A_BOLD)
    self.print_heading(line)
    self.screen.attroff(curses.A_BOLD)

  def do_horline(self):
    # pdb.set_trace()
    self.screen.attron(curses.A_BOLD)
    for x in range(1,self.termwidth):
      self.screen.move(self.cur_line,x)
      self.screen.addstr("-")
    self.screen.attroff(curses.A_BOLD)

  def print_heading(self,text):
    width = self.termwidth - 2*self.indent
    lines = self.split_lines(text,width)
    for l in lines:
      self.screen.move(self.cur_line,self.indent)
      x = (self.termwidth - len(l))/2
      self.screen.addstr(self.cur_line,x,l)
      self.cur_line += 1

  def do_center(self,text):
    # self.screen.move(1,1)
    # self.screen.addstr("in do_center")
    width = self.termwidth - 2*self.indent
    if self.output or self.shelloutput:
      width -= 2
    lines = self.split_lines(text,width)
    # pdb.set_trace()
    for l in lines:
      self.screen.move(self.cur_line,self.indent)
      if self.output or self.shelloutput:
        self.screen.addstr("| ")
      x = (self.termwidth - len(l))/2
      self.screen.move(self.cur_line,x)
      self.screen.addstr(l)
      if self.output or self.shelloutput:
        self.screen.move(self.cur_line,self.termwidth - self.indent - 1)
        self.screen.addstr(" |")
      self.cur_line += 1

  def do_right(self,text):
    width = self.termwidth - 2*self.indent
    if self.output or self.shelloutput:
      width -= 2
    lines = self.split_lines(text,width)
    for l in lines:
      self.screen.move(self.cur_line,self.indent)
      if self.output or self.shelloutput:
        self.screen.addstr("| ")
      x = (self.termwidth - len(l) - 4)
      self.screen.move(self.cur_line,x)
      self.screen.addstr(l)
      if self.output or self.shelloutput:
        self.screen.addstr(" |")
      self.cur_line += 1

  def show_help_page(self):
    help_text = [ "tpp help",
                  "",
                  "space bar ............................... display next entry within page",
                  "space bar, cursor-down, cursor-right .... display next page",
                  "b, cursor-up, cursor-left ............... display previous page",
                  "q, Q .................................... quit tpp",
                  "j, J .................................... jump directly to page",
                  "l, L .................................... reload current file",
                  "s, S .................................... jump to the first page",
                  "e, E .................................... jump to the last page",
                  "c, C .................................... start command line",
                  "?, h .................................... this help screen" ]
    self.screen.clear()
    y = self.voffset
    for line in help_text:
      self.screen.move(y,self.indent)
      self.screen.addstr(line)
      y += 1
    self.screen.move(self.termheight - 2, self.indent)
    self.screen.addstr("Press any key to return to slide")
    self.screen.refresh()

  def do_exec(self, cmdline):
    rc = Kernel.system(cmdline)
    if not rc:
      pass
      # self.todo: add error message

  def do_wait(self):
    # self.screen.addstr("In do wait")
    # self.screen.getch()
    pass

  def do_beginoutput(self):
    # self.screen.move(self.cur_line,self.indent)
    self.screen.addstr(self.cur_line,self.indent,".")
    for i in range((self.termwidth - self.indent*2 - 2 + 1)):
      self.screen.addstr("-")
    self.screen.addstr(".")
    self.output = True
    self.cur_line += 1

  def do_beginshelloutput(self):
    self.screen.addstr(self.cur_line,self.indent,".")
    for  i in range((self.termwidth - self.indent*2 - 2 + 1)):
       self.screen.addstr("-")
    # pdb.set_trace()
    self.screen.addstr(".")
    self.shelloutput = True
    self.cur_line += 1

  def do_endoutput(self):
    if self.output:
      self.screen.move(self.cur_line,self.indent)
      self.screen.addstr("`")
      for i in range(self.termwidth - self.indent*2 - 2 + 1):
         self.screen.addstr("-")
      self.screen.addstr("'")
      self.output = False
      self.cur_line += 1

  def do_title(self,title):
    self.do_boldon()
    self.do_center(title)
    self.do_boldoff()
    self.do_center("")

  def do_footer(self,footer_txt):
    self.screen.move(self.termheight - 3, (self.termwidth - len(footer_txt))/2)
    self.screen.addstr(footer_txt)

  def do_header(self,header_txt):
    self.screen.move(self.termheight - self.termheight+1, (self.termwidth - len(header_txt))/2)
    self.screen.addstr(header_txt)

  def do_author(self, author):
    self.do_center(author)
    self.do_center("")

  def do_date(self,date):
    self.do_center(date)
    self.do_center("")

  def do_endshelloutput(self):
    if self.shelloutput:
      self.screen.move(self.cur_line,self.indent)
      self.screen.addstr("`")
      for i in range (self.termwidth - self.indent*2 - 2):
         self.screen.addstr("-")
      self.screen.addstr("'")
      self.shelloutput = False
      self.cur_line += 1

  def do_sleep(self,time2sleep):
    time.sleep(int(4))
    time.sleep( int(time2sleep) )

  def do_boldon(self):
    self.screen.attron(curses.A_BOLD)

  def do_boldoff(self):
    self.screen.attroff(curses.A_BOLD)

  def do_revon(self):
    self.screen.attron(curses.A_REVERSE)

  def do_revoff(self):
    self.screen.attroff(curses.A_REVERSE)

  def do_ulon(self):
    self.screen.attron(curses.A_UNDERLINE)

  def do_uloff(self):
    self.screen.attroff(curses.A_UNDERLINE)

  def do_beginslideleft(self):
    self.slideoutput = True
    self.slidedir = "left"

  def do_endslide(self):
    self.slideoutput = False

  def do_beginslideright(self):
    self.slideoutput = True
    self.slidedir = "right"

  def do_beginslidetop(self):
    self.slideoutput = True
    self.slidedir = "top"

  def do_beginslidebottom(self):
    self.slideoutput = True
    self.slidedir = "bottom"

  def do_sethugefont(self, params):
    self.figletfont = params

  def do_huge(self, figlet_text):
    output_width = self.termwidth - self.indent
    output_width -= 2
    if self.output or self.shelloutput:
       op = IO.popen("figlet -f #{self.figletfont} -w #{output_width} -k \"#{figlet_text}\"","r")
    for line in op.readlines:
      self.print_line(line)
    op.close

  def do_bgcolor(self, color):

    bgcolor = self.cm.get_color(color)
    # pdb.set_trace()
    curses.init_pair(1, curses.COLOR_WHITE, bgcolor)
    curses.init_pair(2, curses.COLOR_YELLOW, bgcolor)
    curses.init_pair(3, curses.COLOR_RED, bgcolor)
    curses.init_pair(4, curses.COLOR_GREEN, bgcolor)
    curses.init_pair(5, curses.COLOR_BLUE, bgcolor)
    curses.init_pair(6, curses.COLOR_CYAN, bgcolor)
    curses.init_pair(7, curses.COLOR_MAGENTA, bgcolor)
    curses.init_pair(8, curses.COLOR_BLACK, bgcolor)
    #self.screen.addstr("Vitt\n\r", curses.color_pair(1))
    #self.screen.addstr("Gult\n\r", curses.color_pair(2))
    #self.screen.addstr("Rott\n\r", curses.color_pair(3))
    #self.screen.addstr("Gront\n\r", curses.color_pair(4))
    #self.screen.addstr("Blatt\n\r", curses.color_pair(5))
    #self.screen.addstr("Cyan\n\r", curses.color_pair(6))
    #self.screen.addstr("Magenta\n\r", curses.color_pair(7))
    #self.screen.addstr("Black\n\r", curses.color_pair(8))
    # self.screen.bkgd(" ",curses.color_pair(3))


    #self.screen.getch()
    try: # check if thevariableis defined
        self.fgcolor
    except:
        self.screen.bkgd(" ",self.cm.get_color_pair("white"))
        #self.screen.addstr("No fgcolor defined\n\r", curses.color_pair(3))
        #self.screen.getch()
    else:
        #pdb.set_trace()
        self.screen.bkgd(" ",self.fgcolor)
        # self.screen.getch()

  def do_fgcolor(self,color):
    # pdb.set_trace()
    self.fgcolor = self.cm.get_color_pair(color)
    self.screen.bkgd(" ",self.fgcolor)

  def do_color(self, color):
    num = self.cm.get_color_pair(color)
    self.screen.attron(num)

  def type_line(self,l):
    for x in l:
      self.screen.addstr(x)
      self.screen.refresh()
      time_to_sleep = random.uniform(0.02,0.1)
      time.sleep(time_to_sleep)

  def slide_text(self,l):
    if l == "":
       return True

    if self.slidedir == "left":
      xcount = len(l)-1
      while xcount >= 0:
        self.screen.move(self.cur_line,self.indent)
        self.screen.addstr(l[xcount:len(l)])
        self.screen.refresh()
        time_to_sleep = float(1) / 20
        time.sleep(time_to_sleep)
        xcount -= 1
    elif self.slidedir == "right":
      for pos in range (self.termwidth - self.indent+1):
        self.screen.move(self.cur_line,self.termwidth - pos - 1)
        self.screen.clrtoeol()
        self.screen.addstr(l[0:pos+1])
        self.screen.refresh()
        time_to_sleep = float(1) / 20
        time.sleep(time_to_sleep)
    elif self.slidedir == "top":
      tmpfile = tempfile.TemporaryFile()
      self.screen.putwin(tmpfile)
      for i in range(1,self.cur_line+1):
        tmpfile.seek(0)
        self.screen = curses.getwin(tmpfile) # overwrite self.screen with saved screen
        self.screen.addstr(i, self.indent,l)
        self.screen.refresh()
        time.sleep(float(1) / 10)
    elif self.slidedir == "bottom":
      tmpfile = tempfile.TemporaryFile()
      self.screen.putwin(tmpfile)
      for i in range(self.termheight-1,self.cur_line -1,-1):
        tmpfile.seek(0)
        self.screen = curses.getwin(tmpfile) # overwrite self.screen with saved screen
        self.screen.addstr(i, self.indent,l)
        self.screen.move(i,self.indent)
        self.screen.addstr(l)
        self.screen.refresh()
        time.sleep(float(1) / 10)

  def print_line(self, line):
    width = self.termwidth - 2*self.indent
    if self.output or self.shelloutput:
      width -= 2
    lines = self.split_lines(line,width)
    for l in lines:
      self.screen.move(self.cur_line,self.indent)
      if (self.output or self.shelloutput) and not self.slideoutput:
        self.screen.addstr("| ")
      if self.shelloutput and (l.startswith("$") or l.startswith("%") or l.startswith("#")):  # allow sh and csh style prompts
        self.type_line(l)
      elif self.slideoutput:
        self.slide_text(l)
      else:
        self.screen.addstr(self.cur_line,self.indent+2,l)
      if (self.output or self.shelloutput) and not self.slideoutput:
        self.screen.addstr(self.cur_line,self.termwidth - self.indent - 1," |")
      self.cur_line += 1

  def close(self):
    # pdb.set_trace()
    curses.nocbreak()
    self.screen.keypad(False)
    curses.echo()
    curses.endwin()

  def read_newpage(self,pages,current_page):
    page = []
    self.screen.clear()
    col = 0
    line = 2
    for i in pages.each_index:
      self.screen.move(line,col*15 + 2)
      if current_page == i:
        self.screen.printw("%2d %s <=",i+1,pages[i].title[0:81])
      else:
        self.screen.printw("%2d %s",i+1,pages[i].title[0:81])
      line += 1
      if line >= self.termheight - 3:
        line = 2
        col += 1
    prompt = "jump to slide: "
    prompt_indent = 12
    self.screen.move(self.termheight - 2, self.indent + prompt_indent)
    self.screen.addstr(prompt)
    # self.screen.refresh();
    curses.echo
    self.screen.scanw("%d",page)
    curses.noecho
    self.screen.move(self.termheight - 2, self.indent + prompt_indent)
    for i in range(len(prompt) + len(page[0].to_s)+1):
       self.screen.addstr(" ")
    if page[0]:
      return page[0] - 1
    return -1 # invalid page

  def store_screen(self):
    self.screen.dupwin

  def getLastFile(self):
    return self.lastFileName

  def restore_screen(self,s):
    curses.overwrite(s,self.screen)

  def draw_slidenum(self, cur_page,max_pages,eop):
    self.screen.move(self.termheight - 2, self.indent)
    self.screen.attroff(curses.A_BOLD) # this is bad
    self.screen.addstr("[slide "+str(cur_page)+"/"+str(max_pages)+"]")
    if len(self.footer_txt) > 0:
      self.do_footer(self.footer_txt)
    if len(self.header_txt) > 0:
      self.do_header(self.header_txt)

    if eop:
      self.draw_eop_marker()

  def draw_eop_marker(self):
    self.screen.move(self.termheight - 2, self.indent - 1)
    self.screen.attron(curses.A_BOLD)
    self.screen.addstr("*")
    self.screen.attroff(curses.A_BOLD)


#viz = NcursesVisualizer()
#lines = viz.split_lines("Vargen ar nu alla har, har patrullerna sa kar, leder stottar skogens djur",20)

#viz.do_heading("Oh, I like it")
#viz.get_key()
#viz.draw_border()
#viz.get_key()
#viz.close()




