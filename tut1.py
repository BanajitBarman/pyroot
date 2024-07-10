import ROOT

def main():
    # Create a simple 1D histogram
    histogram = ROOT.TH1F("hist", "Example Histogram;X-axis;Y-axis", 100, -4, 4)
    
    # Fill the histogram with random Gaussian data
    for i in range(1000):
        histogram.Fill(ROOT.gRandom.Gaus())
    
    # Draw the histogram
    canvas = ROOT.TCanvas("canvas", "Canvas for Histogram", 800, 600)
    histogram.Draw()
    canvas.SaveAs("/tmp/basic_histogram.png")

if __name__ == "__main__":
    main()
