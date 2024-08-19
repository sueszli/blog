python's package management system is both a blessing and a curse. while initially appealing, especially to those coming from java or c++, its simplicity can lead to complications over time such as (1) breaking your systems python runtime by using `--break-system-packages`, (2) excessive disk space usage from multiple toolchains that you installed unisolated (3) an overwhelming number of [enviornment tools](https://sinoroc.gitlab.io/kb/python/packaging_tools_comparisons.html) when collaborating with other developers each with their own quirks.

here is my recommendation for a simple and sane python workflow:

1) install python:

  - [`asdf`](https://asdf-vm.com/) lets you install and switch between different language runtimes for each project
  - you want to avoid any interference with your operating systems python runtime

2) install packages:

  - [`venv`](https://docs.python.org/3/library/venv.html) lets you isolate dependencies per project
  - if you need to install development tools outside your `venv` make sure to use `python -m pip` to ensure you're not using the system runtime
  
  - don't install packages outside your `venv` and if you do, use 
  - project isolation: utilize `venv` to isolate dependencies for each project
  - dependency management: employ `pip-tools` for locking dependencies and ensuring reproducibility (`pip
  - deployment: 
  
  use **docker** for deployment, not development [^1]
  
  - provides simplicity and declarative nature
  - ensures reproducibility when combined with the above steps
  - may complicate gpu development due to sandboxing, but the benefits outweigh this drawback
  
by following these practices, you can maintain a more organized and efficient python development environment.

[^1]: [`pixi`](https://github.com/prefix-dev/pixi) seems to be the most promising new alternative to conda as of august 2024
