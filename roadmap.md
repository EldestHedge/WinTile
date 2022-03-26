## Key

✅ - completed

⚠️ - some variations not supported

🏃‍ - work in progress

⬇️ - in low priority

❌ - rejected

## Roadmap

#### CLI Config

| Status | Feature          | Description                                                                      |
|--------|------------------|-----------------------------------------------------------|
|        | Arguments           | Take user arguments relating to config via CLI            |
|        | Config File           | Create ``program.ini`` config file in x86 Program Files |
|⬇️      | Start on Startup   | Start tiling windows once machine is turned on         |
|⬇️      | Affect minimized windows | add argument whether or not minimized windows should be tiled or stay minimized and not tiled|

#### Window Tiling

| Status | Feature          | Description                                                                      |
|--------|---------------------|-----------------------------------------------------------|
|        | Process Separation   | Separate event loop into separate processes i.e. global hotkeys & resizer/window listener|
|        | Global Hotkeys         |Generate default and allow customization of global hotkeys to resize, quit, change position, etc. of windows |
|🏃      | Complete Refactor helper_funcs.py| It is nearly impossible to fix anything in this file as there was no initial plan on structure|