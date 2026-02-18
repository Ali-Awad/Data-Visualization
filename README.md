# Data-Visualization

Visualization tools for object detection and segmentation results, including figure generation for publications.

## Structure

- **Visualization Codes/** -- Core plotting scripts (violin plots, regression plots, bar charts, combined figures)
- **generate_figure.py / generate_labels.py** -- Publication figure and label generators
- **combine_img.py** -- Image grid combiner for side-by-side comparisons
- **Unanimous_fig.py** -- Unanimous agreement visualization
- **colorbar.py** -- Custom colorbar generation
- **mAP_hists_v3_two_groups_stds.py** -- mAP histogram with standard deviation bands
- **Bnethic grid.py / goby grid.py / mussel grid.py** -- Species-specific detection grid figures
- **OBB*, Seg*, SCP*, GT*, Alg.%** -- Sample result images organized by task (oriented bounding box, segmentation, SCP approaches)
- **Data_rep/** -- Dataset representative samples

## Requirements

- Python 3.x (matplotlib, seaborn, pandas, PIL/Pillow)
