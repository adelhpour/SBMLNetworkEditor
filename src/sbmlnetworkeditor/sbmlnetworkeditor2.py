import libsbmlnetworkeditor
import networkinfotranslator
from IPython.display import display
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

class SBMLNetworkEditor(libsbmlnetworkeditor.LibSBMLNetworkEditor):

    def __init__(self, sbml=""):
        super().__init__(sbml)

    def save_figure(self, file_directory="", file_name="", file_format=""):
        if not self.getNumLayouts() or (not self.getNumGlobalRenderInformation() and not self.getNumLocalRenderInformation()):
            self.autolayout()
        networkinfotranslator.import_sbml_export_figure(self.export(), file_directory, file_name, file_format)

    def draw(self):
        if not self.getNumLayouts() or (not self.getNumGlobalRenderInformation() and not self.getNumLocalRenderInformation()):
            self.autolayout()

        pil_image = networkinfotranslator.import_sbml_export_pil_image(self.export())
        pil_image = Image.open('/Users/home/Downloads/example10.png', 'r')
        imshow(np.asarray(pil_image))




a = SBMLNetworkEditor("/Users/home/Downloads/example.xml")
a.save_figure("/Users/home/Downloads", "example10", "png")
a.draw()





