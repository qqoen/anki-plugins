from anki.hooks import addHook
from aqt import mw

from .config import *

def easeAdjustFunc():        
    mw.reviewer.card.factor = ease_factor
    
addHook('showQuestion', easeAdjustFunc)
addHook('showAnswer', easeAdjustFunc)
