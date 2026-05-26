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

### Architecture

We have a "main.py" file which represent our current entry point. It loads the CommandHandler, which takes some init commands such as "generate_templates" (generating the CSV templates that will help populate our future DB) and so on.

It also loads its necessary components:
- `view`, which will load `Screen` objects. `Screens` represent a scene with its specific text (the text is hosted in view/utils, in json format). Text will be displayed differently depending on the `DISPLAY_TYPE` variable, thanks to being parsed with the help of view/utils/{DISPLAY_TYPE}.json if the display_type is in text form.
- `db`, which will handle db-related functionalities.
- `mechanics`, which will hold inner components such as the social system, perhaps time passing, etc.

### Working functionalities
- `python3 main.py generate_templates`: generate CSV templates to fill for imports.
- `python3 main.py import_csv {FILE_NAME}`: import any CSV placed inside `import_files` to save it into the database. This allow us to create characters, domains, places on the fly.

### Tests
Tests are more end-to-end than unitary.

Our test structure: one class per module. Classes may have as many methods as wished.

**Module naming:** test_my_module_name
**Inner class naming:** TestMyModuleName (= the module name, but pascal case).
**Methods naming**: test_describe_input_and_possibly_behaviour

```bash
python -m unittest tests # Check every tests imported in init
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```
OR
```bash
python main.py tests
python main.py module_name
python main.py module_name.function_name
```

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
~~- Determining starting player fields~~
- CSV to character, domain, place
- Creating a dialog name norm
- DB connection: starting create a player character
- DB connection: remember a player's latest screen (for text platforms)