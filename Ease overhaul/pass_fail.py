# -*- coding: utf-8 -*-

from aqt.reviewer import Reviewer
from aqt import mw

from .config import *

remap = {2:  [None, 1, 2, 2, 2],    # - nil      Again   Good   Good    Good - def 2-buttons: 1 = Again, 2 = Good, 3 = None, 4=None
         3:  [None, 1, 2, 2, 2],    # nil        Again   Good   Good    Good - def 3-buttons: 1 = Again, 2 = Good, 3 = Easy, 4=None
         4:  [None, 1, 3, 3, 3]}    # 0=nil/none Again   Good   Good    Good - def 4-buttons: 1 = Again, 2 = Hard, 3 = Good, 4=Easy

BUTTON_LABEL = [
    '<b style="color:' + again_color + ';font-family:' + font_family + ';">' + again_label + '</b>',
    '<b style="color:' + good_color + ';font-family:' + font_family + ';">' + good_label + '</b>',
]

__oldFunc = Reviewer._answerCard

def new_answerButtonList(self):
    l = ((1, BUTTON_LABEL[0]),)

    cnt = self.mw.col.sched.answerButtons(self.card)
    
    if cnt == 2 or cnt == 3: # we want ease 2 = good if 2 or 3 buttons
	    return l + ((2, "<div class='btn-i-ease btn-i-good'>" + BUTTON_LABEL[1] + "</div>"),)
    elif cnt == 4: # b/c we want ease 3 = good in this version
        return l + ((3, "<div class='btn-i-ease btn-i-good'>" + BUTTON_LABEL[1] + "</div>"),)
        
def new_answerCard(self, ease):
    cnt = mw.col.sched.answerButtons(mw.reviewer.card)  # Get button count

    try:
        ease = remap[cnt][ease]
    except (KeyError, IndexError):
        pass

    __oldFunc(self, ease)

Reviewer._answerCard =  new_answerCard
Reviewer._answerButtonList = new_answerButtonList
