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
    RECT
)

UINT8 = ctypes.c_uint8
COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring
POINTER = ctypes.POINTER
VOID = ctypes.c_void_p
MIDL_INTERFACE = GUID
REFIID = POINTER(GUID)
SIZE_T = ctypes.c_size_t
REFGUID = POINTER(GUID)
HRESULT = ctypes.c_long
UINT64 = ctypes.c_uint64
D3D10_RECT = RECT
D3D10_IGNORE_SDK_LAYERS = None


class ENUM(INT):
    pass


class _D3D10_SHADER_DESC(ctypes.Structure):
    pass


D3D10_SHADER_DESC = _D3D10_SHADER_DESC


class _D3D10_SHADER_BUFFER_DESC(ctypes.Structure):
    pass


D3D10_SHADER_BUFFER_DESC = _D3D10_SHADER_BUFFER_DESC


class _D3D10_SHADER_VARIABLE_DESC(ctypes.Structure):
    pass


D3D10_SHADER_VARIABLE_DESC = _D3D10_SHADER_VARIABLE_DESC


class _D3D10_SHADER_TYPE_DESC(ctypes.Structure):
    pass


D3D10_SHADER_TYPE_DESC = _D3D10_SHADER_TYPE_DESC


class _D3D10_SHADER_INPUT_BIND_DESC(ctypes.Structure):
    pass


D3D10_SHADER_INPUT_BIND_DESC = _D3D10_SHADER_INPUT_BIND_DESC


class _D3D10_SIGNATURE_PARAMETER_DESC(ctypes.Structure):
    pass


D3D10_SIGNATURE_PARAMETER_DESC = _D3D10_SIGNATURE_PARAMETER_DESC




# ////////////////////////////////////////////////////////////////////////////
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  D3D10Shader.h
# Content: D3D10 Shader Types and APIs
# ////////////////////////////////////////////////////////////////////////////
from .d3d10_h import *  # NOQA
# -----------------------------------------------------------------
# D3D10_TX_VERSION:
# --------------
# Version token used to create a procedural texture filler in effects
# Used by D3D10Fill[]TX functions
# -----------------------------------------------------------------
def D3D10_TX_VERSION(_Major, _Minor):
    return (ord('T') << 24) | (ord('X') << 16) | (_Major << 8) | _Minor

# ------------------------------------------------------------------
# D3D10SHADER flags:
# -----------------
# D3D10_SHADER_DEBUG
# Insert debug file/line/type/symbol information.
# D3D10_SHADER_SKIP_VALIDATION
# Do not validate the generated code against known capabilities and
# constraints. This option is only recommended when compiling shaders
# you KNOW will work. (ie. have compiled before without this option.)
# Shaders are always validated by D3D before they are set to the
# device.
# D3D10_SHADER_SKIP_OPTIMIZATION
# Instructs the compiler to skip optimization steps during code
# generation.
# Unless you are trying to isolate a problem in your code using this
# option
# is not recommended.
# D3D10_SHADER_PACK_MATRIX_ROW_MAJOR
# Unless explicitly specified, matrices will be packed in row-major
# order
# on input and output from the shader.
# D3D10_SHADER_PACK_MATRIX_COLUMN_MAJOR
# Unless explicitly specified, matrices will be packed in column-major
# order on input and output from the shader. This is generally more
# efficient, since it allows vector-matrix multiplication to be
# performed
# using a series of dot-products.
# D3D10_SHADER_PARTIAL_PRECISION
# Force all computations in resulting shader to occur at partial
# precision.
# This may result in faster evaluation of shaders on some hardware.
# D3D10_SHADER_FORCE_VS_SOFTWARE_NO_OPT
# Force compiler to compile against the next highest available software
# target for vertex shaders. This flag also turns optimizations off,
# and debugging on.
# D3D10_SHADER_FORCE_PS_SOFTWARE_NO_OPT
# Force compiler to compile against the next highest available software
# target for pixel shaders. This flag also turns optimizations off,
# and debugging on.
# D3D10_SHADER_NO_PRESHADER
# Disables Preshaders. Using this flag will cause the compiler to not
# pull out static expression for evaluation on the host cpu
# D3D10_SHADER_AVOID_FLOW_CONTROL
# Hint compiler to avoid flow-control constructs where possible.
# D3D10_SHADER_PREFER_FLOW_CONTROL
# Hint compiler to prefer flow-control constructs where possible.
# D3D10_SHADER_ENABLE_STRICTNESS
# By default, the HLSL/Effect compilers are not strict on deprecated
# syntax.
# Specifying this flag enables the strict mode. Deprecated syntax may
# be
# removed in a future release, and enabling syntax is a good way to
# make sure
# your shaders comply to the latest spec.
# D3D10_SHADER_ENABLE_BACKWARDS_COMPATIBILITY
# This enables older shaders to compile to 4_0 targets.
# ------------------------------------------------------------------
D3D10_SHADER_DEBUG = 1 << 0
D3D10_SHADER_SKIP_VALIDATION = 1 << 1
D3D10_SHADER_SKIP_OPTIMIZATION = 1 << 2
D3D10_SHADER_PACK_MATRIX_ROW_MAJOR = 1 << 3
D3D10_SHADER_PACK_MATRIX_COLUMN_MAJOR = 1 << 4
D3D10_SHADER_PARTIAL_PRECISION = 1 << 5
D3D10_SHADER_FORCE_VS_SOFTWARE_NO_OPT = 1 << 6
D3D10_SHADER_FORCE_PS_SOFTWARE_NO_OPT = 1 << 7
D3D10_SHADER_NO_PRESHADER = 1 << 8
D3D10_SHADER_AVOID_FLOW_CONTROL = 1 << 9
D3D10_SHADER_PREFER_FLOW_CONTROL = 1 << 10
D3D10_SHADER_ENABLE_STRICTNESS = 1 << 11
D3D10_SHADER_ENABLE_BACKWARDS_COMPATIBILITY = 1 << 12
D3D10_SHADER_IEEE_STRICTNESS = 1 << 13
D3D10_SHADER_WARNINGS_ARE_ERRORS = 1 << 18
D3D10_SHADER_RESOURCES_MAY_ALIAS = 1 << 19
D3D10_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES = 1 << 20
D3D10_ALL_RESOURCES_BOUND = 1 << 21
D3D10_SHADER_DEBUG_NAME_FOR_SOURCE = 1 << 22
D3D10_SHADER_DEBUG_NAME_FOR_BINARY = 1 << 23

