import streamlit as st
import numpy as np

def calculate_boards_needed(room_grid):
    # Count the number of filled squares (representing boards)
    num_boards = np.sum(room_grid == 1)
    
    # Calculate the number of packs needed (assuming each pack contains 10 boards)
    num_packs = int(np.ceil(num_boards / 10))
    
    return num_boards, num_packs

def main():
    st.title("Ceiling Board Calculator")
    
    # Create a 15x15 grid of squares
    room_grid = np.zeros((15, 15), dtype=int)
    
    # Display the grid as a heatmap
    grid_plot = st.empty()
    grid_plot.image(room_grid, use_column_width=True)
    
    # Allow users to click on squares to fill them in
    col_index, row_index = st.columns(2)
    with col_index:
        col = st.slider("Select Column", 0, 14)
    with row_index:
        row = st.slider("Select Row", 0, 14)
    
    if st.button("Fill Square"):
        room_grid[row, col] = 1
        
    if st.button("Clear Square"):
        room_grid[row, col] = 0
    
    # Calculate the number of boards needed
    num_boards, num_packs = calculate_boards_needed(room_grid)
    
    # Display the results
    st.write(f"Number of boards needed: {num_boards}")
    st.write(f"Number of packs needed: {num_packs}")

if __name__ == "__main__":
    main()
