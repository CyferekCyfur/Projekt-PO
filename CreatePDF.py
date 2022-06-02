from fpdf import FPDF
from matplotlib import pyplot as plt


class CreatePDF(FPDF):
    def AddToPDF(self, chart, map):
        self.add_page()
        self.image(chart, x=0, y=0, w=210, h=140)
        self.image(map, x=-15, y=140, w=240, h=160)

        self.output("Wykresy_dla_krajów.pdf", "F")


if __name__ == '__main__':

    pdf = CreatePDF()
    pdf.AddToPDF("chart.png", "map.png")
