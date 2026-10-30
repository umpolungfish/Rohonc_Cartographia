# Rohonc Cartographia — Engine Specification

## 12 IG Primitives as Codicological Operations

| Primitive | Value | Codex Interpretation |
|-----------|-------|---------------------|
| Ð (Dimensionality) | 𐑨 (2d surface) | The codex is a 2d page surface — 448 folios |
| Þ (Topology) | 𐑶 (box product) | Pages × symbols × regimes — a 3-dimensional structure |
| Ř (Coupling) | 𐑽 (adjoint pair) | Text ↔ image — illustration has a one-way relationship to script |
| Φ (Parity) | 𐑹 (Frobenius-special) | Regime boundaries are exact — page 117 ≠ page 118 |
| ƒ (Fidelity) | 𐑱 (classical) | The text is classical — no quantum superposition of readings |
| Ç (Kinetics) | 𐑧 (slow) | The codex changes regime slowly — broad blocks of 100+ pages |
| Γ (Cardinality) | 𐑔 (mesoscale) | Moderate number of symbols, moderate number of regimes |
| ɢ (Composition) | 𐑠 (sequential) | Pages are bound in fixed order |
| ⊙ (Criticality) | ⊙ (self-modeling gate open) | Regime classification is self-reflective — the classifier can re-classify itself |
| Ħ (Chirality) | 𐑖 (two-step memory) | Page n remembers page n-1's regime — bigram transitions |
| Σ (Stoichiometry) | 𐑳 (many heterogeneous) | Many symbol types, many illustration types, four regimes |
| Ω (Winding) | 𐑭 (integer winding) | The codex's 448 pages form one complete topological circuit |

## 12 Symbol Families → IMASM Opcodes

| Symbol Type | Opcode | Operation |
|-------------|--------|----------|
| Cross/cruciform | VINIT | Open a liturgical sequence |
| Leaf/foliate | AFWD | Advance pictographic narrative |
| Bird | AREV | Return/reverse in astronomical circuit |
| Crown | FSPLIT | Split into parallel streams |
| Serpent | FFUSE | Fuse streams into mixed regime |
| Blessing hand | CLINK | Link to liturgical frame |
| Building | IFIX | Fix astronomical position |
| Animal | IMSCRIB | Inscribe narrative element |
| Geometric | EVALT | Evaluate calendrical cycle |
| Circle/rosette | EVALF | Evaluate astronomical completion |
| Wave/water | ENGAGR | Engage mixed regime |
| Grid/checker | — | Close/end regime |

## Bootstrap Core

```
IMSCRIB → AREV → FSPLIT → AFWD → FFUSE → CLINK → IFIX → IMSCRIB
```

## Section Topology

The codex follows a ⟨𐑑⟩ categorical chain with four topological blocks:

```
Liturgical [1–117] → Pictographic [118–235] → Astronomical [236–387] → Mixed [388–448]
```

Each block transition marks a structural phase transition where Þ, Ř, ɢ, and Ω change simultaneously.

## Transcription Format (RTFF)

```
<FOLIO> <REGIME> <SYMBOL_COUNT> <TEXT_DENSITY> <ILLUSTRATION_TYPE>
```

Example: `0042 liturgical 142 high crucifix`
