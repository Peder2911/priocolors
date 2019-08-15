#!/usr/bin/python3

import os
import yaml
import sys

palettes = {}

# ================================================
colors_incl = input('Enter colors to include (comma-sep):\n>>> ').split(',')
palettes_excl = input('Enter palettes to exclude(comma-sep):\n>>> ').split(',')
outname = input('Enter dest. file (yaml):\n>>> ')

# ================================================

for fname in [f for f in os.listdir('raw') if '.yaml' in f]:
    name,_ = os.path.splitext(fname)
    if name not in palettes_excl:
        with open(os.path.join('raw',fname)) as f:
            palette = {name:yaml.load(f)}

        palettes.update(palette)
    else:
        print(f'Not doing {name}')

colors_out = {}
for name,palette in palettes.items():
    chosen = {key:item for key,item in palette.items() if key in colors_incl}
    chosen = {f'{name}_{key}':item for key,item in chosen.items()}
    colors_out.update(chosen)

with open(os.path.join('out',outname),'w') as f:
    for key,item in colors_out.items():
        f.write(f'{key}: \"{item}\"\n')


