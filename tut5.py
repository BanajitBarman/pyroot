import ROOT

def use_python_containers():
    # Create a list of random numbers
    data = [ROOT.gRandom.Gaus() for _ in range(1000)]
    
    # Create a histogram
    histogram = ROOT.TH1F("h1", "Histogram from Python list;X Axis;Y Axis", 100, -4, 4)
    
    # Fill the histogram with data from the list
    for value in data:
        histogram.Fill(value)
    
    # Draw the histogram
    canvas = ROOT.TCanvas("canvas", "Histogram Canvas", 800, 600)
    histogram.Draw()
    canvas.SaveAs("python_list_histogram.png")

if __name__ == "__main__":
    use_python_containers()
