import libsbmlnetworkeditor
import networkinfotranslator
from IPython.display import display


class SBMLNetworkEditor(libsbmlnetworkeditor.LibSBMLNetworkEditor):

    def __init__(self, sbml=""):
        super().__init__(sbml)

    def draw(self, file_directory="", file_name="sbml_network", file_format="png"):
        """
        Draws the network of the SBML model. Saves the figure to the file_directory if specified, otherwise displays the figure.

        :param file_directory:
        :param file_name:
        :param file_format:
        """
        if not self._layout_is_specified() or not self._render_is_specified():
            self.autolayout()
        if file_directory:
            networkinfotranslator.import_sbml_export_figure(self.export(), file_directory, file_name, file_format)
        else:
            display(networkinfotranslator.import_sbml_export_pil_image(self.export()))

    def _layout_is_specified(self):
        if self.getNumLayouts():
            return True

        return False

    def _render_is_specified(self):
        if self.getNumGlobalRenderInformation() or self.getNumLocalRenderInformation():
            return True

        return False



