---
layout: post
title: "Argument Map: Manufactured Incompetence"
date: 2026-07-24
type: post
published: false
---

Core spine in **blue/purple**, side quests in **grey**, resolution in **green**. Dashed lines are contrasts, not support.

```mermaid
flowchart TD
    classDef core     fill:#1e40af,color:#fff,stroke:#1e3a8a,stroke-width:2px
    classDef claim    fill:#6d28d9,color:#fff,stroke:#5b21b6,stroke-width:2px
    classDef fix      fill:#065f46,color:#fff,stroke:#064e3b,stroke-width:2px
    classDef sq       fill:#6b7280,color:#fff,stroke:#4b5563,stroke-width:1px,font-size:12px
    classDef contrast fill:#92400e,color:#fff,stroke:#78350f,stroke-width:1px,font-size:12px

    %% ── CORE SPINE ──────────────────────────────────
    P1["Complex problems genuinely require\ndeep, sustained attention to engage well"]:::core
    P2["Senior roles exist to exercise\nthis kind of judgement"]:::core
    P3["The busyness regime consumes\nall attention available for judgement"]:::core
    IC["Senior people cannot engage\nwith complex ideas presented to them"]:::claim
    MC["They misattribute this to idea quality,\nnot their own depleted condition\n═══════════════════════\nManufactured Incompetence"]:::claim
    S1["Fix requires: skill to sort\nwhich decisions need deep attention"]:::fix
    S2["Fix requires: accurate information\nreaching whoever is sorting"]:::fix
    RES["AI offers the first chance at ethical scholē\n— freed capacity could go to actual judgement —\nbut only if we defend attention\nrather than fill the new hours"]:::fix

    P1 & P2 & P3 --> IC --> MC --> S1 & S2 --> RES

    %% ── WHY BUSYNESS HAS MORAL WEIGHT (→ P3) ───────
    subgraph SG_BUSY ["Why busyness has moral weight"]
        direction TB
        SQ_CM["'Accidental managers'\n82% receive no management training\n(CMI 2023)"]:::sq
        SQ_WB["Weber: Calvinist doctrine gave\nvisible labour its moral charge;\nthe theology left, the reflex stayed"]:::sq
        SQ_BZ["Bellezza et al.: busyness now\nsignals status (inverts Veblen's\nleisure class)"]:::sq
        SQ_EX["External imposition: calendar filled\nby others; quiet = 'spare capacity'\nin others' eyes"]:::sq
        SQ_NP["Newport: pseudo-productivity —\nvisible activity stands in for\nknowledge-work output"]:::sq
        SQ_CM ~~~ SQ_WB ~~~ SQ_BZ ~~~ SQ_EX ~~~ SQ_NP
    end
    SG_BUSY --> P3

    %% ── ATTENTION AS THE SCARCE RESOURCE (→ P3) ────
    subgraph SG_ATT ["Attention as scarce resource"]
        direction TB
        SQ_SI["Simon (1971): wealth of information\ncreates a poverty of attention"]:::sq
        SQ_AI["AI compresses production;\nremoves interstitial thinking time;\nattention becomes the bottleneck"]:::sq
        SQ_LR["Leroy: attention residue —\nfragmented days compound the\ncost of every context switch"]:::sq
        SQ_SI ~~~ SQ_AI ~~~ SQ_LR
    end
    SG_ATT --> P3

    %% ── CONTRAST: DIFFERENT FAILURE MODE (→ MC) ────
    SQ_PP["Peter Principle: different failure —\ngenuine inability, not prevented ability.\nFix is better promotion decisions.\nHere, better decisions wouldn't help."]:::contrast
    SQ_PP -.->|"contrast"| MC

    %% ── SORTING DECISIONS (→ S1) ────────────────────
    subgraph SG_SORT ["Sorting decisions"]
        direction TB
        SQ_BE["Bezos: one-way vs two-way doors\n(reversibility × stakes)\nMost decisions are two-way;\ntreating them as one-way is the drift"]:::sq
        SQ_CO["Collison: same sorting framework,\narrived at independently — suggests\nit's discovered by need, not theory"]:::sq
        SQ_BE ~~~ SQ_CO
    end
    SG_SORT --> S1

    %% ── INFORMATION FLOW (→ S2) ─────────────────────
    subgraph SG_INFO ["Information flow"]
        direction TB
        SQ_MC["McChrystal: hierarchies filter info\nas it rises — JSOC couldn't act fast\nbecause nobody lower had the whole picture"]:::sq
        SQ_FC["Fusion cells: co-location +\nshared information feed +\ndelegated authority to act"]:::sq
        SQ_MC --> SQ_FC
    end
    SG_INFO --> S2

    %% ── AUTOMATION AS DELEGATION (→ RES) ────────────
    subgraph SG_DEL ["Automation as delegation"]
        direction TB
        SQ_DP["Delegation = Programming (2015):\na function call indifferent to what\nsits on the other end"]:::sq
        SQ_AD["AI as delegation: pushes judgement\ndown the hierarchy, freeing\nsenior attention — in principle"]:::sq
        SQ_DA["Condition: needs real trust.\n'Directed outsourcing with retained\naccountability' just smears\nthe same attention wider"]:::sq
        SQ_DP --> SQ_AD --> SQ_DA
    end
    SG_DEL --> RES

    %% ── WHAT PROTECTED ATTENTION LOOKS LIKE (→ RES) ─
    subgraph SG_PROT ["What protected attention looks like"]
        direction TB
        SQ_GR["Graham: maker-mode needs\nunbroken stretches; a single\nmeeting splits the day in two"]:::sq
        SQ_SC["Aristotle: scholē — freedom from\nnecessity is the precondition\nof judgement (negotium = nec-otium);\nnote: built on unfree labour"]:::sq
        SQ_PI["Pieper: 'total work' corrodes\nthe very faculty that thought\ndepends on (acedia as hidden busyness)"]:::sq
        SQ_WL["Wallas / Poincaré:\nincubation is a legitimate stage\nof work, not a lapse from it"]:::sq
        SQ_LD["Maths & physics have a doctrine\nthat sanctions the sofa;\ndesign and architecture do not"]:::sq
        SQ_GR ~~~ SQ_SC ~~~ SQ_PI ~~~ SQ_WL ~~~ SQ_LD
    end
    SG_PROT --> RES

    %% ── WHY THE FAILURE IS COSTLY (→ MC) ────────────
    subgraph SG_COST ["Why the failure is costly"]
        direction TB
        SQ_BV["Bloom & Van Reenen:\nmanagement quality explains 20%+\nof productivity variance across firms"]:::sq
        SQ_LB["DeMarco / Leibenstein:\nslack is productive reserve, not waste;\nat full utilisation, responsiveness collapses"]:::sq
        SQ_AF["Architecture's fixed fee:\nquiet hours cost margin directly —\nthe instrument meant to free thinking\nmay tax it most efficiently"]:::sq
        SQ_BV ~~~ SQ_LB ~~~ SQ_AF
    end
    SG_COST --> MC
```

