#!/bin/python
# The above line is used to tell Linux to run this script with Python so you can call it right from the command line. How very convenient!

import os
import argparse

# Commented arguments are unimplemented and do nothing.
parser = argparse.ArgumentParser()
loaderMode = parser.add_mutually_exclusive_group()
loaderMode.add_argument("-i", "--install", dest="mod_url", help="Installs a mod from a specified URL.")
loaderMode.add_argument("-id", "--install-dialog", dest="mod_url_dialog", help="Installs a mod from a specified URL. This makes the script use tkinter dialogs instead of CLI inputs and is meant to be called for one-click installs.")
loaderMode.add_argument("-r", "--remove", dest="folder_to_delete", help="Deletes the specified mod based on folder name.", type=str)
loaderMode.add_argument("-l", "--list", action="store_true", help="Lists the folder names of all currently installed mods.")
loaderMode.add_argument("-e","--enable", dest="folder_to_enable", help="Enables the specified mod based on folder name.", type=str)
"""
loaderMode.add_argument("-d", "--disable", dest="folder_to_disable", help="Disables the specified mod based on folder name.", type=str)
loaderMode.add_argument("-u", "--update", dest="folder_to_update", help="Updates the specified mod based on folder name. Leave blank to scan all mods for update", type=str)
loaderMode.add_argument("-U", "--update-all", action="store_true", help="Scans all installed mods (with the exception of those in the ignore file) for updates.")
loaderMode.add_argument("-p", "--modpack", action="modpack_json", help="Modpack options.")
loaderMode.add_argument("-c", "--config", action="modpack_json", help="Alters the script's configuration file.")
"""
parser.add_argument("-fn", "--folder-name", dest="folder_name", help="Only used in tandem with -i/--install. Sets the filename of the download. Leaving this blank will autogenerate a name. More often that not, including this doesn't really matter since the mod's subfolder will have its intended name. If a mod isn't packaged as a subfolder or is a 7Z file then you can use this option to give it its proper name") # I should probably phrase this a bit better
args = parser.parse_args()

#modurl = sys.argv[0]

def getModPath():
        import platform

        s3airPath = ""

        print(platform.system())
        if platform.system() == "Linux": # For us pros who use Linux
            #return os.path.expanduser('~/.local/share/Sonic3AIR/mods')
            #return os.path.expanduser('~/.var/app/org.sonic3air.Sonic3AIR/data/Sonic3AIR/mods/')


            nativePath = os.path.exists(os.path.expanduser('~/.local/share/Sonic3AIR/mods'))
            flatpakPath = os.path.expanduser('~/.var/app/org.sonic3air.Sonic3AIR/data/Sonic3AIR/mods/')

            if args.mod_url_dialog:
                print("""
                    It seems that both the native and Flatpak versions of Sonic 3 AIR have been installed on your system.

                    You can change your settings in the configuration file (NOTE TO SELF: Not actually implemented yet)

                    """)

            else:
                print("""
                    It seems that both the native and Flatpak versions of Sonic 3 AIR have been installed on your system.

                    You can change your settings in the configuration file (NOTE TO SELF: Not actually implemented yet)

                    """)

            return os.path.expanduser('~/.local/share/Sonic3AIR/mods') # Placeholder behaviour. There should be a dialogue box



        #if platform.system() == "Windows": # For the silly people who still use Windows

        #if platform.system() == "Darwin": # For the weirdos who use Mac

def handleZipFile():
    if args.mod_url_dialog: # Python programming is my passion
        return tkinter.messagebox.askyesno(title="Knux 1-Click Mod Installer", message="Sonic 3 AIR is able to load mods from ZIPs so extraction is not required. However, extacting the mod may improve performance. Would you like to extract the archive?")

    else:
        if input("Sonic 3 AIR is able to load mods from ZIPs so extraction is not required. However, extacting the mod may improve performance. Would you like to extract the archive? (y/n)") == "y":
            return True

# At this point, all the actual program logic happens.

