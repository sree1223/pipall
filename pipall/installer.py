import sys
import subprocess
import os
import sysconfig


def get_py_paths():
    try:
        result = subprocess.run(["py", "-0p"], stdout=subprocess.PIPE, text=True, check=True)
        versions = result.stdout.strip().split('\n')
        pylist = []
        for i in versions:
            pylist.append((i.strip().split()[-1][:-10],
                          i.strip().split("-V:")[1].split()[0]))
        return pylist
    except subprocess.CalledProcessError as e:
        print(f"Error getting installed Python versions: {e}")
        return []
    
def install_library(library_name):
    installed_versions = get_py_paths()
    if not library_name:
        print("Please provide a library name for installation.")
        return
    
    for each in installed_versions:
        path = each[0]
        python_version = each[1]
        pip_executable = os.path.join(path, f"Scripts\pip.exe")                
        if os.path.exists(pip_executable):
            try:
                subprocess.run([pip_executable, "install", library_name], check=True)
                print(f"Library '{library_name}' installed successfully for Python version {python_version}")
            except subprocess.CalledProcessError as e:
                print(f"Error installing '{library_name}' for Python version {python_version}: {e}")
        else:
            print(f"pip not found for Python version {python_version}")
    


def uninstall_library(library_name):
    installed_versions = get_py_paths()
    if not library_name:
        print("Please provide a library name for installation.")
        return
    
    for each in installed_versions:
        path = each[0]
        python_version = each[1]
        path = os.path.join(path, f"python.exe")
        
        if os.path.exists(path):
            try:
                subprocess.run([path, "-m", "pip", "uninstall", "-y", library_name], check=True)
                print(f"Library '{library_name}' installed successfully for Python version {python_version}")
            except subprocess.CalledProcessError as e:
                print(f"Error installing '{library_name}' for Python version {python_version}: {e}")
        else:
            print(f"pip not found for Python version {python_version}")
    

def pythons():
    try:
        result = subprocess.run(["py", "-0p"], stdout=subprocess.PIPE, text=True, check=True)
        versions = result.stdout.strip().split('\n')
        for py in versions:
            print(py)
    except subprocess.CalledProcessError as e:
        print(f"Error getting installed Python versions: {e}")

def list_installed_libraries():
    installed_versions = get_py_paths()
<<<<<<< HEAD
    print("Select the python version to list libraries under it :")
    count = 0
    for each in installed_versions:
        print(count+1,") ",each[1])
        count += 1
=======
    print("Select the python version to list libraries under it")
    count = 0
    for each in installed_versions:
        print(count,") ",each[1])
>>>>>>> 7a6da01e9eacfb4840e296fbe1fc74e995540649
    print()
    index = input("Enter the index number of Python Version : ")
    
    try:
        each = installed_versions[int(index)-1]
<<<<<<< HEAD
=======
        print(each)
>>>>>>> 7a6da01e9eacfb4840e296fbe1fc74e995540649
        path = each[0]
        python_version = each[1]
        pip_executable = os.path.join(path, f"Scripts\pip.exe")                
        if os.path.exists(pip_executable):
            try:
                result = subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=subprocess.PIPE, check=True)
                installed_libraries = result.stdout.decode("utf-8").split('\n')
                print(f"Installed libraries on Python -V:{python_version} -")
                for lib in installed_libraries:
                    print(lib)
            except subprocess.CalledProcessError as e:
                print(f"Error listing installed libraries: {e}")
    except:
        print("Index Out of Range")

def print_help():
    print("pipall commands:")
<<<<<<< HEAD
    print("  pipall install <library_name>      :  Install a Library for all Python versions")
    print("  pipall uninstall <library_name>    :  Uninstall a Library for all Python versions")
    print("  pipall pythons                     :  List all versions of Python Installed")
    print("  pipall list                        :  List all Libraries under a Python Version")
=======
    print("  pipall install <library_name>      :  Install a Library")
    print("  pipall uninstall <library_name>    :  Uninstall a Library")
    print("  pipall pythons                     :  List all versions of Python Installed")
    print("  pipall listlib                     :  List all Libraries under a ")
>>>>>>> 7a6da01e9eacfb4840e296fbe1fc74e995540649
    print("  pipall help                        :  List all commands under pipall")
    print("  pipall developer                   :  Developer info")

def developer():
    print("Email    :- sreeharsha120203@gmail.com")
    print("Linkedin :- https://github.com/sree1223")
    print("Linkedin :- https://www.linkedin.com/in/sree1223")
    

def main():
    # Check the command and call the appropriate function
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "install":
            install_library(sys.argv[2] if len(sys.argv) > 2 else None)
        elif command == "uninstall":
            uninstall_library(sys.argv[2] if len(sys.argv) > 2 else None)
        elif command == "list":
            list_installed_libraries()
        elif command == "help":
            print_help()
        elif command == "pythons":
            pythons()
        elif command == "developer":
            developer()
        else:
            print(f"Unknown command: {command}")
    else:
        print("Please provide a command. Use 'pipall help' for help.")

if __name__ == "__main__":
    main()