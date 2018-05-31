"""
ARM Support Module
"""
import envi.archs.arm as e_arm

class ArmMixin(e_arm.ArmModule, e_arm.ArmRegisterContext):

    def __init__(self):
        e_arm.ArmModule.__init__(self)
        e_arm.ArmRegisterContext.__init__(self)

