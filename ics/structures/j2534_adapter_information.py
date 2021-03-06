# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

class j2534_adapter_information(ctypes.Structure):
    _fields_ = [
        ('szName', ctypes.c_char * 128), # Adaptor name - ASCII Null terminated
        ('szDeviceName', ctypes.c_char * 64), # Device name - ASCII Null terminated
        ('Status', ctypes.c_ulong), # Adaptor Status, 0 for disabled, 1 for enabled
        ('bMAC_Address', ctypes.c_ubyte * 6), # The Media Access Control (MAC) Address of the Network interface in the PC that is to be connected to the vehicle.
        ('bIPV6_Address', ctypes.c_ubyte * 16), 
        ('bIPV4_Address', ctypes.c_ubyte * 4), # The Ipv4 address assigned to the Network interface. If not available, all bytes are set to zero.
    ]

# Extra names go here:
J2534_ADAPTER_INFORMATION = j2534_adapter_information
# End of extra names

