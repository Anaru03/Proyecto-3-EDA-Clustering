import os
import glob
import sys
import subprocess

def install_required_packages():
    """Install required packages if they're not already installed."""
    required_packages = ['pyreadstat']
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} has been installed")

# Install required packages first
print("Checking for required dependencies...")
install_required_packages()

# Now import the packages after installation
import pandas as pd
import pyreadstat

def convert_and_merge_sav_files(input_folder, output_file):
    """
    Convert all .sav files in the input folder and merge them into a single CSV file.
    
    Args:
        input_folder: Path to the folder containing .sav files
        output_file: Path to save the merged CSV file
    """
    # Find all .sav files in the input folder
    sav_files = glob.glob(os.path.join(input_folder, "*.sav"))
    
    if not sav_files:
        print(f"No .sav files found in {input_folder}")
        return
    
    print(f"Found {len(sav_files)} .sav files to convert and merge")
    
    # List to store all DataFrames
    all_dfs = []
    
    # Process each .sav file
    for sav_file in sav_files:
        try:
            # Get the filename without extension
            file_name = os.path.basename(sav_file)
            print(f"Processing: {file_name}")
            
            # Read the .sav file
            df, meta = pyreadstat.read_sav(sav_file)
            
            # Add a column to identify the source file
            df['source_file'] = file_name
            
            # Add to the list of DataFrames
            all_dfs.append(df)
            
            print(f"  - Rows: {df.shape[0]}, Columns: {df.shape[1]}")
            
        except Exception as e:
            print(f"Error processing {sav_file}: {str(e)}")
    
    if not all_dfs:
        print("No data was successfully processed. Nothing to merge.")
        return
    
    # Merge all DataFrames
    print("\nMerging all DataFrames...")
    merged_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save to CSV
    merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"\nMerge complete!")
    print(f"Total rows: {merged_df.shape[0]}")
    print(f"Total columns: {merged_df.shape[1]}")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    # Define input and output paths
    input_folder = r"c:\Users\rodri\Documents\Data-Mining\Proyecto-3-EDA-Clustering\unmerged_data"
    output_file = r"c:\Users\rodri\Documents\Data-Mining\Proyecto-3-EDA-Clustering\merged_data.csv"
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Convert and merge .sav files
    convert_and_merge_sav_files(input_folder, output_file)