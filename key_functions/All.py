from .PyButton import *

class Global_Storage:

    Properties = {}

    Subclasses = {
        "PyButton": PyButton,
    }

    def __init__(self, **kwargs):
        for i in kwargs.keys():
            self.Properties[i] = kwargs[i]

    def newClass(self, className, **passed_args):

        if not className in self.Subclasses: return
        #
        nClass = self.Subclasses[className]
        final_tb = {}

        for Requirement in nClass.requirements:
            UReq = (
                isinstance(Requirement, dict)
                and Requirement["var_name"]
                or Requirement
            )

            Detected = (
                    UReq in passed_args and passed_args[UReq]
                    or (
                        UReq in self.Properties and self.Properties[UReq]
                        or ("default" in Requirement and Requirement["default"])
                    )
            )
            if Detected is None:
                raise TypeError(f"Requirement {Requirement} in class \"{className}\" not found in neither passed_args nor (or is it or?) self.Properties.")

            final_tb[UReq] = Detected

        return nClass(**final_tb)

__all__ = "Global_Storage",