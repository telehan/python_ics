# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

class ics_spy_message_flex_ray(ctypes.Structure):
    _fields_ = [
        ('StatusBitField', ctypes.c_uint32), 
        ('StatusBitField2', ctypes.c_uint32), 
        ('TimeHardware', ctypes.c_uint32), 
        ('TimeHardware2', ctypes.c_uint32), 
        ('TimeSystem', ctypes.c_uint32), 
        ('TimeSystem2', ctypes.c_uint32), 
        ('TimeStampHardwareID', ctypes.c_uint8), 
        ('TimeStampSystemID', ctypes.c_uint8), 
        ('NetworkID', ctypes.c_uint8), 
        ('NodeID', ctypes.c_uint8), 
        ('Protocol', ctypes.c_uint8), 
        ('MessagePieceID', ctypes.c_uint8), 
        ('ExtraDataPtrEnabled', ctypes.c_uint8), 
        ('NumberBytesHeader', ctypes.c_uint8), 
        ('NumberBytesData', ctypes.c_uint8), 
        ('NetworkID2', ctypes.c_uint8), 
        ('DescriptionID', ctypes.c_int16), 
        ('ArbIDOrHeader', ctypes.c_uint32), 
        ('id', ctypes.c_uint32, 12), # [Bitfield] 
        ('res1', ctypes.c_uint32, 4), # [Bitfield] 
        ('cycle', ctypes.c_uint32, 6), # [Bitfield] 
        ('chA', ctypes.c_uint32, 1), # [Bitfield] 
        ('chB', ctypes.c_uint32, 1), # [Bitfield] 
        ('startup', ctypes.c_uint32, 1), # [Bitfield] 
        ('sync', ctypes.c_uint32, 1), # [Bitfield] 
        ('null_frame', ctypes.c_uint32, 1), # [Bitfield] 
        ('payload_preamble', ctypes.c_uint32, 1), # [Bitfield] 
        ('frame_reserved', ctypes.c_uint32, 1), # [Bitfield] 
        ('dynamic', ctypes.c_uint32, 1), # [Bitfield] 
        ('Data', ctypes.c_uint8 * 8), 
        ('StatusBitField3', ctypes.c_uint32), 
        ('StatusBitField4', ctypes.c_uint32), 
        ('AckBytes', ctypes.c_uint8 * 8), 
        ('hcrc_msbs', ctypes.c_uint32, 3), # [Bitfield] 
        ('res2', ctypes.c_uint32, 5), # [Bitfield] 
        ('hcrc_lsbs', ctypes.c_uint32, 8), # [Bitfield] 
        ('frame_len_12_5ns', ctypes.c_uint32, 16), # [Bitfield] 
        ('fcrc0', ctypes.c_uint32, 8), # [Bitfield] 
        ('fcrc1', ctypes.c_uint32, 8), # [Bitfield] 
        ('fcrc2', ctypes.c_uint32, 8), # [Bitfield] 
        ('tss_len_12_5ns', ctypes.c_uint32, 8), # [Bitfield] 
        ('ExtraDataPtr', ctypes.c_voidp), 
        ('MiscData', ctypes.c_uint8), 
        ('Reserved', ctypes.c_uint8 * 3), 
    ]

# Extra names go here:
icsSpyMessageFlexRay = ics_spy_message_flex_ray
# End of extra names

