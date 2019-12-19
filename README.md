# Export Visible Layers Inkscape extension
========================================
Allows to import visible/invisible/all layers from SVG file into currently opened SVG file.

Works for 1.0beta2. Not checked with other versions.

Installation
============

On Mac OS X
-----------
Copy export_visible_layers.inx and export_visible_layers.py into
/Applications/Inkscape.app/Contents/Resources/share/inkscape/extensions
and restart Inkscape

The extension is available as menu Extensions/Import/Import Layers.

On Other OS
-----------
See platform specific instruction how to install an extension.


Usage
=====

Options allows:
- import only visible layers
- import only invisible layers
- import all layers
- prepend prefix to the imported layer labels
- put all imported layers as sublayers for layer with specific name
- add all 'defs' resources during import (e.g. gradients)
