# -*- coding: utf-8 -*-
#
# ***********************************************************************************
# MIT License
#
# Copyright (c) 2020 Kevin G. Schlosser
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# ***********************************************************************************


# **********************************************************************************************************************
# Copyright 2012 NVIDIA Corporation. All rights reserved.
# NOTICE TO USER:
# This software is subject to NVIDIA ownership rights under U.S. and international Copyright laws.
# This software and the information contained herein are PROPRIETARY and CONFIDENTIAL to NVIDIA
# and are being provided solely under the terms and conditions of an NVIDIA software license agreement.
# Otherwise, you have no rights to use or access this software in any manner.
#
# If not covered by the applicable NVIDIA software license agreement:
# NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOFTWARE FOR ANY PURPOSE.
# IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY KIND.
# NVIDIA DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
# IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDI, INCIDENTAL, OR CONSEQUENTIAL DAMAGES,
# OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOURCE CODE.
#
# U.S. Government End Users.
# This software is a "commercial item" as that term is defined at 48 C.F.R. 2.101 (OCT 1995),
# consisting of "commercial computer software" and "commercial computer software documentation"
# as such terms are used in 48 C.F.R. 12.212 (SEPT 1995) and is provided to the U.S. Government only as a commercial
# end item.
# Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through 227.7202-4 (JUNE 1995),
# all U.S. Government End Users acquire the software with only those rights set forth herein.
#
# Any use of this software in individual and commercial software must include,
# in the user documentation and internal comments to the code,
# the above Disclaimer (as applicable) and U.S. Government End Users Notice.
#
# **********************************************************************************************************************

import ctypes
import comtypes
from comtypes.GUID import GUID

from ctypes.wintypes import (
    BOOL,
    UINT,
    INT,
    FLOAT,
    BYTE,
    LPCSTR,
    LPSTR,
    HANDLE,
    RECT,
    LPCWSTR,
    DWORD,
    USHORT,
    SIZE,
    LARGE_INTEGER,
    LONG,
    WCHAR,
    HDC,
    HWND,
    HMODULE,
    CHAR,
    LPCVOID,
    LPVOID,
    POINT
)


COMMETHOD = comtypes.COMMETHOD
POINTER = ctypes.POINTER
helpstring = comtypes.helpstring
VOID = ctypes.c_void_p
HRESULT = ctypes.c_long
UINT8 = ctypes.c_uint8
MIDL_INTERFACE = GUID
REFGUID = POINTER(GUID)
REFIID = POINTER(GUID)
SIZE_T = ctypes.c_size_t
UINT64 = ctypes.c_uint64
D3D10_RECT = RECT
UINT16 = ctypes.c_uint16
ULONGLONG = ctypes.c_ulonglong
INT8 = ctypes.c_int8
UINT32 = ctypes.c_uint32


if ctypes.sizeof(ctypes.c_void_p) == 8:
    LONG_PTR = ctypes.c_longlong
else:
    LONG_PTR = ctypes.c_long


class ENUM(INT):
    # ctypes simple types (this wraps c_int) compare by identity, not
    # value, by default -- "status == NVAPI_OK" style checks throughout
    # this codebase were silently always-false/always-true regardless of
    # the actual returned value. Comparing by .value fixes every call site
    # that checks a returned NvAPI_Status (or any other ENUM-typed field)
    # against a constant, without needing to touch each individual check.
    def __eq__(self, other):
        if isinstance(other, ENUM):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __hash__(self):
        return hash(self.value)

    def __index__(self):
        # needed for "%d" % status style formatting, used throughout this
        # codebase's own error-raising code (e.g.
        # "returned %s (%d)" % (szDesc, nvStatus)) -- without __index__,
        # %d can't convert an ENUM instance at all, which was turning
        # real driver errors into an unrelated TypeError and hiding the
        # actual failure reason.
        return self.value

    def __int__(self):
        return self.value

    @classmethod
    def get(cls, val):
        for value in cls.__dict__.values():
            if value == val:
                return value


class EnumItem(int):
    def __init__(self, value):
        try:
            int.__init__(self, value)
        except TypeError:
            int.__init__(self)

        self.__str_val = ''

    def __eq__(self, other):
        if isinstance(other, int):
            return int.__eq__(self, other)
        if isinstance(other, ENUM):
            return int(self) == other.value

        return self.__str_val == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.__str_val

    def __repr__(self):
        # tuple/namedtuple repr (and anything else nesting an EnumItem)
        # always calls repr() on its elements, never str() -- without this,
        # an enum value shown bare (print(x)) displays its friendly name via
        # __str__, but the exact same value nested inside a namedtuple
        # falls back to plain int.__repr__ and shows just the raw number.
        # The underlying int is still fully accessible either way (this
        # class subclasses int); only the display differs.
        return self.__str_val if self.__str_val else int.__repr__(self)

    def set_string(self, value):
        self.__str_val = value
        return self


__all__ = (
    'BOOL',
    'UINT',
    'INT',
    'FLOAT',
    'BYTE',
    'LPCSTR',
    'LPSTR',
    'HANDLE',
    'RECT',
    'LPCWSTR',
    'DWORD',
    'USHORT',
    'SIZE',
    'LARGE_INTEGER',
    'LONG',
    'WCHAR',
    'HDC',
    'HWND',
    'HMODULE',
    'CHAR',
    'LPCVOID',
    'LPVOID',
    'COMMETHOD',
    'POINTER',
    'helpstring',
    'VOID',
    'HRESULT',
    'UINT8',
    'MIDL_INTERFACE',
    'REFIID',
    'REFGUID',
    'SIZE_T',
    'UINT64',
    'D3D10_RECT',
    'UINT16',
    'ULONGLONG',
    'INT8',
    'UINT32',
    'LONG_PTR',
    'POINT',
    'ENUM',
    'EnumItem',
    'comtypes',
    'GUID',
    'ctypes'
)
