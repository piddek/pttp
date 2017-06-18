
import datetime, curses

class TppVisualizer:

  def __init__(self):
    pass

  # Splits a line into several lines, where each of the result lines is at most
  # _width_ characters long, caring about word boundaries, and returns an array
  # of strings.
  def split_lines(self,text,width):
    lines = []
    if text == "":
		while len(text) > 0:
			i = width
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
			  x = text[:i-1]
			  # remove extracted line
			  text = text[i+1:-1]
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
      if line.startswith("--heading"):
        text = line.replace("--heading ","")
        do_heading(text)
      elif line.startswith("--withborder"):
        do_withborder
      elif line.startswith("--horline"):
        do_horline
      elif line.startswith("--color "):
        text = line.replace("--color ","")
        text = text.rstrip
        do_color(text)
      elif line.startswith("--center "):
        text = line.replace("--center ","")
        do_center(text)
      elif line.startswith("--right "):
        text = line.replace("--right ","")
        do_right(text)
      elif line.startswith("--exec "):
        cmdline = line.replace("--exec ","")
        do_exec(cmdline)
      elif line.startswith("---"):
        do_wait
        return true
      elif line.startswith("--beginoutput"):
        do_beginoutput
      elif line.startswith("--beginshelloutput"):
        do_beginshelloutput
      elif line.startswith("--endoutput"):
        do_endoutput
      elif line.startswith("--endshelloutput"):
        do_endshelloutput
      elif line.startswith("--sleep "):
        time2sleep = line.replace("--sleep ","")
        do_sleep(time2sleep)
      elif line.startswith("--boldon"):
        do_boldon
      elif line.startswith("--boldoff"):
        do_boldoff
      elif line.startswith("--revon"):
        do_revon
      elif line.startswith("--revoff"):
        do_revoff
      elif line.startswith("--ulon"):
        do_ulon
      elif line.startswith("--uloff"):
        do_uloff
      elif line.startswith("--beginslideleft"):
        do_beginslideleft
      elif line.startswith(("--endslideleft", "--endslideright", "--endslidetop", "--endslidebottom")):
        do_endslide
      elif line.startswith("--beginslideright"):
        do_beginslideright
      elif line.startswith("--beginslidetop"):
        do_beginslidetop
      elif line.startswith("--beginslidebottom"):
        do_beginslidebottom
      elif line.startswith("--sethugefont "):
        params = line.replace("--sethugefont ","")
        do_sethugefont(params.strip)
      elif line.startswith("--huge "):
        figlet_text = line.replace("--huge ","")
        do_huge(figlet_text)
      elif line.startswith("--footer "):
        self.footer_txt = line.replace("--footer ","")
        do_footer(self.footer_txt)
      elif line.startswith("--header "):
        self.header_txt = line.replace("--header ","")
        do_header(self.header_txt)
      elif line.startswith("--title "):
        title = line.replace("--title ","")
        do_title(title)
      elif line.startswith("--author "):
        author = line.replace("--author ","")
        do_author(author)
      elif line.startswith("--date "):
        date = line.replace("--date ","")
        if (date == "today"):
		  date = datetime.datetime.now().strftime("%b %d %Y") #now with default format
        elif date.startswith("today "):  # this is for now with custom date format
          date = datetime.datetime.now().strftime(date.replace("today ",""))
        do_date(date)
      elif line.startswith("--bgcolor "):
        color = line.replace("--bgcolor ","").rstrip
        do_bgcolor(color)
      elif line.startswith("--fgcolor "):
        color = line.replace("--fgcolor ","").rstrip
        do_fgcolor(color)
      elif line.startswith("--color "):
        color = line.replace("--color ","").rstrip
        do_color(color)
      elif line.startswith("--include-file "):
        self.lastFileName = line.replace("--include-file ","").rstrip
        do_beginoutput
        print_line(self.lastFileName)
        do_beginoutput
        f = open(self.lastFileName)
        for line in f:
          line.rstrip
          if line != "":
            print_line(line)
        do_endoutput
      else:
        print_line(line)
      return false

  def close(self):
    pass