print("""
Knux-CLI - the command line mod manager for Sonic 3 Angel Island Revisted

    THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

This means that if you break something then it's your fault.

Found a bug? Report it here: *INSERT GITHUB LINK HERE*
""")



loadIssues = False

if args.mod_url or args.mod_url_dialog: # If the script is set to installer mode with the -i argument

    # I'm only loading Python modules if I need them.

    import requests
    import filetype
    from urllib.parse import urlparse

    # Archive formats

    try:
        import zipfile
    except:
        print("Could not import zipfile. ZIP extraction will not work, but zipped mods can still be installed as S3AIR supports them out of the box.")
        loadIssues = True

    try:
        import py7zr
    except:
        print("Could not import py7zr. 7Z files cannot extracted")
        print("py7zr can be found here: https://pypi.org/project/py7zr/")
        loadIssues = True

    try:
        import rarfile # No hate on the makers of this library (hate on the makers of RAR instead), but I honestly think RAR is a bad format because it isn't open source like 7Z is.
    except:
        print("Could not import rarfile. RAR files cannot extracted")
        print("rarfile can be found here: https://pypi.org/project/rarfile/")
        print("You will also need to install unrar or unar.")
        print("Note that RAR is a terrible proprietary format that nobody likes and is only included for full GameBanana support. This message can be disabled in the config.")
        loadIssues = True

    if loadIssues == True:
        input("Some extraction libraries are missing. Are you sure you would like to continue?")

    if args.mod_url_dialog:
        import tkinter
        #from tkinter import simpledialog
        from tkinter import messagebox # This makes me grumpy. I wish I could just have the lot.

    # Main Python code for the Knux command line mod manager for Sonic 3 AIR

    s3airmodpath = getModPath()

    print(s3airmodpath)

    if os.path.exists(s3airmodpath) == True: # Checks if the folder for Sonic 3 AIR has been found
        print("Mods folder found!")
        if not os.path.exists(f"{s3airmodpath}/knux-installs"):
            os.makedirs(f"{s3airmodpath}/knux-installs")
            print(f"Created installation folder at {s3airmodpath}/knux-installs")
        else:
            print("Installation folder found!")
    else:
        print("Mods folder not found! Have you installed Sonic 3 AIR yet?")
        exit()

    #if modurl == "":

    if args.mod_url:
        modurl = args.mod_url
    elif args.mod_url_dialog:
        modurl = args.mod_url_dialog

    o = urlparse(modurl)

    if o.scheme == "knux":
        print("Using knux link; de-knux-ifying")
        modurl = o.path

    #if args.mod_url_dialog:
    #    modname = tkinter.simpledialog.askstring("Knux One Click Installer", "Enter mod name (used for the folder name, leave blank or cancel to autogenerate)")
    #    if modname == "None":
    #        modname = ""

    """else:
        modname = input("Enter mod name (used for the filename, leave blank to autogenerate): ")

    if modname == "":"""

    if args.folder_name:
        modname = args.folder_name

    else:
        print("Auto-generating folder name")
        modno = 0
        hasAName = False

        while hasAName == False:
            tryname = f"knux-download-{modno}"
            if not os.path.exists(f"{s3airmodpath}/knux-installs/{tryname}") and not os.path.exists(f"{s3airmodpath}/knux-installs/extracted-{tryname}") and not os.path.exists(f"{s3airmodpath}/knux-installs/{tryname}.zip"):
                modname = tryname
                hasAName = True
            else:
                modno += 1

    print(f"Downloading as {modname}")
    print("Downloading mod, please be patient")
    download = requests.get(modurl, allow_redirects=True)
    #request.urlretrieve(modurl, filename=f"{s3airmodpath}/knux-installs/{modname}")
    print("Download complete, writing to mods folder")

    installedpath = f"{s3airmodpath}/knux-installs/{modname}"

    with open(installedpath, 'wb') as f:
        f.write(download.content)

    kind = filetype.guess(installedpath)


    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

    if kind.extension == "zip":

        print("Mod uses ZIP compression. Extracting...")
        choice = ""

        if handleZipFile() == True: # This allows you to be gooey or cli-ey

            with zipfile.ZipFile(installedpath, mode='r') as z:
                try:
                    f = z.open("mod.json")
                    print("mod.json in root directory. Creating mod folder")
                    #f.reset()
                    os.makedirs(f"{s3airmodpath}/knux-installs/extracted-{modname}")
                    z.extractall(path=f"{s3airmodpath}/knux-installs/extracted-{modname}")

                except:
                    z.extractall(path=f"{s3airmodpath}/knux-installs/")

            print("Extraction completed")

        else:
            os.rename(installedpath, f"{installedpath}.zip")
            print("Mod installed without extracting!")
            exit()

    elif kind.extension == "7z":
        print("Mod uses 7Z compression. Extracting...")

        with py7zr.SevenZipFile(installedpath, mode='r') as z: # I can't figure our how to add subfolder detection for 7z files so here's some junk
            #try:
            f = z.read("mod.json")
            print("mod.json in root directory. Creating mod folder")
            os.makedirs(f"{s3airmodpath}/knux-installs/extracted-{modname}")
            z.extractall(path=f"{s3airmodpath}/knux-installs/extracted-{modname}")
            #except:
            #print(z.list())
            #z.extractall(path=f"{s3airmodpath}/knux-installs/")

            print("Extraction completed")


    elif kind.extension == "rar": # I can't make RARs without causing package issues; maybe I'll need to set up a distrobox for that
        print("For some stupid reason, this mod uses RAR compression. Extracting...") # RAR + RARtio + RAR issue. RARfile is still a terRARfic library though and I'd probably be stuck without it.

        with rarfile.RarFile(installedpath) as z:
            try:
                f = z.open("mod.json")
                print("mod.json in root directory. Creating mod folder")
                os.makedirs(f"{s3airmodpath}/knux-installs/extracted-{modname}")
                z.extractall(path=f"{s3airmodpath}/knux-installs/extracted-{modname}")
            except:
                z.extractall(path=f"{s3airmodpath}/knux-installs/")

            print("Extracted the RAR. Absolutely proprietary.")

    else:
        print("Unsupported archive format! You'll have to extract it yourself to complete the installation process. The path to the file is:")
        print(installedpath)

        exit()

    if kind.extension == "rar":
        print("Purging the foul RAR to save space")
    else:
        print("Deleting archive file to save space")

    os.remove(installedpath)
    print("Mod installed!")