# optimization level flags
D3D10_SHADER_OPTIMIZATION_LEVEL0 = 1 << 14
D3D10_SHADER_OPTIMIZATION_LEVEL1 = 0
D3D10_SHADER_OPTIMIZATION_LEVEL2 = (1 << 14) | (1 << 15)
D3D10_SHADER_OPTIMIZATION_LEVEL3 = 1 << 15

# Force root signature flags. (Passed in Flags2)
D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_LATEST = 0
D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_1_0 = 1 << 4
D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_1_1 = 1 << 5
D3D10_SHADER_MACRO = D3D_SHADER_MACRO
LPD3D10_SHADER_MACRO = POINTER(D3D10_SHADER_MACRO)
D3D10_SHADER_VARIABLE_CLASS = D3D_SHADER_VARIABLE_CLASS
LPD3D10_SHADER_VARIABLE_CLASS = POINTER(D3D10_SHADER_VARIABLE_CLASS)
D3D10_SHADER_VARIABLE_FLAGS = D3D_SHADER_VARIABLE_FLAGS
LPD3D10_SHADER_VARIABLE_FLAGS = POINTER(D3D10_SHADER_VARIABLE_FLAGS)
D3D10_SHADER_VARIABLE_TYPE = D3D_SHADER_VARIABLE_TYPE
LPD3D10_SHADER_VARIABLE_TYPE = POINTER(D3D10_SHADER_VARIABLE_TYPE)
D3D10_SHADER_INPUT_FLAGS = D3D_SHADER_INPUT_FLAGS
LPD3D10_SHADER_INPUT_FLAGS = POINTER(D3D10_SHADER_INPUT_FLAGS)
D3D10_SHADER_INPUT_TYPE = D3D_SHADER_INPUT_TYPE
LPD3D10_SHADER_INPUT_TYPE = POINTER(D3D10_SHADER_INPUT_TYPE)
D3D10_SHADER_CBUFFER_FLAGS = D3D_SHADER_CBUFFER_FLAGS
LPD3D10_SHADER_CBUFFER_FLAGS = POINTER(D3D10_SHADER_CBUFFER_FLAGS)
D3D10_CBUFFER_TYPE = D3D_CBUFFER_TYPE
LPD3D10_CBUFFER_TYPE = POINTER(D3D10_CBUFFER_TYPE)
D3D10_NAME = D3D_NAME
D3D10_RESOURCE_RETURN_TYPE = D3D_RESOURCE_RETURN_TYPE
D3D10_REGISTER_COMPONENT_TYPE = D3D_REGISTER_COMPONENT_TYPE
D3D10_INCLUDE_TYPE = D3D_INCLUDE_TYPE

