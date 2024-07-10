import ROOT

def data_analysis_pipeline():
    # Generate random data and store in a Python list
    data = [ROOT.gRandom.Gaus() for _ in range(1000)]
    
    # Create a histogram and fill with data
    histogram = ROOT.TH1F("h1", "Data Analysis Pipeline;X Axis;Y Axis", 100, -4, 4)
    for value in data:
        histogram.Fill(value)
    
    # Create a tree and store the data in branches
    file = ROOT.TFile("/tmp/analysis_pipeline.root", "RECREATE")
    tree = ROOT.TTree("tree", "Example Tree")
    branch_value = ROOT.std.vector('float')(1)
    tree.Branch("data", branch_value)
    for value in data:
        branch_value[0] = value
        tree.Fill()
    tree.Write()
    
    # Draw and save the histogram
    canvas = ROOT.TCanvas("canvas", "Analysis Canvas", 800, 600)
    histogram.Draw()
    canvas.SaveAs("/tmp/analysis_pipeline_histogram.png")
    
    # Close the file
    file.Close()

if __name__ == "__main__":
    data_analysis_pipeline()
