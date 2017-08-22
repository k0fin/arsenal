# Arsenal

## About

* Arsenal is a Python script made to automate the download and installation of
  multiple pentesting and security-related tools and scripts. Additionally,
  several other tools and installation scripts are included in Arsenal,
  which automate the download and installation of tools such as CobaltStrike and Hostapd-WPE.
  
## Requirements

* Run 'pip install blessings' (used in Arsenal for proper console output) and you should be good to go.

## Install

* Kali Linux Configuration

Arsenal will perform the following configurations-

  - Update and upgrade

* Core Tools Installation

Arsenal will download and install the following tools-

  - The Backdoor Factory
  - HTTPScreenshot
  - Masscan
  - Gitrob
  - CMSmap
  - WPScan
  - Eyewitness
  - Praedasploit
  - SQLMap
  - Recon-NG
  - Discover Scripts
  - Browser Exploitation Framework
  - Responder
  - DumpNTDS
  - SPARTA
  - NoSQLMap
  - Spiderfoot
  - Windows Credential Editor
  - Mimikatz
  - Social Engineering Toolkit
  - PowerSploit
  - Nishang
  - Veil-Framework
  - BurpSuitePro
  - Burp Fuzzing Lists
  - Password Lists
  - Net-Creds Network Parsing
  - Firefox Add-Ons
  - Wifite
  - WIFIPhisher
  - Phishing Frenzy
  - SMBExec
  - Pykek
  - BloodHound
  - Sn1p3r

## Usage

* Arsenal utilizes files containing the instructions for tools installation and updates.
* There are 3 files under the instruct folder named arsenal-tools, arsenal-updates, and arsenal-extras.
  In the conf folder, a file named arsenal.conf contains global variables which are parsed by the Arsenal script.
  These global variables point to the files used for updates, tools, and extras. By default, the 3 files mentioned earlier
  are used in this configuration file. Any edits made to the configuration file could possibly break the tool if written improperly,
  so use caution when adding extra tool sources, update commands, or install scripts.

*  Simply run the arsenal.py script.

  - ./arsenal.py

## Tools

* The arsenal-tools files contains the instructions parsed by Arsenal to install tools.
  The instructions within the file look something like this-

...snip...

TITLE=TOOLNAME
PREINSTALL=COMMANDS_TO_INSTALL_BEFORE_DOWNLOADING_THE_TOOL
CLIENT_CMD=WEB CLIENT TO USE FOR DOWNLOADING THE TOOL
URL=URL TO TOOL
PATH=TOOL INSTALLATION PATH
INSTALL=COMMAND_TO_INSTALL_TOOL

...snip...
