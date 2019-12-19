import os
from enum import Enum
import inkex
from lxml import etree
from copy import deepcopy

from inkex.elements import load_svg, Group

class IMPORT_MODE(Enum):
    VISIBLE = 'visible'
    NOT_VISIBLE = 'not-visible'
    ALL = 'all'

class ImportLayers(inkex.EffectExtension):
    """Exports the visible layers as SVG file"""
    def __init__(self):
        super(ImportLayers, self).__init__()

    def add_arguments(self, pars):
        pars.add_argument(
            "-f",
            "--file_name",
            help="File to import",
        )
        pars.add_argument(
            "-m",
            "--mode",
            default="import.svg",
            help="Import mode",
        )
        pars.add_argument(
            "-x",
            "--prefix",
            default="",
            help="Imported Layers Prefix",
        )
        pars.add_argument(
            "-p",
            "--parent",
            default="",
            help="Parent Layer",
        )
        pars.add_argument(
            "-g",
            "--with_defs",
            default=True,
            help="With defs",
        )

    def effect(self):
        with open(self.options.file_name, 'rb') as fhl:
            data = fhl.read()
            extDocument = load_svg(data)
            layers = extDocument.findall(inkex.addNS('g', 'svg'))
            layers2add = []
            for layer in layers:
                if hasattr(layer, 'groupmode') and layer.groupmode == 'layer':
                    if self.options.mode == IMPORT_MODE.VISIBLE.value:
                        if (not hasattr(layer, 'style')) or layer.style != 'display:none':
                            layers2add.append(layer)
                    elif self.options.mode == IMPORT_MODE.NOT_VISIBLE.value:
                        if hasattr(layer, 'style') and layer.style == 'display:none':
                            layers2add.append(layer)
                    else: # all
                        layers2add.append(deepcopy(layer))

            root = self.document.getroot()

            if len(self.options.parent) > 0:
                g = Group.create(self.options.parent, True);
                root.append(g)
                g.set_random_id()
                root = g

            if self.options.with_defs == 'true':
                defs = extDocument.findall(inkex.addNS('defs', 'svg'))
                for d in defs:
                    root.append(deepcopy(d))
                    d.set_random_id()

            for layer in layers2add:
                layer.label = self.options.prefix + layer.label
                root.append(layer)
                layer.set_random_id()

        return self.document

if __name__ == '__main__':
    ImportLayers().run()
