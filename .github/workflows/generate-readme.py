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
            link = path.replace('.md', '')
            toc += '\t'*indent + f"- [{node.split('.')[0]}](<{link}>)\n"

        elif os.path.isdir(path):
            toc += '\t'*indent + '- ' + node + '\n'
            toc += gen_toc(path, indent + 1)
    
    return toc


def main():
    if os.path.isfile('README.md'):
        os.remove('README.md')
    
    toc = gen_toc('.')
    
    with open('README.md', 'w') as f:
        f.write('## sueszli\'s blog')
        f.write('\n\n')
        f.write('_file tree:_')
        f.write('\n\n')
        f.write(toc)
        f.write('\n\n')
        f.write('<br>')
        f.write('\n\n')
        f.write('subscribe via github: [https://github.com/sueszli/blog/subscription](https://github.com/sueszli/blog/subscription)')


if __name__ == '__main__':
    # main()
    print("generation of toc is currently disabled")
