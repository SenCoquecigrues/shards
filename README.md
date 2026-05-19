# Shards (v.0.0.0)

1. [Introduction](#introduction)
2. [Systems](#systems)
   - [Social System](#social-system)
   - [Exploration System](#exploration-system)
   - [Item generation](#item-generation)
     -  [CSV templates](#csv-templates)
3. [Tasks](#tasks)
    -  [TODO]()
4. [Advanced Features](#advanced-features)

## Introduction
*Shards* is a complex project, and platform choice is still up in the air. Therefore, some of the most complex mechanics will be done as platform-agnostic as we can.
**Current goal**: MVP.

## Systems
### Social System
Moving parts:
- 26 Facets rated 1 to 5
- Different scores => chances for conflict (different words for conflict depending on temper/random? Revulse, sadden, offend?...)
- Every day, 5 random traits are tested
- When failure/success, either critical failure/success (= immediate change) or normal failure/success (changing mood? A gauge? Perhaps offer opportunities for player to mediate?)
- Conflicts/getting along allow players to gain a better insight into traits: high/low, then specific score
- The characters being of the same element allow you to gain insight twice as quickly (discover two traits instead of one?)
- Talking with them also helps (one conversation = one traits)
- Some traits influence failure or success (for instance, if aggressive or extroverted)

### Exploration System
- Differing level of rarity? Or rarity inside a place?
- Various type of events? Shards, items, stats increase? Send shards who like you in mission?

### Item generation
Use CSV with special categories, which is transformed into a json file sorted in various folders (characters, items, domains, dialogs, character dialogs)

#### CSV templates
Title will determine import type:
- char_
- item_
- dom_
- place_
- dial_
- char_dial

## Tasks
### TODO (goal: MVP without db)
~~- Create CSV for character, domain, place~~
- CSV to character, domain, place
- Creating a dialog name norm
- Determining starting player fields
- DB connection: starting create a player character