---

## Reading the map

**Core spine** (blue/purple → green): The argument runs in a straight chain — complex problems need attention; senior roles exist to provide it; busyness consumes it; therefore the judgement fails; the failure is misread as the idea's problem; fixing it requires two simultaneous conditions; AI offers a rare opening.

**Side quests** (grey): Each supports a specific node on the spine but doesn't change the logical chain if removed. They answer *why* busyness has its grip (Weber, Bellezza, CMI), *why* attention is the real scarcity (Simon, Leroy), *how* you would actually implement the two fixes (Bezos, McChrystal), and *what* protecting attention looks like in practice (Graham, Aristotle, Wallas).

**Contrast node** (brown, dashed): The Peter Principle is deliberately distinguished — it's a different diagnosis, included to sharpen rather than support the main claim.

---

## Which sections are side quests?

| Essay section | Role |
|---|---|
| *How it is built* (accidental managers) | Side quest → supports P3 (how busyness gets imposed) |
| *Why the anxiety comes out as busyness* (Weber, Bellezza, Newport) | Partly core (external imposition), partly side quest (genealogy/status) |
| *Which decisions are yours* (Bezos, Collison) | Core — direct support for S1 |
| *Getting the information to the decision* (McChrystal, fusion cells) | Core — direct support for S2 |
| *The maker who forgot they were a maker* (Graham, Leroy, alienation) | Side quest → supports RES |
| *What leisure was for* (Aristotle, Pieper, Wallas, architecture) | Side quest → supports RES; most tangential section |
| *What it costs, and to whom* (Bloom, DeMarco, Leibenstein, fixed fee) | Side quest → supports MC (stakes of the failure) |
