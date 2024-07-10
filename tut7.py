import ROOT
import numpy as np
import array

def read_data(file_name):
    data = np.loadtxt(file_name)
    return data[:, 0], data[:, 1]  # Return two separate columns

def store_data_in_root(x_data, y_data, output_file):
    # Create a new ROOT file
    file = ROOT.TFile(output_file, "RECREATE")
    
    # Create a tree
    tree = ROOT.TTree("tree", "Tree with two branches")

    # Create branches for x and y data
    x_value = array.array('f', [0])
    y_value = array.array('f', [0])
    tree.Branch("x", x_value, "x/F")
    tree.Branch("y", y_value, "y/F")
    
    # Fill the tree with data
    for x, y in zip(x_data, y_data):
        x_value[0] = x
        y_value[0] = y
        tree.Fill()

    # Write the tree to the file
    tree.Write()
    file.Close()

if __name__ == "__main__":
    # Read data from the input file
    x_data, y_data = read_data("data.txt")
    
    # Store data in a ROOT file
    store_data_in_root(x_data, y_data, "data.root")
