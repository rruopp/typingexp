#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.6),
    on Tue 10 Aug 2021 03:55:28 PM PDT
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.6'
expName = 'typingtask_V2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/rubi/Documents/psychopy/typing_task/typingtask_V2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "practice_intro"
practice_introClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text="During this task you will be typing strings of text displayed to you. Once the text appears, that is your cue to type the presented text as quickly and as accurately as possible.\n\nWhen you are done typing no need to press enter, the next trial will automatically begin. Backspacing will also have no effect, so if you make a mistake just keep typing. If you type a string correctly it will turn green. Otherwise the text will remain white. \n\nBetween trials you will see an image of hands on a keyboard. This is your cue to return your hands to the home position (index fingers on the F and J keys) between trials. \n\nLet's run through a practice round first.\nPress any key to continue!",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_1 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
hand_reset = visual.ImageStim(
    win=win,
    name='reset_image', 
    image='home_keyboard.png', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
sound_1A = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_1A')
sound_1A.setVolume(1)

# Initialize components for Routine "real_intro"
real_introClock = core.Clock()
startpoint = visual.TextStim(win=win, name='startpoint',
    text='Now you are ready to begin the task! \n\nPlace your hands in the ready position and hit any key to continue.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_2 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
hand_reset = visual.ImageStim(
    win=win,
    name='reset_image', 
    image='home_keyboard.png', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
sound_1A = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_1A')
sound_1A.setVolume(1)

# Initialize components for Routine "rest"
restClock = core.Clock()
break_time = visual.TextStim(win=win, name='break_time',
    text="You're halfway done! Time for a break.\n\nThe test will automatically resume in 5min, but if you want to start early, place your hands in the ready position and press 'Y' to continue. ",
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_3 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
hand_reset = visual.ImageStim(
    win=win,
    name='reset_image', 
    image='home_keyboard.png', mask=None,
    ori=0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
sound_1A = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_1A')
sound_1A.setVolume(1)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thank_you = visual.TextStim(win=win, name='thank_you',
    text="You're all done - thank you for participating in our study! ",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "practice_intro"-------
continueRoutine = True
# update component parameters for each repeat
start_1.keys = []
start_1.rt = []
_start_1_allKeys = []
# keep track of which components have finished
practice_introComponents = [instructions, start_1]
for thisComponent in practice_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_intro"-------
while continueRoutine:
    # get current time
    t = practice_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *start_1* updates
    waitOnFlip = False
    if start_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_1.frameNStart = frameN  # exact frame index
        start_1.tStart = t  # local t and not account for scr refresh
        start_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_1, 'tStartRefresh')  # time at next scr refresh
        start_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_1.status == STARTED and not waitOnFlip:
        theseKeys = start_1.getKeys(keyList=None, waitRelease=False)
        _start_1_allKeys.extend(theseKeys)
        if len(_start_1_allKeys):
            start_1.keys = _start_1_allKeys[-1].name  # just the last key pressed
            start_1.rt = _start_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_intro"-------
for thisComponent in practice_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# the Routine "practice_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stringbank_V2.xls', selection='1,2,3'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    text.setText(string)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    text.color = 'white'
    sound_1A.setSound('A', secs=0.1, hamming=True)
    sound_1A.setVolume(1, log=False)
    # keep track of which components have finished
    trialComponents = [text, key_resp, hand_reset, sound_1A]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'space', 'enter', 'backspace'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
                # was this correct?
                if corrAns is not None and ((''.join(key_resp.keys) == str(corrAns)) or (key_resp.keys == corrAns)):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # feedback for correct response
                if key_resp.corr == 1:
                    text.color='green'
                else:
                    text.color='white'
        
        # *hand_reset* updates
        if hand_reset.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            hand_reset.frameNStart = frameN  # exact frame index
            hand_reset.tStart = t  # local t and not account for scr refresh
            hand_reset.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hand_reset, 'tStartRefresh')  # time at next scr refresh
            hand_reset.setAutoDraw(True)
        if hand_reset.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hand_reset.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                hand_reset.tStop = t  # not accounting for scr refresh
                hand_reset.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hand_reset, 'tStopRefresh')  # time at next scr refresh
                hand_reset.setAutoDraw(False)
        # start/stop sound_1A
        if sound_1A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1A.frameNStart = frameN  # exact frame index
            sound_1A.tStart = t  # local t and not account for scr refresh
            sound_1A.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1A.play(when=win)  # sync with win flip
        if sound_1A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1A.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1A.tStop = t  # not accounting for scr refresh
                sound_1A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1A, 'tStopRefresh')  # time at next scr refresh
                sound_1A.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('text.started', text.tStartRefresh)
    practice_trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('key_resp.keys',key_resp.keys)
    practice_trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        practice_trials.addData('key_resp.rt', key_resp.rt)
    practice_trials.addData('key_resp.started', key_resp.tStartRefresh)
    practice_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    sound_1A.stop()  # ensure sound has stopped at end of routine
    practice_trials.addData('sound_1A.started', sound_1A.tStartRefresh)
    practice_trials.addData('sound_1A.stopped', sound_1A.tStopRefresh)
    
# completed 1 repeats of 'practice_trials'


# ------Prepare to start Routine "real_intro"-------
continueRoutine = True
# update component parameters for each repeat
start_2.keys = []
start_2.rt = []
_start_2_allKeys = []
# keep track of which components have finished
real_introComponents = [startpoint, start_2]
for thisComponent in real_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
real_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "real_intro"-------
while continueRoutine:
    # get current time
    t = real_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=real_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startpoint* updates
    if startpoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startpoint.frameNStart = frameN  # exact frame index
        startpoint.tStart = t  # local t and not account for scr refresh
        startpoint.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startpoint, 'tStartRefresh')  # time at next scr refresh
        startpoint.setAutoDraw(True)
    
    # *start_2* updates
    waitOnFlip = False
    if start_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in real_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "real_intro"-------
for thisComponent in real_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('startpoint.started', startpoint.tStartRefresh)
thisExp.addData('startpoint.stopped', startpoint.tStopRefresh)
# the Routine "real_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stringbank_V2.xls'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    text.setText(string)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    text.color = 'white'
    sound_1A.setSound('A', secs=0.1, hamming=True)
    sound_1A.setVolume(1, log=False)
    # keep track of which components have finished
    trialComponents = [text, key_resp, hand_reset, sound_1A]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'space', 'enter', 'backspace'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
               # was this correct?
                if corrAns is not None and ((''.join(key_resp.keys) == str(corrAns)) or (key_resp.keys == corrAns)):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # feedback for correct response
                if key_resp.corr == 1:
                    text.color='green'
                else:
                    text.color='white'
        
        # *hand_reset* updates
        if hand_reset.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            hand_reset.frameNStart = frameN  # exact frame index
            hand_reset.tStart = t  # local t and not account for scr refresh
            hand_reset.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hand_reset, 'tStartRefresh')  # time at next scr refresh
            hand_reset.setAutoDraw(True)
        if hand_reset.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hand_reset.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                hand_reset.tStop = t  # not accounting for scr refresh
                hand_reset.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hand_reset, 'tStopRefresh')  # time at next scr refresh
                hand_reset.setAutoDraw(False)
        # start/stop sound_1A
        if sound_1A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1A.frameNStart = frameN  # exact frame index
            sound_1A.tStart = t  # local t and not account for scr refresh
            sound_1A.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1A.play(when=win)  # sync with win flip
        if sound_1A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1A.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1A.tStop = t  # not accounting for scr refresh
                sound_1A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1A, 'tStopRefresh')  # time at next scr refresh
                sound_1A.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    sound_1A.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1A.started', sound_1A.tStartRefresh)
    trials.addData('sound_1A.stopped', sound_1A.tStopRefresh)
    
