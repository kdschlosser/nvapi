import ctypes


class NvShaderExtnStruct(ctypes.Structure):
    pass


uint = ctypes.c_uint


class uint2(ctypes.Structure):

    _fields_ = [
        ('x', uint),
        ('y', uint)
    ]


class uint3(ctypes.Structure):
    _fields_ = [
        ('x', uint),
        ('y', uint),
        ('z', uint)
    ]


class uint4(ctypes.Structure):
    _fields_ = [
        ('x', uint),
        ('y', uint),
        ('z', uint),
        ('w', uint)
    ]


int = ctypes.c_int


class int2(ctypes.Structure):

    _fields_ = [
        ('x', int),
        ('y', int)
    ]


class int3(ctypes.Structure):
    _fields_ = [
        ('x', int),
        ('y', int),
        ('z', int)
    ]


class int4(ctypes.Structure):
    _fields_ = [
        ('x', int),
        ('y', int),
        ('z', int),
        ('w', int)
    ]


float = ctypes.c_float


class float2(ctypes.Structure):

    _fields_ = [
        ('x', float),
        ('y', float)
    ]


class float3(ctypes.Structure):
    _fields_ = [
        ('x', float),
        ('y', float),
        ('z', float)
    ]


class float4(ctypes.Structure):
    _fields_ = [
        ('x', float),
        ('y', float),
        ('z', float),
        ('w', float)
    ]


def asuint(x):
    try:
        return uint4(x.x, x.y, x.z, x.w)
    except AttributeError:
        pass

    try:
        return uint3(x.x, x.y, x.z)
    except AttributeError:
        pass

    try:
        return uint2(x.x, x.y)
    except AttributeError:
        pass

    return uint(x)


def asfloat(x):
    try:
        return float4(x.x, x.y, x.z, x.w)
    except AttributeError:
        pass

    try:
        return float3(x.x, x.y, x.z)
    except AttributeError:
        pass

    try:
        return float2(x.x, x.y)
    except AttributeError:
        pass

    return float(x)


def f32tof16(x):
    return asuint(x)


#
# ############ NVIDIA SHADER EXTENSIONS ########/
# internal functions
# Functions in this file are not expected to be called by apps directly
from .nvShaderExtnEnums_h import *  # NOQA

NvShaderExtnStruct._fields_ = [
    # opcode
    ('opcode', uint),
    # resource ID
    ('rid', uint),
    # sampler ID
    ('sid', uint),
    # destination operand 1
    # (for instructions that need extra destination operands)
    ('dst1u', uint4),
    # source operand 3
    ('src3u', uint4),
    # source operand 4
    ('src4u', uint4),
    # source operand 5
    ('src5u', uint4),
    # uint source operand 0
    ('src0u', uint4),
    # uint source operand 0
    ('src1u', uint4),
    # uint source operand 0
    ('src2u', uint4),
    # uint destination operand
    ('dst0u', uint4),
    # the next store to UAV is fake and is used only to identify the uav slot
    ('markUavRef', uint),
    # Used for output to IncrementCounter
    ('numOutputsForIncCounter', uint),
    # struct size: 256 bytes
    ('padding1', float * 27),
]


# RW structured buffer for Nvidia shader extensions

# Application needs to define NV_SHADER_EXTN_SLOT as a unused slot, which should be 
# set using NvAPI_D3D11_SetNvShaderExtnSlot() call before creating the first shader that
# uses nvidia shader extensions. E.g before including this file in shader define it as:

# For SM5.1, application needs to define NV_SHADER_EXTN_REGISTER_SPACE as register space
# E.g. before including this file in shader define it as:

# Note that other operations to this UAV will be ignored so application
# should bind a null resource

g_NvidiaExt = NvShaderExtnStruct()
# g_NvidiaExt : register( NV_SHADER_EXTN_SLOT, NV_SHADER_EXTN_REGISTER_SPACE );
# RWStructuredBuffer<NvShaderExtnStruct> g_NvidiaExt : register( NV_SHADER_EXTN_SLOT );


