# Rohonc Cartographia

![language](https://img.shields.io/badge/language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![corpus](https://img.shields.io/badge/corpus-four%20topological%20regimes-8B6914?style=for-the-badge) ![tier](https://img.shields.io/badge/tier-O%E2%88%9E-8A2BE2?style=for-the-badge) ![μ∘δ](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4-id-00A86B?style=for-the-badge) ![licence](https://img.shields.io/badge/licence-LUNLICENSE-1A1A1A?style=for-the-badge)

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
