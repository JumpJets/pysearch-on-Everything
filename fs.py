# -*- coding: utf-8 -*-
import platform
import argparse
from ctypes import *
#from ctypes.wintypes import BOOL, DWORD, LPARAM, WPARAM, UINT

arch = platform.architecture()
parser = argparse.ArgumentParser(description="Return catalogs and search request in it. Using Everything API.")
parser.add_argument('string', metavar='Path', type=str, nargs='+', help='directory')
parser.add_argument('--regex', '-r', dest='regex', action="store", nargs='+', default="", help='use regex search')
parser.add_argument('--search', '-s', dest='subst', action="store", nargs='+', default="", help='search in directory')
args = parser.parse_args()
args.string = ' '.join(args.string)

def main():
    if arch[0] == '32bit':
        hllDll = WinDLL ("Everything32.dll")
    elif arch[0] == '64bit':
        hllDll = WinDLL ("Everything64.dll")
    else:
        print("Can't use provided DLLs on architecture: %s" % arch[0])

    """
    https://www.voidtools.com/support/everything/sdk/
    Manipulating the search state
        Everything_SetSearchW
        Everything_SetMatchPath
        Everything_SetMatchCase
        Everything_SetMatchWholeWord
        Everything_SetRegex
        Everything_SetMax
        Everything_SetOffset
        Everything_SetReplyWindow
        Everything_SetReplyID
        Everything_Reset

    Reading the search state
        Everything_GetSearch
        Everything_GetMatchPath
        Everything_GetMatchCase
        Everything_GetMatchWholeWord
        Everything_GetRegex
        Everything_GetMax
        Everything_GetOffset
        Everything_GetReplyWindow
        Everything_GetReplyID
        Everything_GetLastError

    Executing the query
        Everything_QueryW

    Check for query reply
        Everything_IsQueryReply

    Manipulating results
        Everything_SortResultsByPath
        Everything_Reset

    Reading results
        Everything_GetNumFileResults
        Everything_GetNumFolderResults
        Everything_GetNumResults
        Everything_GetTotFileResults
        Everything_GetTotFolderResults
        Everything_GetTotResults
        Everything_IsVolumeResult
        Everything_IsFolderResult
        Everything_IsFileResult
        Everything_GetResultFileName
        Everything_GetResultPath
        Everything_GetResultFullPathName
    """
    """eDLL = WinDLL("Everything32")
    eDLL.argtypes = [c_wchar_p]
    eDLL.restype = c_void_p
    r = eDLL.Everything_SetSearchW("a")#.value
    print(r)
    eDLL.argtypes = [c_bool]
    eDLL.restype = c_bool
    r = eDLL.Everything_QueryW(True)#.value
    print(r)
    eDLL.argtypes = [c_void_p]
    eDLL.restype = c_ulong
    r = eDLL.Everything_GetNumResults()#.value
    print(r)"""

    """SetSearch = WinDLL('Everything32').Everything_SetSearchW
    SetSearch.argtypes = [None,c_wchar_p]
    SetSearch.restype = None
    #def SetSearch(self=None):
    #    ss = "test"
    #    _SetSearch(self, ss)
    SetSearch(None,"test")"""

    """hllApiProto = WINFUNCTYPE(c_wchar_p) #c_void_p,
    hllApiParams = (1, "String", "0")
    hllApi = hllApiProto (("Everything_SetSearchW", hllDll), hllApiParams) #ValueError: paramflags must have the same length as argtypes
    String = c_wchar_p
    hllApi (byref (String))"""
    
    """prototype = WINFUNCTYPE(c_wchar_p)
    paramflags = (1, "String", "Witcher")
    SetSearch = prototype(("SetSearchW", hllDll.Everything_SetSearchW), paramflags)
    SetSearch()
    hllDll.Everything_SetSearchW("test")
    #id = hllDll.Everything_GetReplyID()
    prototype = WINFUNCTYPE(BOOL)
    paramflags = (1, "Wait", True)
    Query = prototype(("QueryW", hllDll.Everything_QueryW), paramflags)
    Query()
    #hllDll.Everything_QueryW(True)
    #hllDll.Everything_IsQueryReply(m.Msg, m.WParam, m.LParam, MY_REPLY_ID)
    r = hllDll.Everything_GetNumResults()
    prototype = WINFUNCTYPE(None)
    #paramflags = (1, "Wait", True)
    GetNumResults = prototype(("GetNumResults", hllDll.Everything_GetNumResults))
    print(GetNumResults())"""

    """#b = hllDll.Everything_IsQueryReply(UINT message,WPARAM wParam,LPARAM lParam, DWORD nId)
    bufsize = 260
    buf = create_string_buffer(bufsize)
    t = []
    for i in range(0, 10):
        t.append(hllDll.Everything_GetResultFullPathNameW(i, buf, bufsize))
    
    print(t)"""

if __name__ == "__main__":
    main()