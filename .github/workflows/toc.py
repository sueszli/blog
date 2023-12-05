import os

def is_markdown(path):
    # file is .md
    if os.path.isfile(path) and path.endswith('.md') and path.split('/')[-1] != 'README.md':
        return True
    
    # one of subdirectory is .md
    elif os.path.isdir(path):
        return any([is_markdown(os.path.join(path, node)) for node in os.listdir(path)])


def gen_toc(startdir, indent=0):
    toc = ''
    
    for node in os.listdir(startdir):
        path = os.path.join(startdir, node)

        if not is_markdown(path):
            continue

        if os.path.isfile(path):
            toc += '\t'*indent + f"- [{node.split('.')[0]}](<{path}>)\n"

        elif os.path.isdir(path):
            toc += '\t'*indent + '- ' + node + '\n'
            toc += gen_toc(path, indent + 1)
    
    return toc


if __name__ == '__main__':
    os.system('rm -rf README.md && touch README.md')
    
    toc = gen_toc('.')
    with open('README.md', 'w') as f:
        f.write('_last posts:_\n\n')
        f.write(toc)
        f.write('\n\n')
        f.write('---')
        f.write('\n\n')
        f.write('subscribe via the github watch list: https://github.com/sueszli/blog/subscription')