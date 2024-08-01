# plist_memory_value_converter

A small script to count the memory value you should type in config.plist.

When I configured `config.plist` and getting to boot up, it throws the error like [IOConsoleUsers: gIOScreenLock.../gIOLockState (3...](https://dortania.github.io/OpenCore-Install-Guide/troubleshooting/extended/kernel-issues.html#stuck-on-or-near-ioconsoleusers-gioscreenlock-giolockstate-3) and stucked.

Then I found that maybe I should change the frame buffer of igpu after some thinking.

However, counting the values in framebuffer, `PciRoot(0x0)/Pci(0x2,0x0)` was a little difficult, so I wrote this script for easier counting.

Hopes it could help you too.
