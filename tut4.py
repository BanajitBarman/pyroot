import ROOT
import array

def create_tree_with_branches():
    # Create a new ROOT file
    file = ROOT.TFile("/tmp/branches_example.root", "RECREATE")
    
    # Create a tree
    tree = ROOT.TTree("tree", "Tree with multiple branches")
    
    # Create branches
    branch1_value = array.array('f', [0])
    branch2_value = array.array('f', [0])
    tree.Branch("branch1", branch1_value, "branch1/F")
    tree.Branch("branch2", branch2_value, "branch2/F")
    
    # Fill the tree with data
    for i in range(100):
        branch1_value[0] = i * 0.1
        branch2_value[0] = i * 0.2
        tree.Fill()
    
    # Write the tree to the file
    tree.Write()
    file.Close()

if __name__ == "__main__":
    create_tree_with_branches()
