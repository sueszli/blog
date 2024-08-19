python's package management system is both a blessing and a curse. while initially appealing, especially to those coming from java or c++, its simplicity can lead to complications over time such as (1) breaking your systems python runtime by using `--break-system-packages`, (2) excessive disk space usage from multiple toolchains that you installed unisolated (3) an overwhelming number of environment tools when collaborating with other developers each with their own quirks.

here is my recommendation for the most simple and sane python workflow in any project:

1) install python:

- use `asdf` to install and switch between different language runtimes for each project and prevent breaking your operating system's python runtime.

2) install packages:

- use `python -m pip` to make sure you install packages into the correct runtime.
- use `venv` / `virtualenv` to isolate dependencies per project.
- use `pipreqs` / `pip freeze` to derive project dependencies.

3) generate lock files:

- use `pip-tools` to generate lock files.
- combine with `uv` for a speedup.
- do not just rely on `requirements.txt` files. they never capture transitive dependencies and version constraints.

4) deploy:

- use `docker` / `apptainer` / `conda` for deployment, based on your performance requirements.
- beware that a container without a lock file only ensures very limited reproducibility.

by following these practices, you can maintain a more organized and efficient python development environment.

---

further reading:

- [`pixi`](https://github.com/prefix-dev/pixi): an upcoming environment manager competing with `conda`
- overview of all tools mentioned: https://sinoroc.gitlab.io/kb/python/packaging_tools_comparisons.html
- overview of all tools mentioned: https://www.youtube.com/watch?v=qil43iqNdQA