# Implements an interactive visualizer which builds on top of curses.
class NcursesVisualizer(TppVisualizer):

  def __init__(self):
    self.figletfont = "standard"
    curses.initscr
    curses.curs_set(0)
    curses.cbreak # unbuffered input
    curses.noecho # turn off input echoing
    curses.stdscr.intrflush(false)
    curses.stdscr.keypad(true)
    self.screen = curses.stdscr
    self.lastFileName = nil
    setsizes
    curses.start_color()
    curses.use_default_colors()
    do_bgcolor("black")
    do_fgcolor("white")
    # self.fgcolor = ColorMap.get_color_pair("white")
    self.voffset = 5
    self.indent = 3
    self.cur_line = self.voffset
    self.output = self.shelloutput = false


  def get_key(self):
    ch = curses.getch
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
    self.screen.clear
    self.screen.refresh


  def setsizes(self):
    self.termwidth = curses.getmaxx(self.screen)
    self.termheight = curses.getmaxy(self.screen)

  def do_refresh(self):
    self.screen.refresh

  def do_withborder(self):
    self.withborder = true
    draw_border

  def draw_border(self):
    self.screen.move(0,0)
    self.screen.addstr(".")
    # (self.termwidth-2).times { self.screen.addstr("-") }; self.screen.addstr(".")
    self.screen.move(self.termheight-2,0)
    self.screen.addstr("`")
    # (self.termwidth-2).times { self.screen.addstr("-") }; self.screen.addstr("'")
    for y in range(1, self.termheight -2): #python does not include stop value    
      self.screen.move(y,0)
      self.screen.addstr("|")
    for y in range(1, self.termheight -2): #python does not include stop value    
      self.screen.move(y,self.termwidth-1)
      self.screen.addstr("|")

  def new_page(self):
    self.cur_line = self.voffset
    self.output = self.shelloutput = false
    setsizes
    self.screen.clear

  def do_heading(self, line):
    self.screen.attron(curses.A_BOLD)
    print_heading(line)
    self.screen.attroff(curses.A_BOLD)

  def do_horline(self):
    self.screen.attron(curses.A_BOLD)
    for x in range(1,self.termwidth + 1):
      self.screen.move(self.cur_line,x)
      self.screen.addstr("-")
    self.screen.attroff(curses.A_BOLD)

  def print_heading(self,text):
    width = self.termwidth - 2*self.indent
    lines = split_lines(text,width)
    for l in lines:
      self.screen.move(self.cur_line,self.indent)
      x = (self.termwidth - l.length)/2
      self.screen.move(self.cur_line,x)
      self.screen.addstr(l)
      self.cur_line += 1

  def do_center(self,text):
    width = self.termwidth - 2*self.indent
    if self.output or self.shelloutput:
      width -= 2
    lines = split_lines(text,width)
    for l in lines:
      self.screen.move(self.cur_line,self.indent)
      if self.output or self.shelloutput then
        self.screen.addstr("| ")
      x = (self.termwidth - l.length)/2
      self.screen.move(self.cur_line,x)
      self.screen.addstr(l)
      if self.output or self.shelloutput then
        self.screen.move(self.cur_line,self.termwidth - self.indent - 2)
        self.screen.addstr(" |")
      self.cur_line += 1

  def do_right(self,text):
    width = self.termwidth - 2*self.indent
    if self.output or self.shelloutput then
      width -= 2
    lines = split_lines(text,width)
    lines.each do |l|
      self.screen.move(self.cur_line,self.indent)
      if self.output or self.shelloutput then
        self.screen.addstr("| ")
      x = (self.termwidth - l.length - 5)
      self.screen.move(self.cur_line,x)
      self.screen.addstr(l)
      if self.output or self.shelloutput then
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
    self.screen.clear
    y = self.voffset
    help_text.each do |line|
      self.screen.move(y,self.indent)
      self.screen.addstr(line)
      y += 1
    self.screen.move(self.termheight - 2, self.indent)
    self.screen.addstr("Press any key to return to slide")
    self.screen.refresh

  def do_exec(self, cmdline):
    rc = Kernel.system(cmdline)
    if not rc then
      # self.todo: add error message

  def do_wait(self):
    pass

  def do_beginoutput(self):
    self.screen.move(self.cur_line,self.indent)
    self.screen.addstr(".")
    (self.termwidth - self.indent*2 - 2).times { self.screen.addstr("-") }
    self.screen.addstr(".")
    self.output = true
    self.cur_line += 1

  def do_beginshelloutput(self):
    self.screen.move(self.cur_line,self.indent)
    self.screen.addstr(".")
    (self.termwidth - self.indent*2 - 2).times { self.screen.addstr("-") }
    self.screen.addstr(".")
    self.shelloutput = true
    self.cur_line += 1

  def do_endoutput(self):
    if self.output then
      self.screen.move(self.cur_line,self.indent)
      self.screen.addstr("`")
      (self.termwidth - self.indent*2 - 2).times { self.screen.addstr("-") }
      self.screen.addstr("'")
      self.output = false
      self.cur_line += 1

  def do_title(self,title):
    do_boldon
    do_center(title)
    do_boldoff
    do_center("")

  def do_footer(self,footer_txt):
    self.screen.move(self.termheight - 3, (self.termwidth - footer_txt.length)/2)
    self.screen.addstr(footer_txt)

 def do_header(self,header_txt):
    self.screen.move(self.termheight - self.termheight+1, (self.termwidth - header_txt.length)/2)
    self.screen.addstr(header_txt)

  def do_author(self, author):
    do_center(author)
    do_center("")

  def do_date(self,date):
    do_center(date)
    do_center("")

  def do_endshelloutput(self):
    if self.shelloutput then
      self.screen.move(self.cur_line,self.indent)
      self.screen.addstr("`")
      (self.termwidth - self.indent*2 - 2).times { self.screen.addstr("-") }
      self.screen.addstr("'")
      self.shelloutput = false
      self.cur_line += 1

  def do_sleep(self,time2sleep):
    Kernel.sleep(time2sleep.to_i)

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
    self.slideoutput = true
    self.slidedir = "left"

  def do_endslide(self):
    self.slideoutput = false

  def do_beginslideright(self):
    self.slideoutput = true
    self.slidedir = "right"

  def do_beginslidetop(self):
    self.slideoutput = true
    self.slidedir = "top"

  def do_beginslidebottom(self):
    self.slideoutput = true
    self.slidedir = "bottom"

  def do_sethugefont(self, params):
    self.figletfont = params

  def do_huge(self, figlet_text):
    output_width = self.termwidth - self.indent
    output_width -= 2 if self.output or self.shelloutput
    op = IO.popen("figlet -f #{self.figletfont} -w #{output_width} -k \"#{figlet_text}\"","r")
    op.readlines.each do |line|
      print_line(line)
    op.close

  def do_bgcolor(self, color):
    bgcolor = ColorMap.get_color(color) or COLOR_BLACK
    curses.init_pair(1, COLOR_WHITE, bgcolor)
    curses.init_pair(2, COLOR_YELLOW, bgcolor)
    curses.init_pair(3, COLOR_RED, bgcolor)
    curses.init_pair(4, COLOR_GREEN, bgcolor)
    curses.init_pair(5, COLOR_BLUE, bgcolor)
    curses.init_pair(6, COLOR_CYAN, bgcolor)
    curses.init_pair(7, COLOR_MAGENTA, bgcolor)
    curses.init_pair(8, COLOR_BLACK, bgcolor)
    if self.fgcolor then
      curses.bkgd(curses.COLOR_PAIR(self.fgcolor))
    else
      curses.bkgd(curses.COLOR_PAIR(1))

  def do_fgcolor(self,color):
    self.fgcolor = ColorMap.get_color_pair(color)
    curses.attron(curses.COLOR_PAIR(self.fgcolor))

  def do_color(self, color):
    num = ColorMap.get_color_pair(color)
    curses.attron(curses.COLOR_PAIR(num))

  def type_line(self,l):
    l.each_byte do |x|
      self.screen.addstr(x.chr)
      self.screen.refresh()
      r = rand(20)
      time_to_sleep = (5 + r).to_f / 250;
      # puts "#{time_to_sleep} #{r}"
      Kernel.sleep(time_to_sleep)

  def slide_text(self,l):
    return if l == ""
    case self.slidedir
    when "left"
      xcount = l.length-1
      while xcount >= 0
        self.screen.move(self.cur_line,self.indent)
        self.screen.addstr(l[xcount..l.length-1])
        self.screen.refresh()
        time_to_sleep = 1.to_f / 20
        Kernel.sleep(time_to_sleep)
        xcount -= 1
    when "right"
      (self.termwidth - self.indent).times do |pos|
        self.screen.move(self.cur_line,self.termwidth - pos - 1)
        self.screen.clrtoeol()
        self.screen.addstr(l[0..pos])
        self.screen.refresh()
        time_to_sleep = 1.to_f / 20
        Kernel.sleep(time_to_sleep)
      end # do
    when "top"
      # ycount = self.cur_line
      new_scr = self.screen.dupwin
      1.upto(self.cur_line) do |i|
        curses.overwrite(new_scr,self.screen) # overwrite self.screen with new_scr
        self.screen.move(i,self.indent)
        self.screen.addstr(l)
        self.screen.refresh()
        Kernel.sleep(1.to_f / 10)
      end
    when "bottom"
      new_scr = self.screen.dupwin
      (self.termheight-1).downto(self.cur_line) do |i|
        curses.overwrite(new_scr,self.screen)
        self.screen.move(i,self.indent)
        self.screen.addstr(l)
        self.screen.refresh()
        Kernel.sleep(1.to_f / 10)
      end
    end
  end

  def print_line(self, line):
    width = self.termwidth - 2*self.indent
    if self.output or self.shelloutput then
      width -= 2
    lines = split_lines(line,width)
    lines.each do |l|
      self.screen.move(self.cur_line,self.indent)
      if (self.output or self.shelloutput) and ! self.slideoutput then
        self.screen.addstr("| ")
      end
      if self.shelloutput and (l =~ /^\$/ or l=~ /^%/ or l =~ /^#/) then # allow sh and csh style prompts
        type_line(l)
      elsif self.slideoutput then
        slide_text(l)
      else
        self.screen.addstr(l)
      end
      if (self.output or self.shelloutput) and ! self.slideoutput then
        self.screen.move(self.cur_line,self.termwidth - self.indent - 2)
        self.screen.addstr(" |")
      end
      self.cur_line += 1
    end
  end

  def close(self):
    curses.nocbreak
    curses.endwin

  def read_newpage(self,pages,current_page):
    page = []
    self.screen.clear()
    col = 0
    line = 2
    pages.each_index do |i|
      self.screen.move(line,col*15 + 2)
      if current_page == i then
        self.screen.printw("%2d %s <=",i+1,pages[i].title[0..80])
      else
        self.screen.printw("%2d %s",i+1,pages[i].title[0..80])
      end
      line += 1
      if line >= self.termheight - 3 then
        line = 2
        col += 1
      end
    end
    prompt = "jump to slide: "
    prompt_indent = 12
    self.screen.move(self.termheight - 2, self.indent + prompt_indent)
    self.screen.addstr(prompt)
    # self.screen.refresh();
    curses.echo
    self.screen.scanw("%d",page)
    curses.noecho
    self.screen.move(self.termheight - 2, self.indent + prompt_indent)
    (prompt.length + page[0].to_s.length).times { self.screen.addstr(" ") }
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
    self.screen.addstr("[slide #{cur_page}/#{max_pages}]")
    if len(self.footer_txt) > 0:
      do_footer(self.footer_txt)
    if len(self.header_txt) > 0:
      do_header(self.header_txt)

    if eop then
      draw_eop_marker

  def draw_eop_marker(self):
    self.screen.move(self.termheight - 2, self.indent - 1)
    self.screen.attron(A_BOLD)
    self.screen.addstr("*")
    self.screen.attroff(A_BOLD)


viz = cursesVisualizer()
print viz.split_lines("Vargen ar nu alla har, har patrullerna sa kar, leder stottar skogens djur",20)




