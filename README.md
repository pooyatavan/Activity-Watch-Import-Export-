# ActivityWatch Scripts (Import / Export)

This project collects ActivityWatch data from all your systems and imports it into a central server so you can see activity for every machine in one place.

- **Export**: The export script reads all data from ActivityWatch via its API, saves it to a JSON file, and uploads that file to OneDrive.
- **Import**: The import script deletes every existing bucket from the previous run, then imports and updates all buckets from the JSON files stored in OneDrive back into ActivityWatch.

## Requirements

1. OneDrive app installed on all Windows clients and servers (all signed in with the **same account**).
2. Python installed on the server (for running the import scripts).

## Installation

## ActivityWatch

Install ActivityWatch with the default settings on all computers that you want to track.

Link: [https://activitywatch.net/](https://activitywatch.net/)

## OneDrive Setup

Install OneDrive (most Windows machines include it by default; if not, download and install it).

- Sign in to the **same OneDrive account** on all computers.
- All clients and the server must use a single shared OneDrive account to access the same sync folder.

## Windows Task Scheduler

Use Windows Task Scheduler to automate export/import so it runs every 30 minutes (or any schedule you prefer).

**Trigger Setup**:
1. Set "Begin the task" to "One time".
2. Configure "Repeat task every" to the desired interval (minutes or hours).
3. Set "For a duration of" to "Indefinitely".

**Action Setup**:
1. In the Actions tab, browse to and select the .bat file for the script you want to run.

## Hiding Command Prompt Window

To avoid the black command prompt window appearing every time the script runs, convert the .bat file to an .exe using a "bat to exe" tool.

Tool: [Bat To Exe Converter](https://www.majorgeeks.com/mg/getmirror/bat_to_exe_converter,1.html)

**Conversion Steps**:
1. Open the app and load your run.bat file.
2. In the Options tab, set the EXE format to: "64-bit Windows | Screen (Invisible)".
3. Click Convert (choose 64-bit or 32-bit depending on your machines).

## For Server
- download and install Python with pip [Python](https://www.python.org/)
- open command prompt and run this command: pip install aw_client
  
## Recommendations

- Use OneDrive if you do not already have a cloud storage service (reliable and pre-installed on most Windows machines).
- To use another cloud provider, update the paths in the scripts to point to that service's sync folder.

## Important Notes

All paths in this project are configured for OneDrive. If you want to use another cloud service, update the paths in the scripts accordingly.
