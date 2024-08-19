python's package management system is both a blessing and a curse. while initially appealing, especially to those coming from java or c++, its simplicity can lead to complications over time such as (1) breaking your systems python runtime by using `--break-system-packages`, (2) excessive disk space usage from multiple toolchains that you installed unisolated (3) an overwhelming number of [enviornment tools](https://sinoroc.gitlab.io/kb/python/packaging_tools_comparisons.html) when collaborating with other developers each with their own quirks.

here is my recommendation for a sane python workflow:

1) install python: `asdf`

  - `asdf` lets you install and switch between different language runtimes for each project
  - you want to avoid any interference with your operating systems python runtime
  - see: https://asdf-vm.com/

2) install packages: 

- project isolation: use `asdf` for managing python versions
- package installation: always use `python -m pip` to ensure you're not using the system runtime
- project isolation: utilize `venv` to isolate dependencies for each project
- dependency management: employ `pip-tools` for locking dependencies and ensuring reproducibility [^1]
- deployment: 

  use **docker** for deployment, not development
  - provides simplicity and declarative nature
  - ensures reproducibility when combined with the above steps
  - may complicate gpu development due to sandboxing, but the benefits outweigh this drawback
  
by following these practices, you can maintain a more organized and efficient python development environment.

[^1]: [`pixi`](https://github.com/prefix-dev/pixi) seems to be the most promising new alternative to conda as of august 2024
