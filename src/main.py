import os
import shutil

def main():
    dst = "./public"
    src = "./static"

    copy_files(src, dst)

def copy_files(src, dst):
    clean_destination(dst)
    shutil.copytree(src, dst, copy_function=copy_and_print)

def clean_destination(dst):
    # Remove the directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst, ignore_errors=True)

def copy_and_print(src, dst):
    print(f'Copying {src} to {dst}')
    return shutil.copy2(src, dst)
    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()