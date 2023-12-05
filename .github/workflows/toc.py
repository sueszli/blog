import os
import glob

os.system('rm -rf README.md')

readme_contents = "# Table of Contents\n\n"

for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.md') and not filename == 'README.md':
            path = os.path.join(foldername, filename)
            path = os.path.normpath(path)
            link = path.replace('\\', '/')
            name = os.path.splitext(filename)[0]
            readme_contents += f"- [{name}]({link})\n"

with open('README.md', 'w') as f:
    f.write(readme_contents)
