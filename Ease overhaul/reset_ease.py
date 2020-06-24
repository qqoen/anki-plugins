from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

from .config import *

def reset_ease():
    ease_factor2 = ease_factor / 10
    
    # reset ease
    mw.col.db.execute("update cards set factor = ?", ease_factor)

    showInfo("Ease has been reset to " + str(ease_factor2) + "%.")

# create a new menu item
action = QAction('Reset ease', mw)

# set it to call testFunction when it's clicked
action.triggered.connect(reset_ease)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
