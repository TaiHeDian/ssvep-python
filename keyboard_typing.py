import os

from numpy import pi, sin
from psychopy import core, data, gui, logging, prefs, visual
from psychopy.constants import FINISHED, NOT_STARTED, STARTED
from psychopy.hardware import keyboard

prefs.hardware['audioLib'] = 'ptb'

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'idk'  # from the Builder filename that created this script
expInfo = {'participant': '001'}  # 参与者信息设置为001
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'log/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

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
    text='SSVEP输入测试\n',
    font='Microsoft YaHei',
    pos=(0, 0), height=1.0, wrapWidth=8.0, ori=0.0, 
    color='white', colorSpace='rgb'
    )
instructions = visual.TextStim(win=win, name='instructions',
    text=(
       '测试说明\n\n'
       '1. 准星消失后, 请盯住目标字母\n\n'
       '2. 字母闪烁时，请尽量不要眨眼\n\n'
       '\n\n请按任意键继续...'
    ),
    font='Microsoft YaHei',
    units='cm', pos=(-1, -1), height=0.6, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb'
    )
start_2 = keyboard.Keyboard()

# Initialize components for Routine "start_3"
start_3Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='☩',
    font='Microsoft YaHei',
    pos=(0, 0), height=2.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb'
    )

# 设置输入框和键盘字符的位置
expClock = core.Clock()
textbox = visual.TextBox2(
     win, text=' >> ', font='Cascadia Mono',
     pos=(0, 11), letterHeight=0.75,
     size=(32, 1.5), borderWidth=1,
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
iA = visual.ImageStim(
    win=win,
    name='iA', 
    image='images/A.png', mask=None,
    ori=0.0, pos=(-14, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iB = visual.ImageStim(
    win=win,
    name='iB', 
    image='images/B.png', mask=None,
    ori=0.0, pos=(-10, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iC = visual.ImageStim(
    win=win,
    name='iC', 
    image='images/C.png', mask=None,
    ori=0.0, pos=(-6, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iD = visual.ImageStim(
    win=win,
    name='iD', 
    image='images/D.png', mask=None,
    ori=0.0, pos=(-2, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iE = visual.ImageStim(
    win=win,
    name='iE', 
    image='images/E.png', mask=None,
    ori=0.0, pos=(2, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iF = visual.ImageStim(
    win=win,
    name='iF', 
    image='images/F.png', mask=None,
    ori=0.0, pos=(6, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iG = visual.ImageStim(
    win=win,
    name='iG', 
    image='images/G.png', mask=None,
    ori=0.0, pos=(10, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iH = visual.ImageStim(
    win=win,
    name='iH', 
    image='images/H.png', mask=None,
    ori=0.0, pos=(14, 7), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iI = visual.ImageStim(
    win=win,
    name='iI', 
    image='images/I.png', mask=None,
    ori=0.0, pos=(-14, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iJ = visual.ImageStim(
    win=win,
    name='iJ', 
    image='images/J.png', mask=None,
    ori=0.0, pos=(-10, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iK = visual.ImageStim(
    win=win,
    name='iK', 
    image='images/K.png', mask=None,
    ori=0.0, pos=(-6, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iL = visual.ImageStim(
    win=win,
    name='iL',
    image='images/L.png', mask=None,
    ori=0.0, pos=(-2, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iM = visual.ImageStim(
    win=win,
    name='iM',
    image='images/M.png', mask=None,
    ori=0.0, pos=(2, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iN = visual.ImageStim(
    win=win,
    name='iN',
    image='images/N.png', mask=None,
    ori=0.0, pos=(6, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iO = visual.ImageStim(
    win=win,
    name='iO',
    image='images/O.png', mask=None,
    ori=0.0, pos=(10, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iP = visual.ImageStim(
    win=win,
    name='iP',
    image='images/P.png', mask=None,
    ori=0.0, pos=(14, 3), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iQ = visual.ImageStim(
    win=win,
    name='iQ',
    image='images/Q.png', mask=None,
    ori=0.0, pos=(-14, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iR = visual.ImageStim(
    win=win,
    name='iR',
    image='images/R.png', mask=None,
    ori=0.0, pos=(-10, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iS = visual.ImageStim(
    win=win,
    name='iS',
    image='images/S.png', mask=None,
    ori=0.0, pos=(-6, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iT = visual.ImageStim(
    win=win,
    name='iT',
    image='images/T.png', mask=None,
    ori=0.0, pos=(-2, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iU = visual.ImageStim(
    win=win,
    name='iU',
    image='images/U.png', mask=None,
    ori=0.0, pos=(2, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iV = visual.ImageStim(
    win=win,
    name='iV',
    image='images/V.png', mask=None,
    ori=0.0, pos=(6, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iW = visual.ImageStim(
    win=win,
    name='iW',
    image='images/W.png', mask=None,
    ori=0.0, pos=(10, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iX = visual.ImageStim(
    win=win,
    name='iX',
    image='images/X.png', mask=None,
    ori=0.0, pos=(14, -1), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iY = visual.ImageStim(
    win=win,
    name='iY',
    image='images/Y.png', mask=None,
    ori=0.0, pos=(-14, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
iZ = visual.ImageStim(
    win=win,
    name='iZ',
    image='images/Z.png', mask=None,
    ori=0.0, pos=(-10, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i0 = visual.ImageStim(
    win=win,
    name='i0',
    image='images/0.png', mask=None,
    ori=0.0, pos=(-6, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i1 = visual.ImageStim(
    win=win,
    name='i1',
    image='images/1.png', mask=None,
    ori=0.0, pos=(-2, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i2 = visual.ImageStim(
    win=win,
    name='i2',
    image='images/2.png', mask=None,
    ori=0.0, pos=(2, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i3 = visual.ImageStim(
    win=win,
    name='i3',
    image='images/3.png', mask=None,
    ori=0.0, pos=(6, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i4 = visual.ImageStim(
    win=win,
    name='i4',
    image='images/4.png', mask=None,
    ori=0.0, pos=(10, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i5 = visual.ImageStim(
    win=win,
    name='i5',
    image='images/5.png', mask=None,
    ori=0.0, pos=(14, -5), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i6 = visual.ImageStim(
    win=win,
    name='i6',
    image='images/6.png', mask=None,
    ori=0.0, pos=(-14, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i7 = visual.ImageStim(
    win=win,
    name='i7',
    image='images/7.png', mask=None,
    ori=0.0, pos=(-10, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i8 = visual.ImageStim(
    win=win,
    name='i8',
    image='images/8.png', mask=None,
    ori=0.0, pos=(-6, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
i9 = visual.ImageStim(
    win=win,
    name='i9',
    image='images/9.png', mask=None,
    ori=0.0, pos=(-2, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
ispace = visual.ImageStim(
    win=win,
    name='ispace',
    image='images/space.png', mask=None,
    ori=0.0, pos=(2, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
icomma = visual.ImageStim(
    win=win,
    name='icomma',
    image='images/comma.png', mask=None,
    ori=0.0, pos=(6, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
idot = visual.ImageStim(
    win=win,
    name='idot',
    image='images/dot.png', mask=None,
    ori=0.0, pos=(10, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )
ibackspace = visual.ImageStim(
    win=win,
    name='ibackspace',
    image='images/backspace.png', mask=None,
    ori=0.0, pos=(14, -9), size=(3, 3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False
    )

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
trials = data.TrialHandler(nReps=1, method='sequential', # 实验循环次数（指定为1）
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
    routineTimer.add(999)    # 一次实验循环持续时间

    # keep track of which components have finished
    expComponents = [
        textbox, iA, iB, iC, iD, iE, iF, iG, 
        iH, iI, iJ, iK, iL, iM, iN, iO, iP, iQ, 
        iR, iS, iT, iU, iV, iW, iX, iY, iZ, 
        i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, 
        ispace, icomma, idot, ibackspace
    ]

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
            textbox.setColor('black', colorSpace='rgb', log=False)
        
        # *iA* updates
        if iA.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iA.frameNStart = frameN  # exact frame index
            iA.tStart = t  # local t and not account for scr refresh
            iA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iA, 'tStartRefresh')  # time at next scr refresh
            iA.setAutoDraw(True)
        if iA.status == STARTED:
            iA.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*8*(frameN/60))), log=False)
            
        # *iB* updates
        if iB.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iB.frameNStart = frameN  # exact frame index
            iB.tStart = t  # local t and not account for scr refresh
            iB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iB, 'tStartRefresh')  # time at next scr refresh
            iB.setAutoDraw(True)
        if iB.status == STARTED:
            iB.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*9*(frameN/60) + 1.75*pi)), log=False)
            
        # *iC* updates
        if iC.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iC.frameNStart = frameN  # exact frame index
            iC.tStart = t  # local t and not account for scr refresh
            iC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iC, 'tStartRefresh')  # time at next scr refresh
            iC.setAutoDraw(True)
        if iC.status == STARTED:
            iC.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*10*(frameN/60) + 1.5*pi)), log=False)
        
        # *iD* updates
        if iD.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iD.frameNStart = frameN  # exact frame index
            iD.tStart = t  # local t and not account for scr refresh
            iD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iD, 'tStartRefresh')  # time at next scr refresh
            iD.setAutoDraw(True)
        if iD.status == STARTED:
            iD.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*11*(frameN/60) +  1.25*pi)), log=False)
            
        # *iE* updates
        if iE.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iE.frameNStart = frameN  # exact frame index
            iE.tStart = t  # local t and not account for scr refresh
            iE.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iE, 'tStartRefresh')  # time at next scr refresh
            iE.setAutoDraw(True)
        if iE.status == STARTED:
            iE.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*12*(frameN/60) + pi)), log=False)
            
        # *iF* updates
        if iF.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iF.frameNStart = frameN  # exact frame index
            iF.tStart = t  # local t and not account for scr refresh
            iF.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iF, 'tStartRefresh')  # time at next scr refresh
            iF.setAutoDraw(True)
        if iF.status == STARTED:
            iF.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*13*(frameN/60) + 0.75*pi)), log=False)
            
        # *iG* updates
        if iG.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iG.frameNStart = frameN  # exact frame index
            iG.tStart = t  # local t and not account for scr refresh
            iG.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iG, 'tStartRefresh')  # time at next scr refresh
            iG.setAutoDraw(True)
        if iG.status == STARTED:
            iG.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*14*(frameN/60) + 0.5*pi)), log=False)
            
        # *iH* updates
        if iH.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iH.frameNStart = frameN  # exact frame index
            iH.tStart = t  # local t and not account for scr refresh
            iH.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iH, 'tStartRefresh')  # time at next scr refresh
            iH.setAutoDraw(True)
        if iH.status == STARTED:
            iH.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*15*(frameN/60) + 0.25*pi)), log=False)
            
        # *iI* updates
        if iI.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iI.frameNStart = frameN  # exact frame index
            iI.tStart = t  # local t and not account for scr refresh
            iI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iI, 'tStartRefresh')  # time at next scr refresh
            iI.setAutoDraw(True)
        if iI.status == STARTED:
            iI.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*8.2*(frameN/60) + 0.35*pi)), log=False)
            
        # *iJ* updates
        if iJ.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iJ.frameNStart = frameN  # exact frame index
            iJ.tStart = t  # local t and not account for scr refresh
            iJ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iJ, 'tStartRefresh')  # time at next scr refresh
            iJ.setAutoDraw(True)
        if iJ.status == STARTED:
            iJ.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*9.2*(frameN/60) + 0.1*pi)), log=False)
            
        # *iK* updates
        if iK.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iK.frameNStart = frameN  # exact frame index
            iK.tStart = t  # local t and not account for scr refresh
            iK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iK, 'tStartRefresh')  # time at next scr refresh
            iK.setAutoDraw(True)
        if iK.status == STARTED:
            iK.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*10.2*(frameN/60) + 1.85*pi)), log=False)
            
        # *iL* updates
        if iL.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iL.frameNStart = frameN  # exact frame index
            iL.tStart = t  # local t and not account for scr refresh
            iL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iL, 'tStartRefresh')  # time at next scr refresh
            iL.setAutoDraw(True)
        if iL.status == STARTED:
            iL.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*11.2*(frameN/60) + 1.6*pi)), log=False)
            
        # *iM* updates
        if iM.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iM.frameNStart = frameN  # exact frame index
            iM.tStart = t  # local t and not account for scr refresh
            iM.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iM, 'tStartRefresh')  # time at next scr refresh
            iM.setAutoDraw(True)
        if iM.status == STARTED:
            iM.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*12.2*(frameN/60) + 1.35*pi)), log=False)
            
        # *iN* updates
        if iN.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iN.frameNStart = frameN  # exact frame index
            iN.tStart = t  # local t and not account for scr refresh
            iN.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iN, 'tStartRefresh')
            iN.setAutoDraw(True)
        if iN.status == STARTED:
            iN.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*13.2*(frameN/60) + 1.1*pi)), log=False)
            
        # *iO* updates
        if iO.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iO.frameNStart = frameN  # exact frame index
            iO.tStart = t  # local t and not account for scr refresh
            iO.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iO, 'tStartRefresh')
            iO.setAutoDraw(True)
        if iO.status == STARTED:
            iO.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*14.2*(frameN/60) + 0.85*pi)), log=False)
            
        # *iP* updates
        if iP.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iP.frameNStart = frameN  # exact frame index
            iP.tStart = t  # local t and not account for scr refresh
            iP.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iP, 'tStartRefresh')
            iP.setAutoDraw(True)
        if iP.status == STARTED:
            iP.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*15.2*(frameN/60) + 0.6*pi)), log=False)
            
        # *iQ* updates
        if iQ.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iQ.frameNStart = frameN  # exact frame index
            iQ.tStart = t  # local t and not account for scr refresh
            iQ.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iQ, 'tStartRefresh')
            iQ.setAutoDraw(True)
        if iQ.status == STARTED:
            iQ.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*8.4*(frameN/60) + 0.7*pi)), log=False)
            
        # *iR* updates
        if iR.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iR.frameNStart = frameN  # exact frame index
            iR.tStart = t  # local t and not account for scr refresh
            iR.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iR, 'tStartRefresh')
            iR.setAutoDraw(True)
        if iR.status == STARTED:
            iR.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*9.4*(frameN/60) + 0.45*pi)), log=False)
            
        # *iS* updates
        if iS.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iS.frameNStart = frameN  # exact frame index
            iS.tStart = t  # local t and not account for scr refresh
            iS.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iS, 'tStartRefresh')
            iS.setAutoDraw(True)
        if iS.status == STARTED:
            iS.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*10.4*(frameN/60) + 0.2*pi)), log=False)
            
        # *iT* updates
        if iT.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iT.frameNStart = frameN  # exact frame index
            iT.tStart = t  # local t and not account for scr refresh
            iT.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iT, 'tStartRefresh')
            iT.setAutoDraw(True)
        if iT.status == STARTED:
            iT.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*11.4*(frameN/60) + 1.95*pi)), log=False)
            
        # *iU* updates
        if iU.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iU.frameNStart = frameN  # exact frame index
            iU.tStart = t  # local t and not account for scr refresh
            iU.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iU, 'tStartRefresh')  # time at next scr refresh
            iU.setAutoDraw(True)
        if iU.status == STARTED:
            iU.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*12.4*(frameN/60) + 1.7*pi)), log=False)
            
        # *iV* updates
        if iV.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iV.frameNStart = frameN  # exact frame index
            iV.tStart = t  # local t and not account for scr refresh
            iV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iV, 'tStartRefresh')  # time at next scr refresh
            iV.setAutoDraw(True)
        if iV.status == STARTED:
            iV.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*13.4*(frameN/60) + 1.45*pi)), log=False)
            
        # *iW* updates
        if iW.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iW.frameNStart = frameN  # exact frame index
            iW.tStart = t  # local t and not account for scr refresh
            iW.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iW, 'tStartRefresh')  # time at next scr refresh
            iW.setAutoDraw(True)
        if iW.status == STARTED:
            iW.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*14.4*(frameN/60) + 1.2*pi)), log=False)
            
        # *iX* updates
        if iX.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iX.frameNStart = frameN  # exact frame index
            iX.tStart = t  # local t and not account for scr refresh
            iX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iX, 'tStartRefresh')  # time at next scr refresh
            iX.setAutoDraw(True)
        if iX.status == STARTED:
            iX.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*15.4*(frameN/60) + 0.95*pi)), log=False)
            
        # *iY* updates
        if iY.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iY.frameNStart = frameN  # exact frame index
            iY.tStart = t  # local t and not account for scr refresh
            iY.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iY, 'tStartRefresh')  # time at next scr refresh
            iY.setAutoDraw(True)
        if iY.status == STARTED:
            iY.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*8.6*(frameN/60) + 1.05*pi)), log=False)
            
        # *iZ* updates
        if iZ.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            iZ.frameNStart = frameN  # exact frame index
            iZ.tStart = t  # local t and not account for scr refresh
            iZ.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(iZ, 'tStartRefresh')
            iZ.setAutoDraw(True)
        if iZ.status == STARTED:
            iZ.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*9.6*(frameN/60) + 0.8*pi)), log=False)
            
        # *i0* updates
        if i0.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i0.frameNStart = frameN  # exact frame index
            i0.tStart = t  # local t and not account for scr refresh
            i0.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i0, 'tStartRefresh')
            i0.setAutoDraw(True)
        if i0.status == STARTED:
            i0.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*10.6*(frameN/60) + 0.55*pi)), log=False)
            
        # *i1* updates
        if i1.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i1.frameNStart = frameN  # exact frame index
            i1.tStart = t  # local t and not account for scr refresh
            i1.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i1, 'tStartRefresh')
            i1.setAutoDraw(True)
        if i1.status == STARTED:
            i1.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*11.6*(frameN/60) + 0.3*pi)), log=False)
            
        # *i2* updates
        if i2.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i2.frameNStart = frameN  # exact frame index
            i2.tStart = t  # local t and not account for scr refresh
            i2.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i2, 'tStartRefresh')
            i2.setAutoDraw(True)
        if i2.status == STARTED:
            i2.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*12.6*(frameN/60) + 0.05*pi)), log=False)
            
        # *i3* updates
        if i3.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i3.frameNStart = frameN  # exact frame index
            i3.tStart = t  # local t and not account for scr refresh
            i3.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i3, 'tStartRefresh')
            i3.setAutoDraw(True)
        if i3.status == STARTED:
            i3.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*13.6*(frameN/60) + 1.8*pi)), log=False)
            
        # *i4* updates
        if i4.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i4.frameNStart = frameN  # exact frame index
            i4.tStart = t  # local t and not account for scr refresh
            i4.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i4, 'tStartRefresh')
            i4.setAutoDraw(True)
        if i4.status == STARTED:
            i4.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*14.6*(frameN/60) + 1.55*pi)), log=False)
            
        # *i5* updates
        if i5.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i5.frameNStart = frameN  # exact frame index
            i5.tStart = t  # local t and not account for scr refresh
            i5.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i5, 'tStartRefresh')
            i5.setAutoDraw(True)
        if i5.status == STARTED:
            i5.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*15.6*(frameN/60) + 1.3*pi)), log=False)
            
        # *i6* updates
        if i6.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i6.frameNStart = frameN  # exact frame index
            i6.tStart = t  # local t and not account for scr refresh
            i6.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i6, 'tStartRefresh')
            i6.setAutoDraw(True)
        if i6.status == STARTED:
            i6.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*8.8*(frameN/60) + 1.4*pi)), log=False)
            
        # *i7* updates
        if i7.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i7.frameNStart = frameN  # exact frame index
            i7.tStart = t  # local t and not account for scr refresh
            i7.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i7, 'tStartRefresh')
            i7.setAutoDraw(True)
        if i7.status == STARTED:
            i7.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*9.8*(frameN/60) + 1.15*pi)), log=False)
            
        # *i8* updates
        if i8.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i8.frameNStart = frameN  # exact frame index
            i8.tStart = t  # local t and not account for scr refresh
            i8.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i8, 'tStartRefresh')
            i8.setAutoDraw(True)
        if i8.status == STARTED:
            i8.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*10.8*(frameN/60) + 0.9*pi)), log=False)
            
        # *i9* updates
        if i9.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            i9.frameNStart = frameN  # exact frame index
            i9.tStart = t  # local t and not account for scr refresh
            i9.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(i9, 'tStartRefresh')
            i9.setAutoDraw(True)
        if i9.status == STARTED:
            i9.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*11.8*(frameN/60) + 0.65*pi)), log=False)
            
        # *ispace* updates
        if ispace.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            ispace.frameNStart = frameN  # exact frame index
            ispace.tStart = t  # local t and not account for scr refresh
            ispace.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(ispace, 'tStartRefresh')
            ispace.setAutoDraw(True)
        if ispace.status == STARTED:
            ispace.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*12.8*(frameN/60) + 0.4*pi)), log=False)
            
        # *icomma* updates
        if icomma.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            icomma.frameNStart = frameN  # exact frame index
            icomma.tStart = t  # local t and not account for scr refresh
            icomma.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(icomma, 'tStartRefresh')
            icomma.setAutoDraw(True)
        if icomma.status == STARTED:
            icomma.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*13.8*(frameN/60) + 0.15*pi)), log=False)
            
        # *idot* updates
        if idot.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            idot.frameNStart = frameN  # exact frame index
            idot.tStart = t  # local t and not account for scr refresh
            idot.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(idot, 'tStartRefresh')
            idot.setAutoDraw(True)
        if idot.status == STARTED:
            idot.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*14.8*(frameN/60) + 1.9*pi)), log=False)
        
        # *ibackspace* updates
        if ibackspace.status == NOT_STARTED and tThisFlip >= -frameTolerance:
            # keep track of start time/frame for later
            ibackspace.frameNStart = frameN  # exact frame index
            ibackspace.tStart = t  # local t and not account for scr refresh
            ibackspace.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(ibackspace, 'tStartRefresh')
            ibackspace.setAutoDraw(True)
        if ibackspace.status == STARTED:
            ibackspace.setOpacity(1 if t < 2 else 0.5*(1+sin(2*pi*15.8*(frameN/60) + 1.65*pi)), log=False)

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
    trials.addData('iA.started', iA.tStartRefresh)
    trials.addData('iA.stopped', iA.tStopRefresh)
    trials.addData('iB.started', iB.tStartRefresh)
    trials.addData('iB.stopped', iB.tStopRefresh)
    trials.addData('iC.started', iC.tStartRefresh)
    trials.addData('iC.stopped', iC.tStopRefresh)    
    trials.addData('iD.started', iD.tStartRefresh)
    trials.addData('iD.stopped', iD.tStopRefresh)
    trials.addData('iE.started', iE.tStartRefresh)
    trials.addData('iE.stopped', iE.tStopRefresh)
    trials.addData('iF.started', iF.tStartRefresh)
    trials.addData('iF.stopped', iF.tStopRefresh)
    trials.addData('iG.started', iG.tStartRefresh)
    trials.addData('iG.stopped', iG.tStopRefresh)
    trials.addData('iH.started', iH.tStartRefresh)
    trials.addData('iH.stopped', iH.tStopRefresh)
    trials.addData('iI.started', iI.tStartRefresh)
    trials.addData('iI.stopped', iI.tStopRefresh)
    trials.addData('iJ.started', iJ.tStartRefresh)
    trials.addData('iJ.stopped', iJ.tStopRefresh)
    trials.addData('iK.started', iK.tStartRefresh)
    trials.addData('iK.stopped', iK.tStopRefresh)
    trials.addData('iL.started', iL.tStartRefresh)
    trials.addData('iL.stopped', iL.tStopRefresh)
    trials.addData('iM.started', iM.tStartRefresh)
    trials.addData('iM.stopped', iM.tStopRefresh)
    trials.addData('iN.started', iN.tStartRefresh)
    trials.addData('iN.stopped', iN.tStopRefresh)
    trials.addData('iO.started', iO.tStartRefresh)
    trials.addData('iO.stopped', iO.tStopRefresh)
    trials.addData('iP.started', iP.tStartRefresh)
    trials.addData('iP.stopped', iP.tStopRefresh)
    trials.addData('iQ.started', iQ.tStartRefresh)
    trials.addData('iQ.stopped', iQ.tStopRefresh)
    trials.addData('iR.started', iR.tStartRefresh)
    trials.addData('iR.stopped', iR.tStopRefresh)
    trials.addData('iS.started', iS.tStartRefresh)
    trials.addData('iS.stopped', iS.tStopRefresh)
    trials.addData('iT.started', iT.tStartRefresh)
    trials.addData('iT.stopped', iT.tStopRefresh)
    trials.addData('iU.started', iU.tStartRefresh)
    trials.addData('iU.stopped', iU.tStopRefresh)
    trials.addData('iV.started', iV.tStartRefresh)
    trials.addData('iV.stopped', iV.tStopRefresh)
    trials.addData('iW.started', iW.tStartRefresh)
    trials.addData('iW.stopped', iW.tStopRefresh)
    trials.addData('iX.started', iX.tStartRefresh)
    trials.addData('iX.stopped', iX.tStopRefresh)
    trials.addData('iY.started', iY.tStartRefresh)
    trials.addData('iY.stopped', iY.tStopRefresh)
    trials.addData('iZ.started', iZ.tStartRefresh)
    trials.addData('iZ.stopped', iZ.tStopRefresh)
    trials.addData('ispace.started', ispace.tStartRefresh)
    trials.addData('ispace.stopped', ispace.tStopRefresh)
    trials.addData('icomma.started', icomma.tStartRefresh)
    trials.addData('icomma.stopped', icomma.tStopRefresh)
    trials.addData('idot.started', idot.tStartRefresh)
    trials.addData('idot.stopped', idot.tStopRefresh)
    trials.addData('ibackspace.started', ibackspace.tStartRefresh)
    trials.addData('ibackspace.stopped', ibackspace.tStopRefresh)
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