# ----------------------------------------------------------------------------
# the exposed SHFL instructions accept a mask parameter in src2
# To compute lane mask from width of segment:
# minLaneID : currentLaneId & src2[12:8]
# maxLaneID : minLaneId | (src2[4:0] & ~src2[12:8])
# where [minLaneId, maxLaneId] defines the segment where currentLaneId belongs
# we always set src2[4:0] to 11111 (0x1F), and set src2[12:8] as (32 - width)
def _NvGetShflMaskFromWidth(width):
    return ((NV_WARP_SIZE - width) << 8) | 0x1F


# ----------------------------------------------------------------------------
def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav.Store(index, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = float2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = float2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = float2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = float4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = float4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = float4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = float(0.0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = float(0.0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = float(0.0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = uint2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = uint2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = uint2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = uint4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = uint4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = uint4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = int(0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = int(0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = int(0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = int2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = int2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = int2(0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = int4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = int4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = int4(0, 0, 0, 0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[index] = int(0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint2(index, index)] = int(0)


def _NvReferenceUAVForOp(uav):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].markUavRef = 1
    uav[uint3(index, index, index)] = int(0)


# ----------------------------------------------------------------------------
# ATOMIC op sub-opcodes
NV_EXTN_ATOM_AND = 0
NV_EXTN_ATOM_OR = 1
NV_EXTN_ATOM_XOR = 2

NV_EXTN_ATOM_ADD = 3
NV_EXTN_ATOM_MAX = 6
NV_EXTN_ATOM_MIN = 7

NV_EXTN_ATOM_SWAP = 8
NV_EXTN_ATOM_CAS = 9


# ----------------------------------------------------------------------------
# performs Atomic operation on two consecutive fp16 values in the given UAV
# the uint paramater 'fp16x2Val' is treated as two fp16 values
# the passed sub-opcode 'op' should be an immediate constant
# byteAddress must be multiple of 4
# the returned value are the two fp16 values packed into a single uint
def _NvAtomicOpFP16x2(uav, byteAddress, fp16x2Val, atomicOpType):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x = byteAddress
    g_NvidiaExt[index].src1u.x = fp16x2Val
    g_NvidiaExt[index].src2u.x = atomicOpType
    g_NvidiaExt[index].opcode  = NV_EXTN_OP_FP16_ATOMIC

    return g_NvidiaExt[index].dst0u.x


# ----------------------------------------------------------------------------
# performs Atomic operation on a R16G16_FLOAT UAV at the given address
# the uint paramater 'fp16x2Val' is treated as two fp16 values
# the passed sub-opcode 'op' should be an immediate constant
# the returned value are the two fp16 values (.x and .y components) packed into a single uint
# Warning: Behaviour of these set of functions is undefined if the UAV is not 
# of R16G16_FLOAT format (might result in app crash or TDR)
def _NvAtomicOpFP16x2(uav, address, fp16x2Val, atomicOpType):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x    = address
    g_NvidiaExt[index].src1u.x    = fp16x2Val
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC

    return g_NvidiaExt[index].dst0u.x


def _NvAtomicOpFP16x2(uav, address, fp16x2Val, atomicOpType):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xy   = address
    g_NvidiaExt[index].src1u.x    = fp16x2Val
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC

    return g_NvidiaExt[index].dst0u.x

def _NvAtomicOpFP16x2(uav, address, fp16x2Val, atomicOpType):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xyz  = address
    g_NvidiaExt[index].src1u.x    = fp16x2Val
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC

    return g_NvidiaExt[index].dst0u.x


# ----------------------------------------------------------------------------
# performs Atomic operation on a R16G16B16A16_FLOAT UAV at the given address
# the uint2 paramater 'fp16x2Val' is treated as four fp16 values 
# i.e, fp16x2Val.x = uav.xy and fp16x2Val.y = uav.yz
# the passed sub-opcode 'op' should be an immediate constant
# the returned value are the four fp16 values (.xyzw components) packed into uint2
# Warning: Behaviour of these set of functions is undefined if the UAV is not 
# of R16G16B16A16_FLOAT format (might result in app crash or TDR)
def _NvAtomicOpFP16x2(uav, address, fp16x2Val, atomicOpType):
    _NvReferenceUAVForOp(uav)

    # break it down into two fp16x2 atomic ops
    retVal = uint2()

    # first op has x-coordinate = x * 2
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x    = address * 2
    g_NvidiaExt[index].src1u.x    = fp16x2Val.x
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC
    retVal.x = g_NvidiaExt[index].dst0u.x

    # second op has x-coordinate = x * 2 + 1
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x    = address * 2 + 1
    g_NvidiaExt[index].src1u.x    = fp16x2Val.y
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC
    retVal.y = g_NvidiaExt[index].dst0u.x

    return retVal


def _NvAtomicOpFP16x2(uav, address, fp16x2Val, atomicOpType):
    _NvReferenceUAVForOp(uav)

    # break it down into two fp16x2 atomic ops
    retVal = uint2()

    # first op has x-coordinate = x * 2
    addressTemp = uint2(address.x * 2, address.y)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xy   = addressTemp
    g_NvidiaExt[index].src1u.x    = fp16x2Val.x
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC
    retVal.x = g_NvidiaExt[index].dst0u.x

    # second op has x-coordinate = x * 2 + 1
    addressTemp.x += 1
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xy   = addressTemp
    g_NvidiaExt[index].src1u.x    = fp16x2Val.y
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC
    retVal.y = g_NvidiaExt[index].dst0u.x

    return retVal


def _NvAtomicOpFP16x2(uav, address, fp16x2Val, atomicOpType):
    _NvReferenceUAVForOp(uav)

    # break it down into two fp16x2 atomic ops
    retVal = uint2()

    # first op has x-coordinate = x * 2
    addressTemp = uint3(address.x * 2, address.y, address.z)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xyz  = addressTemp
    g_NvidiaExt[index].src1u.x    = fp16x2Val.x
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC
    retVal.x = g_NvidiaExt[index].dst0u.x

    # second op has x-coordinate = x * 2 + 1
    addressTemp.x += 1
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xyz  = addressTemp
    g_NvidiaExt[index].src1u.x    = fp16x2Val.y
    g_NvidiaExt[index].src2u.x    = atomicOpType
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP16_ATOMIC
    retVal.y = g_NvidiaExt[index].dst0u.x

    return retVal


def _fp32x2Tofp16x2(val):
    return (f32tof16(val.y) << 16) | f32tof16(val.x)


def _fp32x4Tofp16x4(val):
    return uint2((f32tof16(val.y) << 16) | f32tof16(val.x), (f32tof16(val.w) << 16) | f32tof16(val.z) )


# ----------------------------------------------------------------------------
# FP32 Atomic functions
# performs Atomic operation treating the uav as float (fp32) values
# the passed sub-opcode 'op' should be an immediate constant
# byteAddress must be multiple of 4
def _NvAtomicAddFP32(uav, byteAddress, val):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x = byteAddress
    g_NvidiaExt[index].src1u.x = asuint(val)   # passing as uint to make it more convinient for the driver to translate
    g_NvidiaExt[index].src2u.x = NV_EXTN_ATOM_ADD
    g_NvidiaExt[index].opcode  = NV_EXTN_OP_FP32_ATOMIC

    return asfloat(g_NvidiaExt[index].dst0u.x)


def _NvAtomicAddFP32(uav, address, val):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x    = address
    g_NvidiaExt[index].src1u.x    = asuint(val)
    g_NvidiaExt[index].src2u.x    = NV_EXTN_ATOM_ADD
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP32_ATOMIC

    return asfloat(g_NvidiaExt[index].dst0u.x)


def _NvAtomicAddFP32(uav, address, val):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xy   = address
    g_NvidiaExt[index].src1u.x    = asuint(val)
    g_NvidiaExt[index].src2u.x    = NV_EXTN_ATOM_ADD
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP32_ATOMIC

    return asfloat(g_NvidiaExt[index].dst0u.x)


def _NvAtomicAddFP32(uav, address, val):
    _NvReferenceUAVForOp(uav)
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xyz  = address
    g_NvidiaExt[index].src1u.x    = asuint(val)
    g_NvidiaExt[index].src2u.x    = NV_EXTN_ATOM_ADD
    g_NvidiaExt[index].opcode     = NV_EXTN_OP_FP32_ATOMIC

    return asfloat(g_NvidiaExt[index].dst0u.x)


# ----------------------------------------------------------------------------
# UINT64 Atmoic Functions
# The functions below performs atomic operation on the given UAV treating the value as uint64
# byteAddress must be multiple of 8
# The returned value is the value present in memory location before the atomic operation
# uint2 vector type is used to represent a single uint64 value with the x component containing the low 32 bits and y
# component the high 32 bits.
def _NvAtomicCompareExchangeUINT64(uav, byteAddress, compareValue, value):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x  = byteAddress
    g_NvidiaExt[index].src1u.xy = compareValue
    g_NvidiaExt[index].src1u.zw = value
    g_NvidiaExt[index].src2u.x  = NV_EXTN_ATOM_CAS
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvAtomicOpUINT64(uav, byteAddress, value, atomicOpType):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x  = byteAddress
    g_NvidiaExt[index].src1u.xy = value
    g_NvidiaExt[index].src2u.x  = atomicOpType
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvAtomicCompareExchangeUINT64(uav, address, compareValue, value):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x  = address
    g_NvidiaExt[index].src1u.xy = compareValue
    g_NvidiaExt[index].src1u.zw = value
    g_NvidiaExt[index].src2u.x  = NV_EXTN_ATOM_CAS
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvAtomicOpUINT64(uav, address, value, atomicOpType):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x  = address
    g_NvidiaExt[index].src1u.xy = value
    g_NvidiaExt[index].src2u.x  = atomicOpType
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvAtomicCompareExchangeUINT64(uav, address, compareValue, value):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xy  = address
    g_NvidiaExt[index].src1u.xy = compareValue
    g_NvidiaExt[index].src1u.zw = value
    g_NvidiaExt[index].src2u.x  = NV_EXTN_ATOM_CAS
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvAtomicOpUINT64(uav, address, value, atomicOpType):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xy  = address
    g_NvidiaExt[index].src1u.xy = value
    g_NvidiaExt[index].src2u.x  = atomicOpType
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvAtomicCompareExchangeUINT64(uav, address, compareValue, value):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xyz  = address
    g_NvidiaExt[index].src1u.xy = compareValue
    g_NvidiaExt[index].src1u.zw = value
    g_NvidiaExt[index].src2u.x  = NV_EXTN_ATOM_CAS
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvAtomicOpUINT64(uav, address, value, atomicOpType):
    _NvReferenceUAVForOp(uav)

    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.xyz  = address
    g_NvidiaExt[index].src1u.xy = value
    g_NvidiaExt[index].src2u.x  = atomicOpType
    g_NvidiaExt[index].opcode   = NV_EXTN_OP_UINT64_ATOMIC

    return g_NvidiaExt[index].dst0u.xy


def _NvFootprint(
    texSpace,
    texIndex,
    smpSpace,
    smpIndex,
    texType,
    location,
    footprintmode,
    gran,
    offset=int3(0, 0, 0)
):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x = texIndex
    g_NvidiaExt[index].src0u.y  = smpIndex
    g_NvidiaExt[index].src1u.xyz = asuint(location)
    g_NvidiaExt[index].src1u.w = gran
    g_NvidiaExt[index].src3u.x = texSpace
    g_NvidiaExt[index].src3u.y = smpSpace
    g_NvidiaExt[index].src3u.z = texType
    g_NvidiaExt[index].src3u.w = footprintmode
    g_NvidiaExt[index].src4u.xyz = asuint(offset)

    g_NvidiaExt[index].opcode = NV_EXTN_OP_FOOTPRINT
    g_NvidiaExt[index].numOutputsForIncCounter = 4

    # result is returned as the return value of IncrementCounter on fake UAV slot
    op = uint4()
    op.x = g_NvidiaExt.IncrementCounter()
    op.y = g_NvidiaExt.IncrementCounter()
    op.z = g_NvidiaExt.IncrementCounter()
    op.w = g_NvidiaExt.IncrementCounter()
    return op


def _NvFootprintBias(
    texSpace,
    texIndex,
    smpSpace,
    smpIndex,
    texType,
    location,
    footprintmode,
    gran,
    bias,
    offset=int3(0, 0, 0)
):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x = texIndex
    g_NvidiaExt[index].src0u.y  = smpIndex
    g_NvidiaExt[index].src1u.xyz = asuint(location)
    g_NvidiaExt[index].src1u.w = gran
    g_NvidiaExt[index].src2u.x = asuint(bias)
    g_NvidiaExt[index].src3u.x = texSpace
    g_NvidiaExt[index].src3u.y = smpSpace
    g_NvidiaExt[index].src3u.z = texType
    g_NvidiaExt[index].src3u.w = footprintmode
    g_NvidiaExt[index].src4u.xyz = asuint(offset)

    g_NvidiaExt[index].opcode = NV_EXTN_OP_FOOTPRINT_BIAS
    g_NvidiaExt[index].numOutputsForIncCounter = 4

    # result is returned as the return value of IncrementCounter on fake UAV slot
    op = uint4()
    op.x = g_NvidiaExt.IncrementCounter()
    op.y = g_NvidiaExt.IncrementCounter()
    op.z = g_NvidiaExt.IncrementCounter()
    op.w = g_NvidiaExt.IncrementCounter()
    return op


def _NvFootprintLevel(
    texSpace,
    texIndex,
    smpSpace,
    smpIndex,
    texType,
    location,
    footprintmode,
    gran,
    lodLevel,
    offset=int3(0, 0, 0)
):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x = texIndex
    g_NvidiaExt[index].src0u.y = smpIndex
    g_NvidiaExt[index].src1u.xyz = asuint(location)
    g_NvidiaExt[index].src1u.w = gran
    g_NvidiaExt[index].src2u.x = asuint(lodLevel)
    g_NvidiaExt[index].src3u.x = texSpace
    g_NvidiaExt[index].src3u.y = smpSpace
    g_NvidiaExt[index].src3u.z = texType
    g_NvidiaExt[index].src3u.w = footprintmode
    g_NvidiaExt[index].src4u.xyz = asuint(offset)

    g_NvidiaExt[index].opcode = NV_EXTN_OP_FOOTPRINT_LEVEL
    g_NvidiaExt[index].numOutputsForIncCounter = 4

    # result is returned as the return value of IncrementCounter on fake UAV slot
    op = uint4()
    op.x = g_NvidiaExt.IncrementCounter()
    op.y = g_NvidiaExt.IncrementCounter()
    op.z = g_NvidiaExt.IncrementCounter()
    op.w = g_NvidiaExt.IncrementCounter()
    return op


def _NvFootprintGrad(
    texSpace,
    texIndex,
    smpSpace,
    smpIndex,
    texType,
    location,
    footprintmode,
    gran,
    ddx,
    ddy,
    offset=int3(0, 0, 0)
):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x = texIndex
    g_NvidiaExt[index].src0u.y = smpIndex
    g_NvidiaExt[index].src1u.xyz = asuint(location)
    g_NvidiaExt[index].src1u.w = gran
    g_NvidiaExt[index].src2u.xyz = asuint(ddx)
    g_NvidiaExt[index].src5u.xyz = asuint(ddy)
    g_NvidiaExt[index].src3u.x = texSpace
    g_NvidiaExt[index].src3u.y = smpSpace
    g_NvidiaExt[index].src3u.z = texType
    g_NvidiaExt[index].src3u.w = footprintmode
    g_NvidiaExt[index].src4u.xyz = asuint(offset)
    g_NvidiaExt[index].opcode = NV_EXTN_OP_FOOTPRINT_GRAD
    g_NvidiaExt[index].numOutputsForIncCounter = 4

    # result is returned as the return value of IncrementCounter on fake UAV slot
    op = uint4()
    op.x = g_NvidiaExt.IncrementCounter()
    op.y = g_NvidiaExt.IncrementCounter()
    op.z = g_NvidiaExt.IncrementCounter()
    op.w = g_NvidiaExt.IncrementCounter()
    return op


# returns value of special register - specify subopcode from any of NV_SPECIALOP_* specified in
# nvShaderExtnEnums.h - other opcodes undefined behavior
def _NvGetSpecial(subOpCode):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].opcode = NV_EXTN_OP_GET_SPECIAL
    g_NvidiaExt[index].src0u.x = subOpCode
    return g_NvidiaExt.IncrementCounter()


# predicate is returned in laneValid indicating if srcLane is in range and val from specified lane is returned.
def _NvShflGeneric(val, srcLane, maskClampVal):
    index = g_NvidiaExt.IncrementCounter()
    g_NvidiaExt[index].src0u.x = val                             # variable to be shuffled
    g_NvidiaExt[index].src0u.y = srcLane                         # source lane
    g_NvidiaExt[index].src0u.z = maskClampVal
    g_NvidiaExt[index].opcode = NV_EXTN_OP_SHFL_GENERIC
    g_NvidiaExt[index].numOutputsForIncCounter = 2

    laneValid = asuint(g_NvidiaExt.IncrementCounter())
    return g_NvidiaExt.IncrementCounter(), laneValid


# RW structured buffer for Nvidia shader extensions
# Application needs to define NV_SHADER_EXTN_SLOT as a unused slot, which
# should be
# set using NvAPI_D3D11_SetNvShaderExtnSlot() call before creating the first
# shader that
# uses nvidia shader extensions. E.g before including this file in shader
# define it as:
# define NV_SHADER_EXTN_SLOT u7
# For SM5.1, application needs to define NV_SHADER_EXTN_REGISTER_SPACE as
# register space
# E.g. before including this file in shader define it as:
# define NV_SHADER_EXTN_REGISTER_SPACE space2
# Note that other operations to this UAV will be ignored so application
# should bind a null resource

# ----------------------------------------------------------------------------
# 
# performs Atomic operation on two consecutive fp16 values in the given UAV
# the uint paramater 'fp16x2Val' is treated as two fp16 values
# the passed sub-opcode 'op' should be an immediate constant
# byteAddress must be multiple of 4
# the returned value are the two fp16 values packed into a single uint
# ----------------------------------------------------------------------------#
# 
# performs Atomic operation on a R16G16_FLOAT UAV at the given address
# the uint paramater 'fp16x2Val' is treated as two fp16 values
# the passed sub-opcode 'op' should be an immediate constant
# the returned value are the two fp16 values (.x and .y components) packed
# into a single uint
# Warning: Behaviour of these set of functions is undefined if the UAV is not
# of R16G16_FLOAT format (might result in app crash or TDR)
# ----------------------------------------------------------------------------#
# 
# performs Atomic operation on a R16G16B16A16_FLOAT UAV at the given address
# the uint2 paramater 'fp16x2Val' is treated as four fp16 values
# i.e, fp16x2Val.x = uav.xy and fp16x2Val.y = uav.yz
# the passed sub-opcode 'op' should be an immediate constant
# the returned value are the four fp16 values (.xyzw components) packed into
# uint2
# Warning: Behaviour of these set of functions is undefined if the UAV is not
# of R16G16B16A16_FLOAT format (might result in app crash or TDR)
# break it down into two fp16x2 atomic ops
# first op has x-coordinate = x * 2
# second op has x-coordinate = x * 2 + 1
# break it down into two fp16x2 atomic ops
# first op has x-coordinate = x * 2
# second op has x-coordinate = x * 2 + 1
# break it down into two fp16x2 atomic ops
# first op has x-coordinate = x * 2
# second op has x-coordinate = x * 2 + 1
# ----------------------------------------------------------------------------#
# 
# FP32 Atomic functions
# performs Atomic operation treating the uav as FLOAT (fp32) values
# the passed sub-opcode 'op' should be an immediate constant
# byteAddress must be multiple of 4# passing as uint to make it more convinient for the driver to translate
# ----------------------------------------------------------------------------#
# 
# UINT64 Atmoic Functions
# The functions below performs atomic operation on the given UAV treating the
# value as uint64
# byteAddress must be multiple of 8
# The returned value is the value present in memory location before the atomic
# operation
# uint2 vector type is used to represent a single uint64 value with the x
# component containing the low 32 bits and y component the high 32 bits.
# result is returned as the return value of IncrementCounter on fake UAV slot
# result is returned as the return value of IncrementCounter on fake UAV slot
# result is returned as the return value of IncrementCounter on fake UAV slot
# result is returned as the return value of IncrementCounter on fake UAV slot
# returns value of special register - specify subopcode from any of
# NV_SPECIALOP_* specified in nvShaderExtnEnums.h - other opcodes undefined
# behavior
# predicate is returned in laneValid indicating if srcLane is in range and val
# from specified lane is returned.# variable to be shuffled# source lane