elif args.list:
    #from pathlib import Path

    modpath = getModPath()
    pdir_list = os.listdir(modpath)
    knownmods = []
    modcount = 0

    print("Installed mods:") # TODO: Make this also count mods in subdirectories
    for counter in pdir_list:
        if os.path.isdir(f"{modpath}/{counter}"):
            if os.path.exists(f"{modpath}/{counter}/mod.json"): # Maybe something else would be a bit more optimal
                print(counter)
                modcount += 1

    print("\nNumber of installed mods:", modcount)

elif args.folder_to_delete:
    import shutil
    modpath = getModPath()

    if os.path.isdir(f"{modpath}/{args.folder_to_delete}"):
        if input(f"\033[1mTHIS WILL DELETE THE MOD '{args.folder_to_delete}'! Are you sure that you want to delete this mod? (y/n): ") == "y":
            print("\033[0mDeleting mod...")
            shutil.rmtree(f"{modpath}/{args.folder_to_delete}")
            print("Mod deleted!")
    else:
        print(f"Mod folder '{args.folder_to_delete}' not found.")


elif args.folder_to_enable:
    import json

    modpath = getModPath()
    modDotJson = open(f"{modpath}/active-mods.json", "r+", encoding="utf-8")
    print(json.dumps(modDotJson.read()))

# If you use WinRAR then I am very ashamed of you.

else:
    print("No arguments specified! Run knux -h for more information.")


# Russian Shadow my beloved

# tom my installer is better than yours



























