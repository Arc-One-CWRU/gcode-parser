from ..base import SectionProcessorInterface, GCodeSection


class PostHome(SectionProcessorInterface):
    """Adds the micer settings to GCode file.
    """

    def __init__(self) -> None:
        super().__init__()

    def process(self, gcode_section: list[str]) -> list[str]:
        """Adds the git commit hash to the top of the G-Code files to
        differentiate versions
        """
        
        gcode_section.insert(0, "G28 Z")
        gcode_section.insert(0,"G28 XY")
        gcode_section.insert(0, "G90")
        gcode_section.insert(0, "G1 Z100")
        gcode_section.insert(0, "G91")
        return gcode_section

    def section_type(self) -> GCodeSection:
        """Returns the current section type.
        """
        return GCodeSection.END_SCRIPT_SECTION