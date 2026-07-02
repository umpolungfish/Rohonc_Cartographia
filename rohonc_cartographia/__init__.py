from .navigator import lookup, list_pages, classify_regime
from . import navigator

import sys
from pathlib import Path
_ENGINE = Path(__file__).parent.parent.parent / 'lang' / 'rohonc-engine'
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))

from rohonc_engine.session import RohoncSession, SessionState

__version__ = '1.0.0'
__all__ = [
    'RohoncSession',
    'SessionState',
    'lookup',
    'list_pages',
    'classify_regime',
    'navigator',
]
