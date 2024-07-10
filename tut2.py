import ROOT

def create_histogram():
    # Create a 1D histogram
    histogram = ROOT.TH1F("h1", "Gaussian Distribution;X Axis;Y Axis", 100, -4, 4)
    
    # Fill the histogram with random Gaussian data
    for i in range(1000):
        histogram.Fill(ROOT.gRandom.Gaus())
    
    # Customize the histogram
    histogram.SetLineColor(ROOT.kRed)
    histogram.SetLineWidth(2)
    histogram.SetFillColor(ROOT.kBlue)
    
    # Draw the histogram on a canvas
    canvas = ROOT.TCanvas("canvas", "Histogram Canvas", 800, 600)
    histogram.Draw()
    
    # Save the histogram to a file
    canvas.SaveAs("/tmp/custom_histogram.png")

if __name__ == "__main__":
    create_histogram()
