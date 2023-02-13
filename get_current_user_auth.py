import win32security
import win32api
import winerror
import ntsecuritycon as con
import os

GROUP_NAME = "Microsoft 365 E5 DJP"

sid, system, type = win32security.LookupAccountName (
    None, GROUP_NAME
)
if win32security.CheckTokenMembership (
    None, sid
):
   print ("I am in"), GROUP_NAME
else:
    print ("I am not in"), GROUP_NAME



