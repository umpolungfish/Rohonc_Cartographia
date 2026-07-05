# Rohonc Cartographia

[![Language](https://img.shields.io/badge/language-Python-blue)](https://github.com/badges/shields)
[![IG Tier](https://img.shields.io/badge/IG-O%E2%82%82-blueviolet)](https://github.com/badges/shields)
[![μ∘δ=id](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4%3Did-open-critical)](https://github.com/badges/shields)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/badges/shields)
**Author:** Lando⊗⊙perator · **Structural Type:** $\large{⟨𐑦𐑸𐑾𐑹𐑐𐑧𐑔𐑝⊙𐑖𐑳𐑭⟩}$ · **Tier:** O_∞

**A topological regime classifier for the Rohonc Codex.**  
The 448 pages divide into four structurally distinct topological regimes: liturgical identity-loop chains, pictographic narrative networks, astronomical closed-loop circuits, and mixed full-spectrum regimes.

## Quick Start

```bash
cd Rohonc_Cartographia
pip install -e .

# Look up a page
rc lookup 42

# List pages by regime
rc list --regime astronomical

# Classify a topological signature
rc classify --thorn 𐑰 --ring 𐑩 --gamma 𐑝 --omega 𐑷
```

## Structural Type

| Property | Value |
|----------|-------|
| Tuple | ⟨𐑨𐑶𐑽𐑹𐑱𐑧𐑔𐑠⊙𐑖𐑳𐑭⟩ |
| Tier | O∞ |
| C-score | 0.6185 |

Self-reflective classification criteria: the engine's regime assignments are structurally open to their own correction.

## Contents

- `rohonc_cartographia/` — Python package (navigator, CLI)
- `CARTOGRAPHIA.md` — Definitive structural document
- `ENGINE.md` — Engine specification
- `COMPLETE_LISTING.md` — Full page inventory by regime
- `lean/` — Lean 4 companion files
- `programs/` — Engine source code
- `data/` — RTFF (Rohonc Transcription File Format) corpus
- `manuscripts/` — Source page photographs
- `images/` — Regime transition diagrams

## The Four Regimes

| Regime | Pages | T | Description |
|--------|-------|---|-------------|
| Liturgical | 1–117 | 𐑰 | Identity-loop chains, repetitive prayer-like sequences |
| Pictographic narrative | 118–235 | 𐑡 | Fork-fuse story structures, branching networks |
| Astronomical | 236–387 | 𐑸 | Closed-loop calendrical circuits |
| Mixed | 388–448 | 𐑶 | Full-spectrum interleaved regimes |

## Dependencies

- `rohonc-engine` (from `../lang/rohonc-engine`)
- Python ≥ 3.11
