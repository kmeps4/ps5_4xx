# PS5 4.03 Kernel Exploit By Specter
---
## Summary
This repo contains an experimental WebKit ROP implementation of a PS5 kernel exploit based on **TheFlow's IPV6 Use-After-Free (UAF)**, which was [reported on HackerOne](https://hackerone.com/reports/1441103). The exploit strategy is for the most part based on TheFlow's BSD/PS4 PoC with some changes to accommodate the annoying PS5 memory layout (for more see *Research Notes* section). It establishes an arbitrary read / (semi-arbitrary) write primitive. This exploit and its capabilities have a lot of limitations, and as such, it's mostly intended for developers to play with to reverse engineer some parts of the system.

Also note; stability is fairly low, especially compared to PS4 exploits. This is due to the bug's nature of being tied to a race condition as well as the mitigations and memory layout of the PS5. This document will contain research info about the PS5, and this exploit will undergo continued development and improvements as time goes on.

This could possibly work on 4.50 as well via substituting valid 4.50 gadget offsets + kernel slides, but that will be for future work.



## Currently Included

- Obtains arbitrary read/write and can run a basic RPC server for reads/writes (or a dump server for large reads) (must edit your own address/port into the exploit file on lines 673-677)
- Enables debug settings menu (note: you will have to fully exit settings and go back in to see it).
- Gets root privileges

## Limitations
- This exploit achieves read/write, **but not code execution**. This is because we cannot currently dump kernel code for gadgets, as kernel .text pages are marked as eXecute Only Memory (XOM). Attempting to read kernel .text pointers will panic!
- As per the above + the hypervisor (HV) enforcing kernel write protection, this exploit also **cannot install any patches or hooks into kernel space**, which means no homebrew-related code for the time being.
- Clang-based fine-grained Control Flow Integrity (CFI) is present and enforced.
- Supervisor Mode Access Prevention/Execution (SMAP/SMEP) cannot be disabled, due to the HV.
- The write primitive is somewhat constrained, as bytes 0x10-0x14 must be zero (or a valid network interface).
- The exploit's stability is currently poor. More on this below.
- On successful run, **exit the browser with circle button, PS button panics for a currently unknown reason**.

## How to use

1. Configure Al-Azid DNS on your PS5: The DNS servers are 165.227.83.145 and 192.241.221.79
2. Go to User's Guide Browser and press L2 button so you can write down a custom URL.
3. Go to https://www.kmeps4.github.io/ps5_403/index.html
4. If it done with success you should be able to see "Debug Settings" Option Enabled.

## Contributors / Special Thanks
- [Andy Nguyen / theflow0](https://twitter.com/theflow0)
- [Specter](https://github.com/Cryptogenic)
- [ChendoChap](https://github.com/ChendoChap)
- [Znullptr](https://twitter.com/Znullptr)
- [sleirsgoevy](https://twitter.com/sleirsgoevy)
- [bigboss](https://twitter.com/psxdev)
- [flatz](https://twitter.com/flat_z)
- [zecoxao](https://twitter.com/notzecoxao)
- [SocracticBliss](https://twitter.com/SocraticBliss)
- laureeeeeee



