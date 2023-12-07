# a love letter to macos

this is just a personal story on how i came to love macos and in no way a recommendation for you to switch to macos – please use whatever works best for you and ✨brings you the most joy✨.

i was inspired to make this post because of wolfgang's video on [why he switched to macos (as a linux user)](https://www.youtube.com/watch?v=X0DIHlnD_S0).

i've used windows, linux and macos as my daily driver for years and thought i might share my thoughts on the topic.

i initially started using windows xp on our family laptop, which was a sony vaio.

i then switched to ubuntu on my first personal laptop, which was a huge lenovo machine. i hopped through a bunch of distros until i settled on "pop_os!" and "zorin os" for older machines. i also used arch and some \*BSD distros on my servers and vms for the fun of it.

running a dual boot machine allowed me to switch between windows and linux whenever i needed to and enjoy the best of both worlds.

i actually had never used a mac until i started working at a startup in vienna, where i was given a macbook pro as my work machine.

at first i was a bit annoyed since i used to poke fun at macos users for and "paying for the brand" but i've come to realize that macos is actually the best option for developers like me, who want to get work done without much setup. additionally, the quality of the hardware and the tight integration with the os is unmatched.

so here's a list of the things that bother me about other operating systems and why i really enjoy using macos.

## linux

_my issues with linux:_

- bad support for proprietary software

     emulators break with microsoft word, zoom and even the chrome browser doesn't render the same as on windows or macos.

     you need to develop your very own workflow with open source software to get work done which is a lot of work, especially when collaborating with less technical people.

- close to no support for proprietary laptop hardware

     linux isn't meant for laptops. you have to buy dedicated hardware (like system76 laptops) for things to work right out the box or else you will have to spend hours setting up drivers.

     no distro ever recognized any peripherals on my lenovo carbon x1 laptop: external microphone, dual display setup, usb dock, wireless mouse and keyboard, fingerprint sensor, etc.

     some were impossible to set up (like the fingerprint sensor) and others were just really annoying to set up (like the dual display setup).

     i also never got more than 3 hours of battery life on linux, even with tlp and powertop installed.

     closing the lid on my laptop would also cause the system to crash and i would have to force restart it.

     when these minor issues add up, it becomes really annoying to use linux as a daily driver.

- janky gui

     i almost never had good scaling options for displays. all distros show massive screen tears and visual glitches with gnome and kde.

     this becomes less of an issue as you learn to use the terminal more, and become less dependent on the gui but it's still annoying and definitely something that makes linux less accessible to new users.

## windows

_my issues with windows:_

- wsl2 (windows subsystem for linux) is very unstable

     see: https://www.reddit.com/r/bashonubuntuonwindows/comments/opujbm/does_wsl_give_windows_an_edge_over_mac/

     you will still need to "drop back to windows" for a lot of things → usb passthrough doesn’t work, it is significantly slower, breaks vscode whenever you log off, has a reduced set of valid bash commands, etc.

- forced advertisement and updates

     since win10 won’t be getting updates from 2025, you will be forced to upgrade to win11.
     but unfortunately in win11 you have ads both in your lock screen and start menu and aren’t able to disable them.

- multiple shells

     the native shells (cmd, powershell, wsl, git bash) don't come close to the experience of using a single shell like bash or zsh on linux or macos.

- aweful software management

     - environment variables must be set through the gui.

     - the file system makes deleting node_modules folders or uninstalling programs really difficult. programs are unintuively spread across multiple folders you have no overview of.

     - package managers like scoop, winget and chocolatey don't work well together and are not as good as brew or apt.

## macos

_my favorite things about macos:_

- very performant but affordable laptops

     the hardware is tightly integrated with the os and the battery life is amazing.

- beautiful gui

- unix based

- a single package manager that is accepted by the entire community: brew

- the ability to test software on the safari browser and ios emulator
