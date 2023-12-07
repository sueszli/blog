# a love letter to macos

this is just a personal story on how i surprisingly came to love macos and in no way a recommendation for you to switch to macos. please use whatever works best for you and ✨brings you the most joy✨.

i was inspired to make this post because of wolfgang's video on [why he switched to macos (as a linux user)](https://www.youtube.com/watch?v=X0DIHlnD_S0).

## backstory

i've now used linux, windows and macos as my daily driver for years and thought i might share my thoughts on the topic.

i initially started using windows xp on our family laptop, which was a sony vaio. then on my first personal laptop i used windows 7 and later switched to ubuntu. i then hopped through a bunch of distros until i settled on "pop_os!" as my daily driver and "zorin os" for the older machines i found in thrift stores. i also used arch and some \*BSD distros on my servers and vms for the fun of it. but that's a story for another time.

i later learned how dual booting work. running a dual boot machine allowed me to switch between windows and linux whenever i needed to. this way i enjoyed the best of both worlds.

and i actually had never used a mac until i started working at a startup in vienna, where i was given a macbook pro as my work machine. at first i was a bit annoyed since i used to poke fun at macos users for and "paying for the brand" but i've come to realize that macos is actually amazing (at least for me).

so here's a list of the things that bother me about other operating systems and why i really enjoy using macos.

## downsides of linux

_my issues with linux:_

- lack of support for most proprietary software

     it isn't economically viable for companies to support linux as there are so many distros and so few users.

     emulators (ie. wine) break with microsoft word, zoom and even the chrome browser doesn't render the same as on windows or macos.

     you could argue that this isn't linux's fault but i think it's a valid point to make since it's a problem that you will have to deal with if you use linux.

     you need to develop your very own workflow with open source software to get work done which is a lot of work, and highly impractical if you need to collaborate with others.

- lack of support for most laptop hardware

     linux isn't meant for laptops but desktop PCs or servers.

     you have to buy dedicated hardware (like system76 laptops) for things to work right out the box or else you will have to spend hours setting up drivers.

     no distro ever recognized any peripherals on my lenovo carbon x1 laptop: external microphone, dual display setup, usb dock, wireless mouse and keyboard, fingerprint sensor, etc.

     some were impossible to set up (like the fingerprint sensor) and others were just really annoying to set up (like the dual display setup).

     i also never got more than 3 hours of battery life on linux, even with tlp and powertop installed.

     closing the lid on my laptop would also cause the system to crash and i would have to force restart it.

     when these minor issues add up, it becomes really annoying to use linux as a daily driver.

- janky gui

     i almost never had good scaling options for displays. all distros show massive screen tears and visual glitches with gnome and kde.

     this becomes less of an issue as you learn to use the terminal more, and become less dependent on the gui but it's still annoying and definitely something that makes linux less accessible to new users.

## downsides of windows

_my issues with windows:_

- wsl2 (windows subsystem for linux) is very unstable

     see: https://www.reddit.com/r/bashonubuntuonwindows/comments/opujbm/does_wsl_give_windows_an_edge_over_mac/

     you will still need to "drop back to windows" for a lot of things → usb passthrough doesn’t work, it is significantly slower, breaks vscode whenever you log off, has a reduced set of valid bash commands, etc.

- forced advertisement and updates

     since win10 won’t be getting updates from 2025, you will be forced to upgrade to win11.

     this is terrible as in win11 you have ads both in your lock screen and start menu that you can't disable.

- multiple shells

     you might have cmd and powershell but none of them are as good as bash.

     it's just something different to be able to use classic unix commands to navigate your file system and manage your software.

- aweful software management

     - environment variables must be set through the gui.
     - the file system makes deleting "node_module" folders or uninstalling programs really difficult. programs are unintuively spread across multiple folders you have no overview of.
     - package managers like scoop, winget and chocolatey don't work well together and are not as good as brew or apt.

## upsides of macos

the reason i love macos is because for me it's the best of both worlds. you get both the nice bits of linux and windows and have to sacrifice very little.

- proprietary software support
- tightly integrated laptop hardware
- unix based, bash shell, great package manager
- beautiful gui
- access to the apple ecosystem (swift, xcode, safari, etc.)
