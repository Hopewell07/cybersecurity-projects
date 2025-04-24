import os
import stat

def check_permissions(file_path):
    mode = os.stat(file_path).st_mode
    permissions = stat.S_IMODE(mode)
    
    if permissions in [0o777, 0o666]:
        return True, oct(permissions)
    else:
        return False, oct(permissions)

# Audit all files in current directory
for file in os.listdir("."):
    if os.path.isfile(file):
        insecure, perms = check_permissions(file)
        if insecure:
            print(f"⚠️  Insecure: {file} has permissions {perms}")
        else:
            print(f"✅ Secure: {file} has permissions {perms}")