# ID3D10Include has been made version-neutral and moved to d3dcommon.h.

class ID3D10Include(ID3DInclude):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


LPD3D10INCLUDE = POINTER(ID3DInclude)


# ------------------------------------------------------------------
# ID3D10ShaderReflection:
# ------------------------------------------------------------------
# Structure definitions
_D3D10_SHADER_DESC._fields_ = [
    # Shader version
    ('Version', UINT),
    # Creator string
    ('Creator', LPCSTR),
    # Shader compilation/parse flags
    ('Flags', UINT),
    # Number of constant buffers
    ('ConstantBuffers', UINT),
    # Number of bound resources
    ('BoundResources', UINT),
    # Number of parameters in the input signature
    ('InputParameters', UINT),
    # Number of parameters in the output signature
    ('OutputParameters', UINT),
    # Number of emitted instructions
    ('InstructionCount', UINT),
    # Number of temporary registers used
    ('TempRegisterCount', UINT),
    # Number of temporary arrays used
    ('TempArrayCount', UINT),
    # Number of constant defines
    ('DefCount', UINT),
    # Number of declarations (input + output)
    ('DclCount', UINT),
    # Number of non-categorized texture instructions
    ('TextureNormalInstructions', UINT),
    # Number of texture load instructions
    ('TextureLoadInstructions', UINT),
    # Number of texture comparison instructions
    ('TextureCompInstructions', UINT),
    # Number of texture bias instructions
    ('TextureBiasInstructions', UINT),
    # Number of texture gradient instructions
    ('TextureGradientInstructions', UINT),
    # Number of floating point arithmetic instructions used
    ('FloatInstructionCount', UINT),
    # Number of INT integer arithmetic instructions used
    ('IntInstructionCount', UINT),
    # Number of UINT integer arithmetic instructions used
    ('UintInstructionCount', UINT),
    # Number of static flow control instructions used
    ('StaticFlowControlCount', UINT),
    # Number of dynamic flow control instructions used
    ('DynamicFlowControlCount', UINT),
    # Number of macro instructions used
    ('MacroInstructionCount', UINT),
    # Number of array instructions used
    ('ArrayInstructionCount', UINT),
    # Number of cut instructions used
    ('CutInstructionCount', UINT),
    # Number of emit instructions used
    ('EmitInstructionCount', UINT),
    # Geometry shader output topology
    ('GSOutputTopology', D3D10_PRIMITIVE_TOPOLOGY),
    # Geometry shader maximum output vertex count
    ('GSMaxOutputVertexCount', UINT),
]

_D3D10_SHADER_BUFFER_DESC._fields_ = [
    # Name of the constant buffer
    ('Name', LPCSTR),
    # Indicates that this is a CBuffer or TBuffer
    ('Type', D3D10_CBUFFER_TYPE),
    # Number of member variables
    ('Variables', UINT),
    # Size of CB (in bytes)
    ('Size', UINT),
    # Buffer description flags
    ('uFlags', UINT),
]

_D3D10_SHADER_VARIABLE_DESC._fields_ = [
    # Name of the variable
    ('Name', LPCSTR),
    # Offset in constant buffer's backing store
    ('StartOffset', UINT),
    # Size of variable (in bytes)
    ('Size', UINT),
    # Variable flags
    ('uFlags', UINT),
    # Raw pointer to default value
    ('DefaultValue', LPVOID),
]

_D3D10_SHADER_TYPE_DESC._fields_ = [
    # Variable class (e.g. object, matrix, etc.)
    ('Class', D3D10_SHADER_VARIABLE_CLASS),
    # Variable type (e.g. float, sampler, etc.)
    ('Type', D3D10_SHADER_VARIABLE_TYPE),
    # Number of rows
    # (for matrices, 1 for other numeric, 0 if not applicable)
    ('Rows', UINT),
    # Number of columns
    # (for vectors & matrices, 1 for other numeric, 0 if not applicable)
    # 
    ('Columns', UINT),
    # Number of elements (0 if not an array)
    ('Elements', UINT),
    # Number of members (0 if not a structure)
    ('Members', UINT),
    # Offset from the start of structure (0 if not a structure member)
    ('Offset', UINT),
]

_D3D10_SHADER_INPUT_BIND_DESC._fields_ = [
    # Name of the resource
    ('Name', LPCSTR),
    # Type of resource (e.g. texture, cbuffer, etc.)
    ('Type', D3D10_SHADER_INPUT_TYPE),
    # Starting bind point
    ('BindPoint', UINT),
    # Number of contiguous bind points (for arrays)
    ('BindCount', UINT),
    # Input binding flags
    ('uFlags', UINT),
    # Return type (if texture)
    ('ReturnType', D3D10_RESOURCE_RETURN_TYPE),
    # Dimension (if texture)
    ('Dimension', D3D10_SRV_DIMENSION),
    # Number of samples (0 if not MS texture)
    ('NumSamples', UINT),
]

