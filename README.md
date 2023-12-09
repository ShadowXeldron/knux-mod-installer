# Knux - A command-line mod installer for Sonic 3 Angel Island Revisited
## This program is a work-in-progress. DOn't expect it to work

ShadowXeldron's terrible ***AND VERY UNFINISHED*** command line-based [Sonic 3 AIR](https://github.com/Eukaryot/sonic3air) mod installer, created by strapping some snakes together

This exists for a few reasons:

1. To enable quick and easy installation of Sonic 3 AIR mods with only a few clicks on **ANY** website
2. To encourage forum users to switch to using GitHub
3. To create an alternative to [A.I.R.drop](https://github.com/TekkaGB/A.I.R.drop) that works on any platform (currently this only works on Linux; Mac and Windows hopefull won't be to difficult) and isn't locked to GameBanana

This project is licensed under the MIT License. This will be changed if one of the libraries used makes that unfeasible and no alternative can be found.

### FEATURES

 - Can install mods via the command line  
 - Optional extraction of ZIP files  
 - Automatic extraction of RAR and 7Z files if compatible libraries are installed.__
 - Works on Linux  
 - A working one-click installer for `knux:` URLs (a HTML file with example URLs and a sample `.desktop` file for Linux is in the `bonuses` folder)  

### INSTALLATION

TODO: put actual instructions here. Maybe also get Knux on PyPI once it's gotten somewhere?

#### Linux

1. Install dependencies
    - Required only:  
    ```pip3 install filetype requests```
    - Everything  
    ```pip3 install filetype requests py7zr rarfile```
    
    For RAR you'll also need a backend supported by rarfile.

2. Download the script  
    ```Put an wget command here```

3. (OPTIONAL) To enable one-click installation via `knux:` links:  
    ```
    Put an wget command here
    xdg-mime default knux-oci.desktop x-scheme-handler/knux
    ```

### DEPENDENCIES
Required:

 - [filetype](https://pypi.org/project/filetype/)  
 - [requests](https://pypi.org/project/requests/)  

Optional:

 - [py7zr](https://pypi.org/project/py7zr/) (for 7Z extraction)  
 - [rarfile](https://pypi.org/project/rarfile/) (for RAR extraction, also requires a compatible backend)  

### TODO LIST:

#### Absolutely Mandatory:  
 - Windows Support  
 - A configuration file (example in the `bonuses` folder)__

#### Would be nice to have
 - A proper GUI for the installer mode  
 - Other mod management things, for example mod updates, enabling and disabling mods  
 - Possibly make an LPGL version that ommits py7zr support as that may cause licensing complications  
 - Automatic mod updates. This may be a sizable logistical issue.  
 - Maybe rework any S3AIR-related queries into a custom module?  
 - Make it so you don't have to do `knux:https://example.com/mymod.zip` since it looks stupid
 
#### Highly unlikely  
 - Android support  
 - Automated listing of *any* mod website as this one is supposed to be platform-independent  

#### Would be better off as its own script
 - `sonic3airdrop:` URL handling: this is to avoid relaince on gbAPI and prevent flame wars (the S3AIR community is... fragmented, to say the least). I may make a seperate program for this.  
 - Handling of cloud storage downloads. Those are likely to be problematic as they may need their own APIs. Helper scripts may be an option for that.  
 - If the library idea comes to pass, it could likely be very useful for these scenarios.  


