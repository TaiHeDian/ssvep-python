import os

from numpy import (pi, sin)
from psychopy import core, data, gui, logging, prefs, visual
from psychopy.constants import (FINISHED, NOT_STARTED, STARTED)
from psychopy.hardware import keyboard

prefs.hardware['audioLib'] = 'ptb'

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'idk'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if not dlg.OK:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Set up the Window
win = visual.Window(
    size=[1366, 768], fullscr=False, screen=1, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome_screen"
welcome_screenClock = core.Clock()
welcome = visual.TextStim(win=win, name='welcome',
    text='SSVEP 输入测试\n',
    font='SimHei',
    pos=(0, 0), height=1.0, wrapWidth=8.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)
instructions = visual.TextStim(win=win, name='instructions',
    text='Instructions\n\n1. After the crosshair, when the keypad is presented, stare at the intended button\n\n2. Try not to blink when the number is flashing\n\n3. When the flashing stops, the signals are decoded and the decoded button is actuated\n\n4. You may blink until the next crosshair.\n\nPlease press a button to continue',
    font='SimHei',
    units='cm', pos=(-1, -1), height=0.6, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0)
start_2 = keyboard.Keyboard()

# Initialize components for Routine "start_3"
start_3Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='SimHei',
    pos=(0, 0), height=2.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

# Initialize components for Routine "exp"
expClock = core.Clock()
textbox = visual.TextBox2(
     win, text='', font='SimHei',
     pos=(0, 10),     letterHeight=0.75,
     size=(8, 2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='top-center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)
i7 = visual.ImageStim(
    win=win,
    name='i7', 
    image='Images/7.png', mask=None,
    ori=0.0, pos=(-3, 7), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=256.0, interpolate=True, depth=-1.0)
i8 = visual.ImageStim(
    win=win,
    name='i8', 
    image='Images/8.png', mask=None,
    ori=0.0, pos=(0, 7), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
i9 = visual.ImageStim(
    win=win,
    name='i9', 
    image='Images/9.png', mask=None,
    ori=0.0, pos=(3, 7), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
i4 = visual.ImageStim(
    win=win,
    name='i4', 
    image='Images/4.png', mask=None,
    ori=0.0, pos=(-3, 4), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
i5 = visual.ImageStim(
    win=win,
    name='i5', 
    image='Images/5.png', mask=None,
    ori=0.0, pos=(0, 4), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
i6 = visual.ImageStim(
    win=win,
    name='i6', 
    image='Images/6.png', mask=None,
    ori=0.0, pos=(3, 4), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
i1 = visual.ImageStim(
    win=win,
    name='i1', 
    image='Images/1.png', mask=None,
    ori=0.0, pos=(-3, 1), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
i2 = visual.ImageStim(
    win=win,
    name='i2', 
    image='Images/2.png', mask=None,
    ori=0.0, pos=(0, 1), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
i3 = visual.ImageStim(
    win=win,
    name='i3', 
    image='Images/3.png', mask=None,
    ori=0.0, pos=(3, 1), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
idel = visual.ImageStim(
    win=win,
    name='idel', 
    image='Images/backspace.png', mask=None,
    ori=0.0, pos=(-3, -2), size=(2, 2),
    color=(1, 1, 1), colorSpace='rgb',
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0
)
i0 = visual.ImageStim(
    win=win,
    name='i0', 
    image='Images/0.png', mask=None,
    ori=0.0, pos=(0, -2), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
ienter = visual.ImageStim(
    win=win,
    name='ienter', 
    image='Images/space.png', mask=None,
    ori=0.0, pos=(3, -2), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
ia = visual.ImageStim(
    win=win,
    name='ia',
    image='Images/A.png', mask=None,
    ori=0.0, pos=(-6, 7), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
# TODO 添加其他字母的位置

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_screen"-------
continueRoutine = True
# update component parameters for each repeat
start_2.keys = []
start_2.rt = []
_start_2_allKeys = []
# keep track of which components have finished
welcome_screenComponents = [welcome, instructions, start_2]
for thisComponent in welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_screen"-------
while continueRoutine:
    # get current time
    t = welcome_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    if welcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            welcome.tStop = t  # not accounting for scr refresh
            welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome, 'tStopRefresh')  # time at next scr refresh
            welcome.setAutoDraw(False)
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *start_2* updates
    waitOnFlip = False
    if start_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        start_2.frameNStart = frameN  # exact frame index
        start_2.tStart = t  # local t and not account for scr refresh
        start_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_2, 'tStartRefresh')  # time at next scr refresh
        start_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_2.status == STARTED and not waitOnFlip:
        theseKeys = start_2.getKeys(keyList=None, waitRelease=False)
        _start_2_allKeys.extend(theseKeys)
        if len(_start_2_allKeys):
            start_2.keys = _start_2_allKeys[-1].name  # just the last key pressed
            start_2.rt = _start_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_screen"-------
for thisComponent in welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if start_2.keys in ['', [], None]:  # No response was made
    start_2.keys = None
thisExp.addData('start_2.keys',start_2.keys)
if start_2.keys is not None:  # we had a response
    thisExp.addData('start_2.rt', start_2.rt)
thisExp.addData('start_2.started', start_2.tStartRefresh)
thisExp.addData('start_2.stopped', start_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=50.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial is not None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial is not None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "start_3"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    start_3Components = [text]
    for thisComponent in start_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_3"-------
    for thisComponent in start_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "exp"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    textbox.reset()
    textbox.setText('>')
    # keep track of which components have finished
    expComponents = [textbox, i7, i8, i9, i4, i5, i6, i1, i2, i3, idel, i0, ienter, ia]
    # TODO 添加其他字母的实验
    for thisComponent in expComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    expClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "exp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = expClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=expClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox, 'tStopRefresh')  # time at next scr refresh
                textbox.setAutoDraw(False)
        if textbox.status == STARTED:  # only update if drawing
            textbox.setColor('black', colorSpace='rgb', log=False)
        
        # *i7* updates
        if i7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i7.frameNStart = frameN  # exact frame index
            i7.tStart = t  # local t and not account for scr refresh
            i7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i7, 'tStartRefresh')  # time at next scr refresh
            i7.setAutoDraw(True)
        if i7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i7.tStop = t  # not accounting for scr refresh
                i7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i7, 'tStopRefresh')  # time at next scr refresh
                i7.setAutoDraw(False)
        if i7.status == STARTED:  # only update if drawing
            i7.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*5*(frameN/60))), log=False)
        
        # *i8* updates
        if i8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i8.frameNStart = frameN  # exact frame index
            i8.tStart = t  # local t and not account for scr refresh
            i8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i8, 'tStartRefresh')  # time at next scr refresh
            i8.setAutoDraw(True)
        if i8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i8.tStop = t  # not accounting for scr refresh
                i8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i8, 'tStopRefresh')  # time at next scr refresh
                i8.setAutoDraw(False)
        if i8.status == STARTED:  # only update if drawing
            i8.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*5.25*(frameN/60))), log=False)
        
        # *i9* updates
        if i9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i9.frameNStart = frameN  # exact frame index
            i9.tStart = t  # local t and not account for scr refresh
            i9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i9, 'tStartRefresh')  # time at next scr refresh
            i9.setAutoDraw(True)
        if i9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i9.tStop = t  # not accounting for scr refresh
                i9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i9, 'tStopRefresh')  # time at next scr refresh
                i9.setAutoDraw(False)
        if i9.status == STARTED:  # only update if drawing
            i9.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*5.5*(frameN/60))), log=False)
        
        # *i4* updates
        if i4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i4.frameNStart = frameN  # exact frame index
            i4.tStart = t  # local t and not account for scr refresh
            i4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i4, 'tStartRefresh')  # time at next scr refresh
            i4.setAutoDraw(True)
        if i4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i4.tStop = t  # not accounting for scr refresh
                i4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i4, 'tStopRefresh')  # time at next scr refresh
                i4.setAutoDraw(False)
        if i4.status == STARTED:  # only update if drawing
            i4.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*5.75*(frameN/60))), log=False)
        
        # *i5* updates
        if i5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i5.frameNStart = frameN  # exact frame index
            i5.tStart = t  # local t and not account for scr refresh
            i5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i5, 'tStartRefresh')  # time at next scr refresh
            i5.setAutoDraw(True)
        if i5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i5.tStop = t  # not accounting for scr refresh
                i5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i5, 'tStopRefresh')  # time at next scr refresh
                i5.setAutoDraw(False)
        if i5.status == STARTED:  # only update if drawing
            i5.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*6*(frameN/60))), log=False)
        
        # *i6* updates
        if i6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i6.frameNStart = frameN  # exact frame index
            i6.tStart = t  # local t and not account for scr refresh
            i6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i6, 'tStartRefresh')  # time at next scr refresh
            i6.setAutoDraw(True)
        if i6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i6.tStop = t  # not accounting for scr refresh
                i6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i6, 'tStopRefresh')  # time at next scr refresh
                i6.setAutoDraw(False)
        if i6.status == STARTED:  # only update if drawing
            i6.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*6.25*(frameN/60))), log=False)
        
        # *i1* updates
        if i1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i1.frameNStart = frameN  # exact frame index
            i1.tStart = t  # local t and not account for scr refresh
            i1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i1, 'tStartRefresh')  # time at next scr refresh
            i1.setAutoDraw(True)
        if i1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i1.tStop = t  # not accounting for scr refresh
                i1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i1, 'tStopRefresh')  # time at next scr refresh
                i1.setAutoDraw(False)
        if i1.status == STARTED:  # only update if drawing
            i1.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*6.5*(frameN/60))), log=False)
        
        # *i2* updates
        if i2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i2.frameNStart = frameN  # exact frame index
            i2.tStart = t  # local t and not account for scr refresh
            i2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i2, 'tStartRefresh')  # time at next scr refresh
            i2.setAutoDraw(True)
        if i2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i2.tStop = t  # not accounting for scr refresh
                i2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i2, 'tStopRefresh')  # time at next scr refresh
                i2.setAutoDraw(False)
        if i2.status == STARTED:  # only update if drawing
            i2.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*6.75*(frameN/60))), log=False)
        
        # *i3* updates
        if i3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i3.frameNStart = frameN  # exact frame index
            i3.tStart = t  # local t and not account for scr refresh
            i3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i3, 'tStartRefresh')  # time at next scr refresh
            i3.setAutoDraw(True)
        if i3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i3.tStop = t  # not accounting for scr refresh
                i3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i3, 'tStopRefresh')  # time at next scr refresh
                i3.setAutoDraw(False)
        if i3.status == STARTED:  # only update if drawing
            i3.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*7*(frameN/60))), log=False)
        
        # *idel* updates
        if idel.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            idel.frameNStart = frameN  # exact frame index
            idel.tStart = t  # local t and not account for scr refresh
            idel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(idel, 'tStartRefresh')  # time at next scr refresh
            idel.setAutoDraw(True)
        if idel.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > idel.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                idel.tStop = t  # not accounting for scr refresh
                idel.frameNStop = frameN  # exact frame index
                win.timeOnFlip(idel, 'tStopRefresh')  # time at next scr refresh
                idel.setAutoDraw(False)
        if idel.status == STARTED:  # only update if drawing
            idel.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*7.25*(frameN/60))), log=False)
        
        # *i0* updates
        if i0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            i0.frameNStart = frameN  # exact frame index
            i0.tStart = t  # local t and not account for scr refresh
            i0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(i0, 'tStartRefresh')  # time at next scr refresh
            i0.setAutoDraw(True)
        if i0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > i0.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                i0.tStop = t  # not accounting for scr refresh
                i0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(i0, 'tStopRefresh')  # time at next scr refresh
                i0.setAutoDraw(False)
        if i0.status == STARTED:  # only update if drawing
            i0.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*7.5*(frameN/60))), log=False)
        
        # *ienter* updates
        if ienter.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ienter.frameNStart = frameN  # exact frame index
            ienter.tStart = t  # local t and not account for scr refresh
            ienter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ienter, 'tStartRefresh')  # time at next scr refresh
            ienter.setAutoDraw(True)
        if ienter.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ienter.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                ienter.tStop = t  # not accounting for scr refresh
                ienter.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ienter, 'tStopRefresh')  # time at next scr refresh
                ienter.setAutoDraw(False)
        if ienter.status == STARTED:  # only update if drawing
            ienter.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*7.75*(frameN/60))), log=False)

        # *ia* updates
        if ia.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ia.frameNStart = frameN  # exact frame index
            ia.tStart = t  # local t and not account for scr refresh
            ia.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ia, 'tStartRefresh')  # time at next scr refresh
            ia.setAutoDraw(True)
        if ia.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ia.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                ia.tStop = t  # not accounting for scr refresh
                ia.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ia, 'tStopRefresh')  # time at next scr refresh
                ia.setAutoDraw(False)
        if ia.status == STARTED:  # only update if drawing
            ia.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*8*(frameN/60))), log=False)

        # TODO 添加其他字母的闪烁频率

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "exp"-------
    for thisComponent in expComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textbox.text',textbox.text)
    trials.addData('textbox.started', textbox.tStartRefresh)
    trials.addData('textbox.stopped', textbox.tStopRefresh)
    trials.addData('i7.started', i7.tStartRefresh)
    trials.addData('i7.stopped', i7.tStopRefresh)
    trials.addData('i8.started', i8.tStartRefresh)
    trials.addData('i8.stopped', i8.tStopRefresh)
    trials.addData('i9.started', i9.tStartRefresh)
    trials.addData('i9.stopped', i9.tStopRefresh)
    trials.addData('i4.started', i4.tStartRefresh)
    trials.addData('i4.stopped', i4.tStopRefresh)
    trials.addData('i5.started', i5.tStartRefresh)
    trials.addData('i5.stopped', i5.tStopRefresh)
    trials.addData('i6.started', i6.tStartRefresh)
    trials.addData('i6.stopped', i6.tStopRefresh)
    trials.addData('i1.started', i1.tStartRefresh)
    trials.addData('i1.stopped', i1.tStopRefresh)
    trials.addData('i2.started', i2.tStartRefresh)
    trials.addData('i2.stopped', i2.tStopRefresh)
    trials.addData('i3.started', i3.tStartRefresh)
    trials.addData('i3.stopped', i3.tStopRefresh)
    trials.addData('idel.started', idel.tStartRefresh)
    trials.addData('idel.stopped', idel.tStopRefresh)
    trials.addData('i0.started', i0.tStartRefresh)
    trials.addData('i0.stopped', i0.tStopRefresh)
    trials.addData('ienter.started', ienter.tStartRefresh)
    trials.addData('ienter.stopped', ienter.tStopRefresh)
    trials.addData('ia.started', ia.tStartRefresh)
    trials.addData('ia.stopped', ia.tStopRefresh)
    # TODO 添加其他字母到实验
    thisExp.nextEntry()
    
# completed 50.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
