# choosing macos

here's a list of the things that bother me about other operating systems, so much so that i'm willing to pay the apple tax to use macos.

this is in no way a recommendation for you to switch to macos. please use whatever works best for your workflow. also check out wolfgang's video on [why he switched to macos (as a linux user)](https://www.youtube.com/watch?v=X0DIHlnD_S0) and james mickens' presention of [his life as a developer](https://youtu.be/7Nj9ZjwOdFQ?si=mhz86GWUVsvk6sPe&t=1009) as they cover a lot of the same points.

## downsides of linux

choosing linux for servers? absolutely! it's the go-to for reliability and performance. but when it comes to desktops / your daily driver, it's a bit different. many folks opt for linux because they love ricing their distro or they see it as a way to support open-source ideals. it can be fun and impactful, but let's face it, sometimes it's not the most practical choice for everyday use.

_my issues with linux:_

- lack of support for most proprietary software

     it isn't economically viable for companies to support linux as there are so many distros and so few users.

     emulators (ie. wine) break with microsoft word, zoom and even the chrome browser doesn't render the same as on windows or macos. of course there are plenty of open source alternatives but you don't always get to choose what software your team is using and it is a lot of work. you could argue that this isn't linux's fault but that of big tech. i think it's a valid point to make since it's a problem that you will have to deal with if you use linux.

- lack of support for most laptop hardware

     linux isn't meant for laptops but desktop PCs or servers.

     you have to buy dedicated hardware (like system76 laptops) for things to work right out the box or else you will have to spend hours searching and configuring drivers.

     no distro ever recognized any peripherals on my lenovo carbon x1 laptop: external microphone, dual display setup, usb dock, wireless mouse and keyboard, fingerprint sensor, etc.

     some were impossible to set up (like the fingerprint sensor) and others were just really annoying to set up (like the dual display setup).

     i also never got more than 3 hours of battery life on linux, even with tlp and powertop installed.

     closing the lid on my laptop would also cause the system to crash and i would have to force restart it.

     when these minor issues add up, it becomes really annoying to use linux as a daily driver.

- janky gui

     i almost never had good scaling options for displays. all distros show massive screen tears and visual glitches with gnome and kde.

     this becomes less of an issue as you learn to use the terminal more, and become less dependent on the gui but it's still annoying and definitely something that makes linux less accessible to new users.

## downsides of windows

> note: a great chunk of these problems can be mitigated by debloating windows using something like https://github.com/LeDragoX/Win-Debloat-Tools

_my issues with windows:_

- wsl2 (windows subsystem for linux) is very unstable

     see: https://www.reddit.com/r/bashonubuntuonwindows/comments/opujbm/does_wsl_give_windows_an_edge_over_mac/

     you will still need to "drop back to windows" for a lot of things → usb passthrough doesn’t work, it is significantly slower, breaks vscode whenever you log off, has a reduced set of valid bash commands, etc.

- forced advertisement and updates

     since win10 won’t be getting updates from 2025. you will be forced to upgrade to win11.

     this is terrible as in win11 you have ads both in your lock screen and start menu that you can't disable.

- multiple shells

     you might have cmd and powershell but none of them are as good as bash.

     it's just something different to be able to use classic unix commands to navigate your file system and manage your software.

- aweful software management

     - environment variables must be set through the gui.
     - the file system makes deleting "node_module" folders or uninstalling programs really difficult. programs are unintuively spread across multiple folders you have no overview of.
     - package managers like scoop, winget and chocolatey don't work well together and are not as good as brew or apt.
