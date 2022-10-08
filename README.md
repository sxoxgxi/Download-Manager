# Download-Manager
My personal downloads manager in python
![Downloads](https://i.ibb.co/3hMVR5L/Screenshot-2022-06-12-142000.png "Downloads Folder")
## Running from commandline (powershell)
* Create a new function in your powershell profile:
```ps1
function clean {
    # The clean.bat file location ↓
    start "C:\Users\sxoxgxi\Downloads\Executables\clean.bat"
}
```
* Now everytime you type `clean` and hit enter on powershell terminal. The script will be executed.
