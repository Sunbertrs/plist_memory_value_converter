# plist_memory_value_converter

A small script to calculate the memory value you should type in config.plist.

When I configured `config.plist` and getting to boot up, it throws the error like [IOConsoleUsers: gIOScreenLock.../gIOLockState (3...](https://dortania.github.io/OpenCore-Install-Guide/troubleshooting/extended/kernel-issues.html#stuck-on-or-near-ioconsoleusers-gioscreenlock-giolockstate-3) and stucked.

Then I found that maybe I should change the frame buffer of igpu after some thinking.

However, it was a little difficult to calculate the values in framebuffer, `PciRoot(0x0)/Pci(0x2,0x0)` so I wrote this script for convenient.

Hopes it could help you too.

>  At last, I finally got to the install interface by changing the value of `AAPL,ig-platform-id` to `78563412`, which is the default value in a clover `config.plist`... Yeh, for some situation that you stuck at `gIOScreenLock...` you can try this universal value, after many times' changing following the dortania's tutorial but don't work.

## Usage

Option 1 and 2 can convert the memory you want to the value that OpenCore/Clover can read, or convert them back. (Please use plist editor for modify or you need to encrypt the value with base64 encode)

E.g. Choose `1. MB to value` and type `12` (MB), it will return `Value you should type: 0000c000`. Then, type this value `0000c000` for `framebuffer-stolenmem` or where you need to.

`2. Value to MB` option is for those who don't know how many memory it stands for.

`3. Hexadecimal to value` option is rarely used, it is usually for those who want to change their `AAPL,ig-platform-id`.
