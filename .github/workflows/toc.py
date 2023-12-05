import os
import time


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
            toc += '\t'*indent + f"- [{node.split('.')[0]}](<{path.replace('.md', '')}>)\n"

        elif os.path.isdir(path):
            toc += '\t'*indent + '- ' + node + '\n'
            toc += gen_toc(path, indent + 1)
    
    return toc


if __name__ == '__main__':
    print('generating toc...')
    
    toc = gen_toc('.')    
    
    with open('README.md', 'w') as f:
        f.write('## sueszli\'s blog')
        f.write('_posts:_')
        f.write('\n\n')
        f.write(toc)
        f.write('\n\n')
        f.write('subscribe via github: [https://github.com/sueszli/blog/subscription](https://github.com/sueszli/blog/subscription)')
