#kevin fink
#kevin@shorecode.org
#Sat Apr  5 09:53:28 AM +07 2025
#

import sys
import os
from mtg_filepaths import Files
from moviepy import VideoFileClip

def get_input_filenames(input_dir, output_dir):
    """
    Returns a list of all file names in the given directory.

    Parameters:
    - input_dir (str): The path to the directory.

    Returns:
    - List[str]: A list of file names within the directory.
    """
    try:
        # List all entries in the directory
        filenames = os.listdir(input_dir)
        print(filenames)
        # Filter out directories, keeping only files
        input_fps = [os.path.join(input_dir, f) for f in filenames if os.path.isfile(os.path.abspath(os.path.join(input_dir, f)))]
        output_fps = [os.path.join(output_dir, os.path.splitext(fn)[0]+'.gif') for fn in filenames if os.path.isfile(os.path.abspath(os.path.join(input_dir, fn)))]
        return input_fps, output_fps
    except FileNotFoundError:
        print(f"The directory {input_dir} does not exist.")
        return [], []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []

def convert_mp4_to_gif(input_fps, output_gifs_fps, start_time=None, end_time=None, resize_factor=1.0):
    for i, input_path in enumerate(input_fps):
        try:
            
            print(input_path)
            # Load the video file
            clip = VideoFileClip(input_path)
        
            # Trim the clip if start_time and end_time are provided
            if start_time is not None and end_time is not None:
                clip = clip.subclipped(start_time, end_time)
        
            # Resize if needed
            if resize_factor != 1.0:
                clip = clip.resized(new_size=resize_factor)
        
            # Write the GIF file
            clip.write_gif(output_gifs_fps[i], fps=10)  # You can adjust the fps for smoother GIFs
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    files = Files()
    filepaths = files.get_files_list()
    output_dir = filepaths[2]
    input_dir = filepaths[1]
    input_files, output_gifs_fps = get_input_filenames(input_dir, output_dir)
    convert_mp4_to_gif(input_files, output_gifs_fps, resize_factor=0.05)