_D3D10_SIGNATURE_PARAMETER_DESC._fields_ = [
    # Name of the semantic
    ('SemanticName', LPCSTR),
    # Index of the semantic
    ('SemanticIndex', UINT),
    # Number of member variables
    ('Register', UINT),
    # A predefined system value, or D3D10_NAME_UNDEFINED if not
    # applicable
    ('SystemValueType', D3D10_NAME),
    # Scalar type (e.g. uint, float, etc.)
    ('ComponentType', D3D10_REGISTER_COMPONENT_TYPE),
    # Mask to indicate which components of the register
    ('Mask', BYTE),
    # Mask to indicate whether a given component is
    ('ReadWriteMask', BYTE),
]


# Interface definitions
class ID3D10ShaderReflectionType(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


LPD3D10SHADERREFLECTIONTYPE = POINTER(ID3D10ShaderReflectionType)

# {C530AD7D-9B16-4395-A979-BA2ECFF83ADD}
IID_ID3D10ShaderReflectionType = GUID(
    '{C530AD7D-9B16-4395-A979-BA2ECFF83ADD}'
)

ID3D10ShaderReflectionType._methods_ = [
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_SHADER_TYPE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionType),
        'GetMemberTypeByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionType),
        'GetMemberTypeByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        LPCSTR,
        'GetMemberTypeName',
        (UINT,)
    ),
]


class ID3D10ShaderReflectionVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


LPD3D10SHADERREFLECTIONVARIABLE = POINTER(ID3D10ShaderReflectionVariable)


# {1BF63C95-2650-405d-99C1-3636BD1DA0A1}
IID_ID3D10ShaderReflectionVariable = GUID(
    '{1BF63C95-2650-405d-99C1-3636BD1DA0A1}'
)

ID3D10ShaderReflectionVariable._methods_ = [
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_SHADER_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionType),
        'GetType',
        ()
    ),
]


class ID3D10ShaderReflectionConstantBuffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


LPD3D10SHADERREFLECTIONCONSTANTBUFFER = POINTER(ID3D10ShaderReflectionConstantBuffer)


# {66C66A94-DDDD-4b62-A66A-F0DA33C2B4D0}
IID_ID3D10ShaderReflectionConstantBuffer = GUID(
    '{66C66A94-DDDD-4b62-A66A-F0DA33C2B4D0}'
)

ID3D10ShaderReflectionConstantBuffer._methods_ = [
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_SHADER_BUFFER_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionVariable),
        'GetVariableByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10ShaderReflectionVariable),
        'GetVariableByName',
        (LPCSTR,)
    ),
]