# completed 5 repeats of 'trials'


# ------Prepare to start Routine "rest"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
start_3.keys = []
start_3.rt = []
_start_3_allKeys = []
# keep track of which components have finished
restComponents = [break_time, start_3]
for thisComponent in restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=restClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break_time* updates
    if break_time.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_time.frameNStart = frameN  # exact frame index
        break_time.tStart = t  # local t and not account for scr refresh
        break_time.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_time, 'tStartRefresh')  # time at next scr refresh
        break_time.setAutoDraw(True)
    if break_time.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > break_time.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            break_time.tStop = t  # not accounting for scr refresh
            break_time.frameNStop = frameN  # exact frame index
            win.timeOnFlip(break_time, 'tStopRefresh')  # time at next scr refresh
            break_time.setAutoDraw(False)
    
    # *start_3* updates
    if start_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_3.frameNStart = frameN  # exact frame index
        start_3.tStart = t  # local t and not account for scr refresh
        start_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_3, 'tStartRefresh')  # time at next scr refresh
        start_3.status = STARTED
        # keyboard checking is just starting
        start_3.clock.reset()  # now t=0
    if start_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_3.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            start_3.tStop = t  # not accounting for scr refresh
            start_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_3, 'tStopRefresh')  # time at next scr refresh
            start_3.status = FINISHED
    if start_3.status == STARTED:
        theseKeys = start_3.getKeys(keyList=['y'], waitRelease=False)
        _start_3_allKeys.extend(theseKeys)
        if len(_start_3_allKeys):
            start_3.keys = _start_3_allKeys[-1].name  # just the last key pressed
            start_3.rt = _start_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('break_time.started', break_time.tStartRefresh)
