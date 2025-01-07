# gif_divider
## Simple Python Program to Split GIFs for Steam Workshop Profile Customization

This Python program splits a GIF vertically into 5 separate GIFs. It's mainly designed for **Steam Workshop Profile Customization**.

## Instructions

1. **Run the Python program** to split your GIF into 5 separate GIFs.

    ### How to Run the Code

    - Install the required libraries by running:
      ```bash
      pip install pillow
      ```

    - Download or clone this repository to your local machine.

    - Open the Python script `split_gif.py` and modify the following parameters:
      - `gif_path`: The path to the GIF you want to split.
      - `num_parts`: The number of vertical parts you want the GIF to be split into (default is 5).
      - `output_dir`: The directory where the split GIFs will be saved.

    - Example:
      ```python
      split_gif_vertically(
          gif_path=r"C:\path\to\your\gif.gif",  # Path to the GIF
          num_parts=5,  # Number of vertical parts
          output_dir=r"C:\path\to\output"  # Output directory
      )
      ```

    - Run the script:
      ```bash
      python split_gif.py
      ```

2. **Upload the GIFs** to the "Upload Artwork" menu on Steam using a browser.
3. **Before submitting** the GIFs, open the browser's developer console and enter the following code:

    ```javascript
    $J('[name=consumer_app_id]').val(480);
    $J('[name=file_type]').val(0);
    $J('[name=visibility]').val(0);
    ```

4. **Repeat the process** for all 5 GIFs.
5. Once all GIFs are uploaded, go to **Edit Profile** > **Featured Showcase** > **My Steam Workshop**, and you're all set!

## Example

Visit my profile to see how it looks: [nicosnek](https://steamcommunity.com/id/nicosnek)
