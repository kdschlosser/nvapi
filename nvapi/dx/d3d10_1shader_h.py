import ctypes
import comtypes
from comtypes.GUID import GUID
from ctypes.wintypes import (
    INT,
    UINT,
    FLOAT,
    LPCSTR,
    BOOL
)


class ENUM(INT):
    pass


COMMETHOD = comtypes.COMMETHOD
POINTER = ctypes.POINTER
helpstring = comtypes.helpstring
VOID = ctypes.c_void_p


class _D3D10_SHADER_DEBUG_TOKEN_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_TOKEN_INFO = _D3D10_SHADER_DEBUG_TOKEN_INFO


class _D3D10_SHADER_DEBUG_VAR_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_VAR_INFO = _D3D10_SHADER_DEBUG_VAR_INFO


class _D3D10_SHADER_DEBUG_INPUT_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_INPUT_INFO = _D3D10_SHADER_DEBUG_INPUT_INFO


class _D3D10_SHADER_DEBUG_SCOPEVAR_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_SCOPEVAR_INFO = _D3D10_SHADER_DEBUG_SCOPEVAR_INFO


class _D3D10_SHADER_DEBUG_SCOPE_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_SCOPE_INFO = _D3D10_SHADER_DEBUG_SCOPE_INFO


class _D3D10_SHADER_DEBUG_OUTPUTVAR(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_OUTPUTVAR = _D3D10_SHADER_DEBUG_OUTPUTVAR


class _D3D10_SHADER_DEBUG_OUTPUTREG_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_OUTPUTREG_INFO = _D3D10_SHADER_DEBUG_OUTPUTREG_INFO


class _D3D10_SHADER_DEBUG_INST_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_INST_INFO = _D3D10_SHADER_DEBUG_INST_INFO


class _D3D10_SHADER_DEBUG_FILE_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_FILE_INFO = _D3D10_SHADER_DEBUG_FILE_INFO


class _D3D10_SHADER_DEBUG_INFO(ctypes.Structure):
    pass


D3D10_SHADER_DEBUG_INFO = _D3D10_SHADER_DEBUG_INFO


# ////////////////////////////////////////////////////////////////////////////
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  D3D10_1Shader.h
# Content: D3D10.1 Shader Types and APIs
# ////////////////////////////////////////////////////////////////////////////

from .d3d10shader_h import *  # NOQA


# ----------------------------------------------------------------------
# Shader debugging structures
# ----------------------------------------------------------------------
class _D3D10_SHADER_DEBUG_REGTYPE(ENUM):
    D3D10_SHADER_DEBUG_REG_INPUT = 1
    D3D10_SHADER_DEBUG_REG_OUTPUT = 2
    D3D10_SHADER_DEBUG_REG_CBUFFER = 3
    D3D10_SHADER_DEBUG_REG_TBUFFER = 4
    D3D10_SHADER_DEBUG_REG_TEMP = 5
    D3D10_SHADER_DEBUG_REG_TEMPARRAY = 6
    D3D10_SHADER_DEBUG_REG_TEXTURE = 7
    D3D10_SHADER_DEBUG_REG_SAMPLER = 8
    D3D10_SHADER_DEBUG_REG_IMMEDIATECBUFFER = 9
    D3D10_SHADER_DEBUG_REG_LITERAL = 10
    D3D10_SHADER_DEBUG_REG_UNUSED = 11
    D3D11_SHADER_DEBUG_REG_INTERFACE_POINTERS = 12
    D3D11_SHADER_DEBUG_REG_UAV = 13
    D3D10_SHADER_DEBUG_REG_FORCE_DWORD = 0x7FFFFFFF


D3D10_SHADER_DEBUG_REGTYPE = _D3D10_SHADER_DEBUG_REGTYPE


class _D3D10_SHADER_DEBUG_SCOPETYPE(ENUM):
    D3D10_SHADER_DEBUG_SCOPE_GLOBAL = 1
    D3D10_SHADER_DEBUG_SCOPE_BLOCK = 2
    D3D10_SHADER_DEBUG_SCOPE_FORLOOP = 3
    D3D10_SHADER_DEBUG_SCOPE_STRUCT = 4
    D3D10_SHADER_DEBUG_SCOPE_FUNC_PARAMS = 5
    D3D10_SHADER_DEBUG_SCOPE_STATEBLOCK = 6
    D3D10_SHADER_DEBUG_SCOPE_NAMESPACE = 7
    D3D10_SHADER_DEBUG_SCOPE_ANNOTATION = 8
    D3D10_SHADER_DEBUG_SCOPE_FORCE_DWORD = 0x7FFFFFFF


D3D10_SHADER_DEBUG_SCOPETYPE = _D3D10_SHADER_DEBUG_SCOPETYPE


class _D3D10_SHADER_DEBUG_VARTYPE(ENUM):
    D3D10_SHADER_DEBUG_VAR_VARIABLE = 1
    D3D10_SHADER_DEBUG_VAR_FUNCTION = 2
    D3D10_SHADER_DEBUG_VAR_FORCE_DWORD = 0x7FFFFFFF


D3D10_SHADER_DEBUG_VARTYPE = _D3D10_SHADER_DEBUG_VARTYPE

# ///////////////////////////////////////////////////////////////////
# These are the serialized structures that get written to the file
# ///////////////////////////////////////////////////////////////////
_D3D10_SHADER_DEBUG_TOKEN_INFO._fields_ = [
    # offset into file list
    ('File', UINT),
    # line
    ('Line', UINT),
    # column
    ('Column', UINT),
    ('TokenLength', UINT),
    # offset to LPCSTR of length TokenLength in string datastore
    ('TokenId', UINT),
]

# Variable list
_D3D10_SHADER_DEBUG_VAR_INFO._fields_ = [
    # Index into token list for declaring identifier
    ('TokenId', UINT),
    ('Type', D3D10_SHADER_VARIABLE_TYPE),
    # register and component for this variable, only valid/necessary for
    # arrays
    ('Register', UINT),
    ('Component', UINT),
    # gives the original variable that declared this variable
    ('ScopeVar', UINT),
    # this variable's offset in its ScopeVar
    ('ScopeVarOffset', UINT),
]

_D3D10_SHADER_DEBUG_INPUT_INFO._fields_ = [
    # index into array of variables of variable to initialize
    ('Var', UINT),
    # input, cbuffer, tbuffer
    ('InitialRegisterSet', D3D10_SHADER_DEBUG_REGTYPE),
    # identifying register for indexable temp, or -1
    ('InitialBank', UINT),
    # -1 if temp, otherwise gives register in register set
    ('InitialRegister', UINT),
    # -1 if temp, otherwise gives component
    ('InitialComponent', UINT),
    # initial value if literal
    ('InitialValue', UINT),
]

_D3D10_SHADER_DEBUG_SCOPEVAR_INFO._fields_ = [
    # Index into variable token
    ('TokenId', UINT),
    # variable or function (different namespaces)
    ('VarType', D3D10_SHADER_DEBUG_VARTYPE),
    ('Class', D3D10_SHADER_VARIABLE_CLASS),
    # number of rows (matrices)
    ('Rows', UINT),
    # number of columns (vectors and matrices)
    ('Columns', UINT),
    # gives a scope to look up struct members. -1 if not a struct
    ('StructMemberScope', UINT),
    # a[3][2][1] has 3 indices
    ('uArrayIndices', UINT),
    # a[3][2][1] has {3, 2, 1}
    ('ArrayElements', UINT),
    # a[3][2][1] has {2, 1, 1}
    ('ArrayStrides', UINT),
    ('uVariables', UINT),
    # index of the first variable, later variables are offsets from this
    # one
    ('uFirstVariable', UINT),
]

# scope data, this maps variable names to debug variables
# (useful for the watch window)
_D3D10_SHADER_DEBUG_SCOPE_INFO._fields_ = [
    ('ScopeType', D3D10_SHADER_DEBUG_SCOPETYPE),
    # offset to name of scope in strings list
    ('Name', UINT),
    # length of name string
    ('uNameLen', UINT),
    ('uVariables', UINT),
    # Offset to UINT[uVariables] indexing the Scope Variable list
    ('VariableData', UINT),
]

# instruction outputs
_D3D10_SHADER_DEBUG_OUTPUTVAR._fields_ = [
    # index variable being written to, if -1 it's not going to a variable
    ('Var', UINT),
    # range data that the compiler expects to be true
    ('uValueMin', UINT),
    # range data that the compiler expects to be true
    ('uValueMax', UINT),
    ('iValueMin', INT),
    ('iValueMax', INT),
    ('fValueMin', FLOAT),
    ('fValueMax', FLOAT),
    ('bNaNPossible', BOOL),
    ('bInfPossible', BOOL),
]


_D3D10_SHADER_DEBUG_OUTPUTREG_INFO._fields_ = [
    # Only temp, indexable temp, and output are valid here
    ('OutputRegisterSet', D3D10_SHADER_DEBUG_REGTYPE),
    # -1 means no output
    ('OutputReg', UINT),
    # if a temp array, identifier for which one
    ('TempArrayReg', UINT),
    # -1 means masked out
    ('OutputComponents', UINT * 4),
    ('OutputVars', D3D10_SHADER_DEBUG_OUTPUTVAR * 4),
    # temps and outputs.
    ('IndexReg', UINT),
    ('IndexComp', UINT),
]

# per instruction data
_D3D10_SHADER_DEBUG_INST_INFO._fields_ = [
    # Which instruction this is in the bytecode
    ('Id', UINT),
    # instruction type
    ('Opcode', UINT),
    # 0, 1, or 2
    ('uOutputs', UINT),
    # up to two outputs per instruction
    ('pOutputs', D3D10_SHADER_DEBUG_OUTPUTREG_INFO * 2),
    # index into the list of tokens for this instruction's token
    ('TokenId', UINT),
    # how many function calls deep this instruction is
    ('NestingLevel', UINT),
    # Number of scopes
    ('Scopes', UINT),
    # Offset to UINT[uScopes] specifying indices of the ScopeInfo Array
    ('ScopeInfo', UINT),
    # Number of variables
    ('AccessedVars', UINT),
    # Offset to UINT[AccessedVars] specifying indices of the
    # ScopeVariableInfo Array
    ('AccessedVarsInfo', UINT),
]

_D3D10_SHADER_DEBUG_FILE_INFO._fields_ = [
    # Offset to LPCSTR for file name
    ('FileName', UINT),
    # Length of file name
    ('FileNameLen', UINT),
    # Offset to LPCSTR of length FileLen
    ('FileData', UINT),
    # Length of file
    ('FileLen', UINT),
]

_D3D10_SHADER_DEBUG_INFO._fields_ = [
    # (ctypes.sizeof(D3D10_SHADER_DEBUG_INFO)
    ('Size', UINT),
    # Offset to LPCSTR for compiler version
    ('Creator', UINT),
    # Offset to LPCSTR for Entry point name
    ('EntrypointName', UINT),
    # Offset to LPCSTR for shader target
    ('ShaderTarget', UINT),
    # flags used to compile
    ('CompileFlags', UINT),
    # number of included files
    ('Files', UINT),
    # Offset to D3D10_SHADER_DEBUG_FILE_INFO[Files]
    ('FileInfo', UINT),
    # number of instructions
    ('Instructions', UINT),
    # Offset to D3D10_SHADER_DEBUG_INST_INFO[Instructions]
    ('InstructionInfo', UINT),
    # number of variables
    ('Variables', UINT),
    # Offset to D3D10_SHADER_DEBUG_VAR_INFO[Variables]
    ('VariableInfo', UINT),
    # number of variables to initialize before running
    ('InputVariables', UINT),
    # Offset to D3D10_SHADER_DEBUG_INPUT_INFO[InputVariables]
    ('InputVariableInfo', UINT),
    # number of tokens to initialize
    ('Tokens', UINT),
    # Offset to D3D10_SHADER_DEBUG_TOKEN_INFO[Tokens]
    ('TokenInfo', UINT),
    # number of scopes
    ('Scopes', UINT),
    # Offset to D3D10_SHADER_DEBUG_SCOPE_INFO[Scopes]
    ('ScopeInfo', UINT),
    # number of variables declared
    ('ScopeVariables', UINT),
    # Offset to D3D10_SHADER_DEBUG_SCOPEVAR_INFO[Scopes]
    ('ScopeVariableInfo', UINT),
    # Offset to the UINT datastore, all UINT offsets are from this offset
    ('UintOffset', UINT),
    # Offset to the string datastore, all string offsets are from this
    # offset
    ('StringOffset', UINT),
]
# ----------------------------------------------------------------------
# ID3D10ShaderReflection1:
# ----------------------------------------------------------------------
# Interface definitions

# {C3457783-A846-47CE-9520-CEA6F66E7447}
IID_ID3D10ShaderReflection1 = GUID(
    '{C3457783-A846-47CE-9520-CEA6F66E7447}'
)


class ID3D10ShaderReflection1(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_ID3D10ShaderReflection1


LPD3D10SHADERREFLECTION1 = POINTER(ID3D10ShaderReflection1)

ID3D10ShaderReflection1._methods_ = [
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_SHADER_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionConstantBuffer),
        'GetConstantBufferByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionConstantBuffer),
        'GetConstantBufferByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetResourceBindingDesc',
        (UINT, POINTER(D3D10_SHADER_INPUT_BIND_DESC))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetInputParameterDesc',
        (UINT, POINTER(D3D10_SIGNATURE_PARAMETER_DESC))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetOutputParameterDesc',
        (UINT, POINTER(D3D10_SIGNATURE_PARAMETER_DESC))
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionVariable),
        'GetVariableByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetResourceBindingDescByName',
        (LPCSTR, POINTER(D3D10_SHADER_INPUT_BIND_DESC))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetMovInstructionCount',
        (POINTER(UINT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetMovcInstructionCount',
        (POINTER(UINT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetConversionInstructionCount',
        (POINTER(UINT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBitwiseInstructionCount',
        (POINTER(UINT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetGSInputPrimitive',
        (POINTER(D3D10_PRIMITIVE),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'IsLevel9Shader',
        (POINTER(BOOL),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'IsSampleFrequencyShader',
        (POINTER(BOOL),)
    ),
]


