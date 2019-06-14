import os
import shutil
import wmi
from datetime import datetime
import stat

def onerror(func, path, exc_info):  # handle error caused by rmtree()
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise Exception(f"unknown error occurred when delete '{path}'")

def is_too_full(client, character):
    for physical_disk in client.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                if logical_disk.Caption == character:
                    total = int(logical_disk.Size)/(1024**3)
                    free = int(logical_disk.FreeSpace)/(1024**3)
                    print(f"{character}\t{free}/{total}")
                    return True if free/total < 0.1 else False
    return None

def clean_workspace(path):
    white_list = ['INV.Shared.Repo']

    if os.path.exists(path):
        list = os.listdir(path)
        for dir in list:
            if dir in white_list:
                continue
            physi_path = os.path.join(path, dir)
            m_time = datetime.fromtimestamp(os.stat(physi_path).st_mtime)
            now = datetime.utcnow()
            delta = now - m_time

            if os.path.isdir(physi_path) and delta.days > 30:
                shutil.rmtree(physi_path, onerror=onerror)

def clean_3p_folder(path):
    if os.path.exists(path):
        list = os.listdir(path)
        for file in list:
            file = os.path.join(path, file)
            if os.path.isdir(file):
                shutil.rmtree(file, onerror=onerror)
            else:
                if not os.access(file, os.W_OK):
                    os.chmod(file, stat.S_IWUSR)
                os.remove(file)

if __name__ == "__main__":
    client = wmi.WMI()
    third_party_path = os.environ.get('_INV_3RD_PARTY_LOCALDIR')
    character = third_party_path.split("\\")[0]
    workspace = os.path.join(os.path.abspath(os.path.join(third_party_path, os.pardir)), "JKS_AUTOBUILD")

    if is_too_full(client, character):
        clean_workspace(workspace)
        if is_too_full(client, character):
            clean_3p_folder(third_party_path)
