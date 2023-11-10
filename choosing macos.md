i was inspired to make this post because of wolfgang's video on [why he switched to macos (as a linux user)](https://www.youtube.com/watch?v=X0DIHlnD_S0).

i've used windows, linux and macos as my daily driver for years and thought i might share my thoughts on the topic.

<br><br>

# windows

windows is the best option best option for less tech savvy users that need custom hardware for high-performance computing (gaming, video editing, 3d modeling etc.).

_good:_

- works great with custom hardware with little to no configuration

_bad:_

- has wsl2 (windows subsystem for linux) but it kind of sucks

  see: https://www.reddit.com/r/bashonubuntuonwindows/comments/opujbm/does_wsl_give_windows_an_edge_over_mac/

  you will still need to "drop back to windows" for a lot of things → usb passthrough doesn’t work, it is significantly slower, breaks vscode whenever you log off, has a reduced set of valid bash commands etc.

- lots of annoying advertisement

  win11 has ads and win10 won’t be getting updates from 2025.

- terrible developer experience

  bad default system terminal: powershell and cmd.

  environment variables must be set through the gui.

  bad file system which makes it difficult to uninstall apps.

  package managers like scoop, winget and chocolatey aren’t as good as brew from macos.

<br><br>

# linux

linux is excellent for servers, power users, and enthusiasts. however, it may not be the best choice for those who just want to get work done without much setup.

while learning unix is valuable, i don't recommend using linux as your daily driver unless you're a fan who enjoys spending a lot of time on maintenance. using linux means dedicating a significant amount of time to system upkeep, leaving less time for actual software development.

_good:_

- extreme customizability, true freedom and privacy

_bad:_

- breaks with most peripherals - you have to buy dedicated hardware/laptops (like system76 laptops) for things to work right out the box

  your hardware must be compatible with linux, to begin with - else you might struggle to find drivers.

  no distro ever recognized any peripherals on my lenovo carbon x1 laptop: external microphone, dual display setup, usb dock, wireless mouse and keyboard, fingerprint sensor, etc.

- access to fewer mainstream apps

  emulators break with microsoft word, zoom etc.

- really slow and janky gui

  almost never had good scaling options for displays.

  on all distros show massive screen tears with gnome. lots of visual glitches.

- working in the terminal is fast but booting up and shutting down is annoyingly slow.

when choosing a distro, you should always start off with ubuntu or mint as they have the largest community to help you out. i personally always recommend: ubuntu, zorin os and popos!.

<br><br>

# macos

have the best laptops in the market. they are the best option for developers who want to get work done without much setup.

good:

- unix, great developer experience with many similarities to linux

- a single package manager that is accepted by the entire community: brew

- enables you to test your software on safari and ios (through xcode)

- super pretty

- most performant and quiet laptops in the market

bad:

- based on \*bsd and not gnu/linux

  has weird shortcuts and commands ie. `xdg-open` vs. `open`
