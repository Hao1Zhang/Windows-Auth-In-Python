import win32security
import ntsecuritycon as con
with open('secret1.txt') as f:
# with open('seLuke.txt') as f:
    username = f.readline().strip()
    domain = f.readline().strip()
    password = f.readline().strip()
try:
    token = win32security.LogonUser(
        username,
        domain,
        password,
        win32security.LOGON32_LOGON_NETWORK,
        win32security.LOGON32_PROVIDER_DEFAULT)
    groupList = []
    groupList.append(win32security.GetTokenInformation(token,con.TokenGroups))
    for (sid,i) in win32security.GetTokenInformation(token,con.TokenGroups):
        print(win32security.LookupAccountSid(None,sid))
    sid,i = win32security.GetTokenInformation(token,con.TokenGroups)[3]
    
except Exception as error:
    print("Error",error)
