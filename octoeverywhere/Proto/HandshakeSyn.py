# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Proto

import octoflatbuffers
from typing import Any
from typing import Optional
class HandshakeSyn(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = octoflatbuffers.encode.Get(octoflatbuffers.packer.uoffset, buf, offset)
        x = HandshakeSyn()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsHandshakeSyn(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # HandshakeSyn
    def Init(self, buf: bytes, pos: int):
        self._tab = octoflatbuffers.table.Table(buf, pos)

    # HandshakeSyn
    def PrinterId(self) -> Optional[str]:
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def IsPrimaryConnection(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(octoflatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # HandshakeSyn
    def PluginVersion(self) -> Optional[str]:
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def LocalDeviceIp(self) -> Optional[str]:
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def LocalHttpProxyPort(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # HandshakeSyn
    def Key(self) -> Optional[str]:
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def RsaChallenge(self, j: int):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(octoflatbuffers.number_types.Uint8Flags, a + octoflatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # HandshakeSyn
    def RsaChallengeAsNumpy(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(octoflatbuffers.number_types.Uint8Flags, o)
        return 0

    # HandshakeSyn
    def RsaChallengeAsByteArray(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsByteArray(o)
        return 0

    # HandshakeSyn
    def RsaChallengeLength(self) -> int:
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # HandshakeSyn
    def RsaChallengeIsNone(self) -> bool:
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # HandshakeSyn
    def RasChallengeVersion(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # HandshakeSyn
    def WebcamFlipH(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(octoflatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # HandshakeSyn
    def WebcamFlipV(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(octoflatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # HandshakeSyn
    def WebcamFlipRotate90(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return bool(self._tab.Get(octoflatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # HandshakeSyn
    def PrivateKey(self) -> Optional[str]:
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def SummonMethod(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 1

    # HandshakeSyn
    def ServerHost(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # HandshakeSyn
    def IsCompanion(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return bool(self._tab.Get(octoflatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # HandshakeSyn
    def OsType(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def HandshakeSynStart(builder: octoflatbuffers.Builder):
    builder.StartObject(16)

def Start(builder: octoflatbuffers.Builder):
    HandshakeSynStart(builder)

def HandshakeSynAddPrinterId(builder: octoflatbuffers.Builder, printerId: int):
    builder.PrependUOffsetTRelativeSlot(0, octoflatbuffers.number_types.UOffsetTFlags.py_type(printerId), 0)

def AddPrinterId(builder: octoflatbuffers.Builder, printerId: int):
    HandshakeSynAddPrinterId(builder, printerId)

def HandshakeSynAddIsPrimaryConnection(builder: octoflatbuffers.Builder, isPrimaryConnection: bool):
    builder.PrependBoolSlot(1, isPrimaryConnection, 0)

def AddIsPrimaryConnection(builder: octoflatbuffers.Builder, isPrimaryConnection: bool):
    HandshakeSynAddIsPrimaryConnection(builder, isPrimaryConnection)

def HandshakeSynAddPluginVersion(builder: octoflatbuffers.Builder, pluginVersion: int):
    builder.PrependUOffsetTRelativeSlot(2, octoflatbuffers.number_types.UOffsetTFlags.py_type(pluginVersion), 0)

def AddPluginVersion(builder: octoflatbuffers.Builder, pluginVersion: int):
    HandshakeSynAddPluginVersion(builder, pluginVersion)

def HandshakeSynAddLocalDeviceIp(builder: octoflatbuffers.Builder, localDeviceIp: int):
    builder.PrependUOffsetTRelativeSlot(3, octoflatbuffers.number_types.UOffsetTFlags.py_type(localDeviceIp), 0)

def AddLocalDeviceIp(builder: octoflatbuffers.Builder, localDeviceIp: int):
    HandshakeSynAddLocalDeviceIp(builder, localDeviceIp)

def HandshakeSynAddLocalHttpProxyPort(builder: octoflatbuffers.Builder, localHttpProxyPort: int):
    builder.PrependUint32Slot(4, localHttpProxyPort, 0)

def AddLocalHttpProxyPort(builder: octoflatbuffers.Builder, localHttpProxyPort: int):
    HandshakeSynAddLocalHttpProxyPort(builder, localHttpProxyPort)

def HandshakeSynAddKey(builder: octoflatbuffers.Builder, key: int):
    builder.PrependUOffsetTRelativeSlot(5, octoflatbuffers.number_types.UOffsetTFlags.py_type(key), 0)

def AddKey(builder: octoflatbuffers.Builder, key: int):
    HandshakeSynAddKey(builder, key)

def HandshakeSynAddRsaChallenge(builder: octoflatbuffers.Builder, rsaChallenge: int):
    builder.PrependUOffsetTRelativeSlot(6, octoflatbuffers.number_types.UOffsetTFlags.py_type(rsaChallenge), 0)

def AddRsaChallenge(builder: octoflatbuffers.Builder, rsaChallenge: int):
    HandshakeSynAddRsaChallenge(builder, rsaChallenge)

def HandshakeSynStartRsaChallengeVector(builder, numElems: int) -> int:
    return builder.StartVector(1, numElems, 1)

def StartRsaChallengeVector(builder, numElems: int) -> int:
    return HandshakeSynStartRsaChallengeVector(builder, numElems)

def HandshakeSynAddRasChallengeVersion(builder: octoflatbuffers.Builder, rasChallengeVersion: int):
    builder.PrependInt8Slot(7, rasChallengeVersion, 0)

def AddRasChallengeVersion(builder: octoflatbuffers.Builder, rasChallengeVersion: int):
    HandshakeSynAddRasChallengeVersion(builder, rasChallengeVersion)

def HandshakeSynAddWebcamFlipH(builder: octoflatbuffers.Builder, webcamFlipH: bool):
    builder.PrependBoolSlot(8, webcamFlipH, 0)

def AddWebcamFlipH(builder: octoflatbuffers.Builder, webcamFlipH: bool):
    HandshakeSynAddWebcamFlipH(builder, webcamFlipH)

def HandshakeSynAddWebcamFlipV(builder: octoflatbuffers.Builder, webcamFlipV: bool):
    builder.PrependBoolSlot(9, webcamFlipV, 0)

def AddWebcamFlipV(builder: octoflatbuffers.Builder, webcamFlipV: bool):
    HandshakeSynAddWebcamFlipV(builder, webcamFlipV)

def HandshakeSynAddWebcamFlipRotate90(builder: octoflatbuffers.Builder, webcamFlipRotate90: bool):
    builder.PrependBoolSlot(10, webcamFlipRotate90, 0)

def AddWebcamFlipRotate90(builder: octoflatbuffers.Builder, webcamFlipRotate90: bool):
    HandshakeSynAddWebcamFlipRotate90(builder, webcamFlipRotate90)

def HandshakeSynAddPrivateKey(builder: octoflatbuffers.Builder, privateKey: int):
    builder.PrependUOffsetTRelativeSlot(11, octoflatbuffers.number_types.UOffsetTFlags.py_type(privateKey), 0)

def AddPrivateKey(builder: octoflatbuffers.Builder, privateKey: int):
    HandshakeSynAddPrivateKey(builder, privateKey)

def HandshakeSynAddSummonMethod(builder: octoflatbuffers.Builder, summonMethod: int):
    builder.PrependInt8Slot(12, summonMethod, 1)

def AddSummonMethod(builder: octoflatbuffers.Builder, summonMethod: int):
    HandshakeSynAddSummonMethod(builder, summonMethod)

def HandshakeSynAddServerHost(builder: octoflatbuffers.Builder, serverHost: int):
    builder.PrependInt8Slot(13, serverHost, 0)

def AddServerHost(builder: octoflatbuffers.Builder, serverHost: int):
    HandshakeSynAddServerHost(builder, serverHost)

def HandshakeSynAddIsCompanion(builder: octoflatbuffers.Builder, isCompanion: bool):
    builder.PrependBoolSlot(14, isCompanion, 0)

def AddIsCompanion(builder: octoflatbuffers.Builder, isCompanion: bool):
    HandshakeSynAddIsCompanion(builder, isCompanion)

def HandshakeSynAddOsType(builder: octoflatbuffers.Builder, osType: int):
    builder.PrependInt8Slot(15, osType, 0)

def AddOsType(builder: octoflatbuffers.Builder, osType: int):
    HandshakeSynAddOsType(builder, osType)

def HandshakeSynEnd(builder: octoflatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: octoflatbuffers.Builder) -> int:
    return HandshakeSynEnd(builder)
