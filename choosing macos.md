# choosing macos

here's a list of the things that bother me about other operating systems (for laptop usage). so much so that i'm willing to pay the apple tax to use macOS.

this is in no way a recommendation for you to switch to macos. please use whatever works best for your workflow. also check out wolfgang's video on [why he switched to macos (as a linux user)](https://www.youtube.com/watch?v=X0DIHlnD_S0) and james mickens' presention of [his life as a developer](https://youtu.be/7Nj9ZjwOdFQ?si=mhz86GWUVsvk6sPe&t=1009) as they cover a lot of the same points.

## downsides of linux

choosing linux for servers? absolutely! it's the go-to for reliability and performance. but when it comes to desktops, your daily driver, it's a bit different: many folks opt for linux because they love ricing their distro or they support open-source ideals. it can be fun and impactful, but let's face it, sometimes it's not the most practical choice for everyday use.

is this linux's fault? or is it more about big tech not playing nice? it's a valid debate.

- lack of support for most proprietary software:

     it isn't economically viable for companies to support linux due to the variety of distros and fewer users. most software you're used to from other operating systems, might behave very differently on linux. plus, popular emulators like wine don't always play nice with tools like microsoft-word or excel, leading to compatibility issues. while open-source alternatives exist, team collaboration can suffer when everyone isn't on the same page software-wise.

- lack of support for most laptop hardware:

     you often need dedicated hardware (like system76 laptops) for things to work right out of the box, or else you'll spend hours searching and configuring drivers. my lenovo carbon x1 gen7 laptop faced recognition issues with external peripherals like microphones, dual displays, usb docks, wireless mouse and keyboard, and fingerprint sensors etc. some were downright impossible to set up, while others were just really annoying. additionally, battery life was significantly reduced compared to other operating systems, even with power management tools installed (tlp, powertop). closing the lid on my laptop would sometimes cause the system to crash, requiring a force restart.

## downsides of windows

- forced advertisement, updates

     you're forced to use windows 11 after 2025 because by then windows 10 won’t receive any updates. but windows 11 comes with ads on the lock screen and start menu that you can’t turn off. luckily, you can mitigate this problem by using tools like win debloat: https://github.com/LeDragoX/Win-Debloat-Tools

- wsl2 (windows subsystem for linux) is very unstable

     see: https://www.reddit.com/r/bashonubuntuonwindows/comments/opujbm/does_wsl_give_windows_an_edge_over_mac/

     wsl isn't mature enough yet. you will still need to "drop back to windows" for a lot of things. usb passthrough doesn’t work or is significantly slower, wsl crashes vscode whenever you log off and has a reduced instruction set of bash commands etc.

- multiple shells

     you might have cmd and powershell but none of them are as good as bash.

     it's just something different to be able to use classic unix commands to navigate your file system and manage your software.

- aweful software management

     - environment variables must be set through the gui.
     - NTFS makes deleting many adjacent files in ie. `node_module` folders really difficult.
     - program files are spread across the filesystem which makes it hard to declutter unused software.
     - package managers like `scoop`, `winget` and `chocolatey` are no where as popular in the community as `brew` or `apt`.
