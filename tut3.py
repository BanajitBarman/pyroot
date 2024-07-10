import ROOT

def create_tree():
    # Create a new ROOT file
    file = ROOT.TFile("/tmp/tree_example.root", "RECREATE")
    
    # Create a tree and branches
    tree = ROOT.TTree("tree", "Example Tree")
    value = ROOT.std.vector('float')(1)
    tree.Branch("branch1", value)
    
    # Fill the tree with data
    for i in range(100):
        value[0] = i * 0.1
        tree.Fill()
    
    # Write the tree to the file
    tree.Write()
    file.Close()

if __name__ == "__main__":
    create_tree()
