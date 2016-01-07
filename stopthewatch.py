  # http://www.codeskulptor.org/#user40_VQNenhSrW8_1.py

  # template for "Stopwatch: The Game by 2ba"

import simplegui

# define global variables
interval = 100
t=0
minute= 0
seconds= 0
mseconds=0
count_stop = 0
counter_success =0
stop_boolean = True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global minute
    global seconds
    global mseconds
    minute = int(t/60000)
    seconds = (t- (minute*60000))/1000
    mseconds = ((t- (minute*60000))% 1000)/100
    minute_str = str(minute)
    mseconds_str= str(mseconds)     
    if seconds< 10:
        seconds_str = str(seconds)
        final_time = minute_str+":"+ "0" + seconds_str + "."+mseconds_str           
    elif seconds >= 10:
        seconds_str = str(seconds)
        final_time = minute_str+":"+ seconds_str + "."+mseconds_str             
    return final_time
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()   
    global stop_boolean
    stop_boolean = True


def Stop():
    global stop_boolean
    global count_stop
    global t
    global counter_success
    if t % 1000 == 0:
        counter_success = counter_success +1
    else:
        counter_success
    if stop_boolean == True:
        count_stop = count_stop +1
    timer.stop()
    stop_boolean = False


    
def Reset():
    timer.stop()
    global t
    t =0
    global counter_success
    global count_stop
    counter_success =0
    count_stop = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t + 100
# define draw handler
def draw(canvas):
    """Draw message."""
    canvas.draw_text(format(t), [114,100], 36, "Black")
    canvas.draw_text(str(counter_success) +"/"+ str(count_stop), [250,30],30, "Black")
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
# register event handlers

timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
frame.set_canvas_background('Orange')
frame.add_button("Start",Start, 200)
frame.add_button("Stop",Stop, 200)
frame.add_button("Reset",Reset, 200)
# start frame
frame.start()



# Please remember to review the grading rubric