thisExp.addData('break_time.stopped', break_time.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stringbank_V2.xls'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    text.setText(string)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    text.color = 'white'
    sound_1A.setSound('A', secs=0.1, hamming=True)
    sound_1A.setVolume(1, log=False)
    # keep track of which components have finished
    trialComponents = [text, key_resp, hand_reset, sound_1A]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'space', 'enter', 'backspace'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
                # was this correct?
                if corrAns is not None and ((''.join(key_resp.keys) == str(corrAns)) or (key_resp.keys == corrAns)):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # feedback for correct response
                if key_resp.corr == 1:
                    text.color='green'
                else:
                    text.color='white'
        
        # *hand_reset* updates
        if hand_reset.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            hand_reset.frameNStart = frameN  # exact frame index
            hand_reset.tStart = t  # local t and not account for scr refresh
            hand_reset.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hand_reset, 'tStartRefresh')  # time at next scr refresh
            hand_reset.setAutoDraw(True)
        if hand_reset.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hand_reset.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                hand_reset.tStop = t  # not accounting for scr refresh
                hand_reset.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hand_reset, 'tStopRefresh')  # time at next scr refresh
                hand_reset.setAutoDraw(False)
        # start/stop sound_1A
        if sound_1A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1A.frameNStart = frameN  # exact frame index
            sound_1A.tStart = t  # local t and not account for scr refresh
            sound_1A.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1A.play(when=win)  # sync with win flip
        if sound_1A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1A.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1A.tStop = t  # not accounting for scr refresh
                sound_1A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1A, 'tStopRefresh')  # time at next scr refresh
                sound_1A.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text.started', text.tStartRefresh)
    trials_2.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp.keys',key_resp.keys)
    trials_2.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials_2.addData('key_resp.rt', key_resp.rt)
    trials_2.addData('key_resp.started', key_resp.tStartRefresh)
    trials_2.addData('key_resp.stopped', key_resp.tStopRefresh)
    sound_1A.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('sound_1A.started', sound_1A.tStartRefresh)
    trials_2.addData('sound_1A.stopped', sound_1A.tStopRefresh)
    
# completed 5 repeats of 'trials_2'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thank_you]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        thank_you.setAutoDraw(True)
    if thank_you.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            thank_you.tStop = t  # not accounting for scr refresh
            thank_you.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thank_you, 'tStopRefresh')  # time at next scr refresh
            thank_you.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thank_you.started', thank_you.tStartRefresh)
thisExp.addData('thank_you.stopped', thank_you.tStopRefresh)

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
