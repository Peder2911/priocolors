#!/usr/bin/python3

import os

# ================================================

for fname in [f for f in os.listdir('raw') if '.txt' in f]:
    name,_ = os.path.splitext(fname)
    print(f'Doing {name}')

    with open(os.path.join('raw',fname)) as f:
        colors = f.readlines()
    colors = [l.strip() for l in colors]

    lines = []

    colors = [*enumerate(colors)]

    for i,color in colors[:2]:
        lines.append(f'prio_{i}: \"{color}\"\n')

    for i,color in colors[2:4]:
        lines.append(f'main_{i-2}: \"{color}\"\n')

    for i,color in colors[4:]:
        lines.append(f'color_{i-4}: \"{color}\"\n')
        
    with open(os.path.join('raw',f'{name}.yaml'),'w') as f:
        f.writelines(lines)

