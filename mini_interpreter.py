def interpret_zgs(block):
    if '⟦' in block and '⟧' in block:
        content = block.split('⟦')[1].split('⟧')[0]
        pairs = content.split('⋄')
        return dict(pair.split(':') for pair in pairs)
    return {}