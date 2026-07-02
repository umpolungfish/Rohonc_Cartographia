"""
Rohonc Cartographia — navigator bridge to the IG catalog.

Maps the Rohonc Codex's 448 pages through the IG crystal,
classifying each into one of four topological regimes.
"""

from __future__ import annotations
import sys
from pathlib import Path
from typing import Optional

_NAV_PATH = Path(__file__).parent.parent.parent / 'imscribing_grammar' / 'navigators'
if str(_NAV_PATH) not in sys.path:
    sys.path.insert(0, str(_NAV_PATH))

import cl8nk_navigator as _nav

_PRIM_KEYS = _nav.PRIMITIVE_KEYS

# Four topological regimes found in the Rohonc Codex
_REGIMES = {
    'liturgical': {
        'description': 'Liturgical identity-loop chains — repetitive prayer-like sequences',
        'Þ': '𐑰',  # containment / enclosure
        'Ř': '𐑩',  # supervenient coupling
        'ɢ': '𐑝',  # conjunctive composition
        'Ω': '𐑷',  # trivial winding (zero net flux)
    },
    'pictographic_narrative': {
        'description': 'Pictographic narrative networks — fork-fuse story structures',
        'Þ': '𐑡',  # branching network
        'Ř': '𐑑',  # categorical depth
        'ɢ': '𐑜',  # disjunctive composition
        'Ω': '𐑴',  # Z2 parity winding
    },
    'astronomical': {
        'description': 'Astronomical closed-loop circuits — calendrical cycles',
        'Þ': '𐑸',  # imscriptive closure
        'Ř': '𐑾',  # bidirectional
        'ɢ': '𐑵',  # broadcast composition
        'Ω': '𐑭',  # integer winding
    },
    'mixed': {
        'description': 'Mixed full-spectrum — multiple regimes interleaved',
        'Þ': '𐑶',  # box product
        'Ř': '𐑽',  # adjoint pair
        'ɢ': '𐑠',  # sequential composition
        'Ω': '𐑟',  # non-Abelian braiding
    },
}

_PAGE_RANGES = {
    'liturgical':             (1, 117),
    'pictographic_narrative': (118, 235),
    'astronomical':           (236, 387),
    'mixed':                  (388, 448),
}

def _tuple_from_entry(entry: dict) -> list[str]:
    t = entry.get('tuple') or entry.get('raw_tuple', {})
    if isinstance(t, dict):
        return [t.get(k, '—') for k in _PRIM_KEYS]
    if isinstance(t, (list, tuple)):
        return list(t)
    return []

def _tuple_dict(entry: dict) -> dict:
    t = entry.get('tuple') or {}
    if isinstance(t, dict):
        return t
    return {k: v for k, v in zip(_PRIM_KEYS, t)}

def _regime_from_page(page: int) -> str:
    """Determine the regime for a given page number based on canonical ranges."""
    for regime, (lo, hi) in _PAGE_RANGES.items():
        if lo <= page <= hi:
            return regime
    return 'mixed'

def lookup(page_num: int) -> dict:
    """
    Look up a Rohonc Codex page by number and return its regime classification.
    """
    _nav.load_catalog()
    regime = _regime_from_page(page_num)
    regime_data = _REGIMES[regime]

    catalog_name = f'rohonc_page_{page_num:04d}'
    entry = _nav.resolve_system(catalog_name)

    t = _tuple_from_entry(entry) if entry else []

    return {
        'page': page_num,
        'regime': regime,
        'regime_description': regime_data['description'],
        'bottleneck_primitives': {
            'Þ': regime_data['Þ'],
            'Ř': regime_data['Ř'],
            'ɢ': regime_data['ɢ'],
            'Ω': regime_data['Ω'],
        },
        'tuple': t,
        'tuple_dict': _tuple_dict(entry) if entry else {},
        'catalog_name': catalog_name,
    }

def list_pages(regime: Optional[str] = None) -> list[dict]:
    """List pages, optionally filtered by topological regime."""
    results = []
    for p in range(1, 449):
        pg = lookup(p)
        if regime is None or pg['regime'] == regime:
            results.append(pg)
    return results

def classify_regime(topo_signature: dict) -> dict:
    """
    Classify an arbitrary topological signature into one of the four regimes.
    topo_signature should contain T, R (mu/Gamma), and Omega primitives.
    """
    best_regime = None
    best_score = float('inf')

    for regime, rdata in _REGIMES.items():
        score = 0
        for prim in ('Þ', 'Ř', 'ɢ', 'Ω'):
            if prim in topo_signature and prim in rdata:
                if topo_signature[prim] == rdata[prim]:
                    score += 0
                else:
                    score += 1
        if score < best_score:
            best_score = score
            best_regime = regime

    return {
        'classification': best_regime,
        'confidence': 1.0 / (1.0 + best_score) if best_regime else 0.0,
        'description': _REGIMES[best_regime]['description'] if best_regime else 'unclassified',
    }