class ID3D10ShaderReflection(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


LPD3D10SHADERREFLECTION = POINTER(ID3D10ShaderReflection)

# {D40E20B6-F8F7-42ad-AB20-4BAF8F15DFAA}
IID_ID3D10ShaderReflection = GUID(
    '{D40E20B6-F8F7-42ad-AB20-4BAF8F15DFAA}'
)

ID3D10ShaderReflection._methods_ = [
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
]

# //////////////////////////////////////////////////////////////////
# APIs
# ////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# ------------------------------------------------------------------
# D3D10CompileShader:
# ------------------
# Compiles a shader.
# Parameters:
# pSrcFile
# Source file name.
# hSrcModule
# Module handle. if NULL, current module will be used.
# pSrcResource
# Resource name in module.
# pSrcData
# Pointer to source code.
# SrcDataSize
# Size of source code, in bytes.
# pDefines
# Optional NULL-terminated array of preprocessor macro definitions.
# pInclude
# Optional interface pointer to use for handling include directives.
# If this parameter is NULL, includes will be honored when compiling
# from file, and will error when compiling from resource or memory.
# pFunctionName
# Name of the entrypoint function where execution should begin.
# pProfile
# Instruction set to be used when generating code. The D3D10 entry
# point currently supports only "vs_4_0", "ps_4_0", and "gs_4_0".
# Flags
# See D3D10_SHADER_xxx flags.
# ppShader
# Returns a buffer containing the created shader. This buffer contains
# the compiled shader code, as well as any embedded debug and symbol
# table info. (See D3D10GetShaderConstantTable)
# ppErrorMsgs
# Returns a buffer containing a listing of errors and warnings that
# were
# encountered during the compile. If you are running in a debugger,
# these are the same messages you will see in your debug output.
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# D3D10DisassembleShader:
# ----------------------
# Takes a binary shader, and returns a buffer containing text assembly.
# Parameters:
# pShader
# Pointer to the shader byte code.
# BytecodeLength
# Size of the shader byte code in bytes.
# EnableColorCode
# Emit HTML tags for color coding the output?
# pComments
# Pointer to a comment string to include at the top of the shader.
# ppDisassembly
# Returns a buffer containing the disassembled shader.
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# D3D10GetPixelShaderProfile/D3D10GetVertexShaderProfile/D3D10GetGeometryShaderProfile:
# 
# -----------------------------------------------------
# Returns the name of the HLSL profile best suited to a given device.
# Parameters:
# pDevice
# Pointer to the device in question
# ------------------------------------------------------------------
d3d10 = ctypes.windll.D3D10


# LPCSTR WINAPI D3D10GetPixelShaderProfile(_In_ ID3D10Device *pDevice);
D3D10GetPixelShaderProfile = d3d10.D3D10GetPixelShaderProfile
D3D10GetPixelShaderProfile.restype = LPCSTR


# LPCSTR WINAPI D3D10GetVertexShaderProfile(_In_ ID3D10Device *pDevice);
D3D10GetVertexShaderProfile = d3d10.D3D10GetVertexShaderProfile
D3D10GetVertexShaderProfile.restype = LPCSTR


# LPCSTR WINAPI D3D10GetGeometryShaderProfile(_In_ ID3D10Device *pDevice);
D3D10GetGeometryShaderProfile = d3d10.D3D10GetGeometryShaderProfile
D3D10GetGeometryShaderProfile.restype = LPCSTR

# ------------------------------------------------------------------
# D3D10ReflectShader:
# ------------------
# Creates a shader reflection object that can be used to retrieve
# information
# about a compiled shader
# Parameters:
# pShaderBytecode
# Pointer to a compiled shader (same pointer that is passed into
# ID3D10Device::CreateShader)
# BytecodeLength
# Length of the shader bytecode buffer
# ppReflector
# [out] Returns a ID3D10ShaderReflection object that can be used to
# retrieve shader resource and constant buffer information
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# D3D10PreprocessShader
# ---------------------
# Creates a shader reflection object that can be used to retrieve
# information
# about a compiled shader
# Parameters:
# pSrcData
# Pointer to source code
# SrcDataSize
# Size of source code, in bytes
# pFileName
# Source file name (used for error output)
# pDefines
# Optional NULL-terminated array of preprocessor macro definitions.
# pInclude
# Optional interface pointer to use for handling include directives.
# If this parameter is NULL, includes will be honored when assembling
# from file, and will error when assembling from resource or memory.
# ppShaderText
# Returns a buffer containing a single large string that represents
# the resulting formatted token stream
# ppErrorMsgs
# Returns a buffer containing a listing of errors and warnings that
# were
# encountered during assembly. If you are running in a debugger,
# these are the same messages you will see in your debug output.
# ------------------------------------------------------------------
# //////////////////////////////////////////////////////////////
# Shader blob manipulation routines
# ---------------------------------
# VOID *pShaderBytecode - a buffer containing the result of an HLSL
# compilation. Typically this opaque buffer contains several
# discrete sections including the shader executable code, the input
# signature, and the output signature. This can typically be retrieved
# by calling ID3D10Blob::GetBufferPointer() on the returned blob
# from HLSL's compile APIs.
# UINT BytecodeLength - the length of pShaderBytecode. This can
# typically be retrieved by calling ID3D10Blob::GetBufferSize()
# on the returned blob from HLSL's compile APIs.
# ID3D10Blob **ppSignatureBlob(s) - a newly created buffer that
# contains only the signature portions of the original bytecode.
# This is a copy; the original bytecode is not modified. You may
# specify NULL for this parameter to have the bytecode validated
# for the presence of the corresponding signatures without actually
# copying them and creating a new blob.
# Returns E_INVALIDARG if any required parameters are NULL
# Returns E_FAIL is the bytecode is corrupt or missing signatures
# Returns S_OK on success
# //////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10GetShaderDebugInfo:
# -----------------------
# Gets shader debug info. Debug info is generated by
# D3D10CompileShader and is
# embedded in the body of the shader.
# Parameters:
# pShaderBytecode
# Pointer to the function bytecode
# BytecodeLength
# Length of the shader bytecode buffer
# ppDebugInfo
# Buffer used to return debug info. For information about the layout
# of this buffer, see definition of D3D10_SHADER_DEBUG_INFO above.


