# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 19:15:38 2025

@author: DELL
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create detailed flowchart with dual paths after XRD analysis
fig, ax = plt.subplots(figsize=(14, 16))
ax.set_xlim(0, 12)
ax.set_ylim(-2, 18)
ax.axis("off")

# Define process steps (excluding Feedback & Iteration)
steps = [
    (5, 17, "Materials Screening"),
    (5, 14, "Synthesis Recipe Generation"),
    (5, 11, "Robotic Synthesis Execution"),
    (5, 8, "XRD & ML Analysis"),
    (2.5, 3.5, "Successful Synthesis\n(Yield >50%)"),  # Left branch
    (7.5, 3.5, "Active Learning\nOptimization (Yield <50%)")       # Right branch
]

# Draw process boxes with different colors
colors = ["lightblue", "lightblue", "lightblue", "lightblue", "lightgreen", "salmon"]
for i, (x, y, text) in enumerate(steps):
    rect = mpatches.FancyBboxPatch(
        (x - 2.2, y - 0.6), 4.4, 1.2, boxstyle="round,pad=0.1", 
        edgecolor="black", facecolor=colors[i]
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center", fontsize=12, fontweight="bold")

# Draw main vertical arrows
for i in range(3):  # Only connect first three steps
    x1, y1, _ = steps[i]
    x2, y2, _ = steps[i+1]
    ax.annotate(
        "", xy=(x2, y2 + 0.6), xytext=(x1, y1 - 0.6),
        arrowprops=dict(arrowstyle="->", lw=2, color="black")
    )

# Draw dual paths after XRD Analysis
x_origin, y_origin = 5, 8
# Left branch (success)
ax.annotate("", xy=(3, 4.6), xytext=(5, 7.4),
            arrowprops=dict(arrowstyle="->", lw=2, color="green"))
# Right branch (active learning)
ax.annotate("", xy=(7, 4.6), xytext=(5, 7.4),
            arrowprops=dict(arrowstyle="->", lw=2, color="red"))

# Add decision diamond
decision = mpatches.Polygon(
    [(5, 6.3), (5.8, 5.5), (5, 4.7), (4.2, 5.5)],  
    closed=True, facecolor="gold", edgecolor="black"
)
ax.add_patch(decision)
ax.text(5, 5.5, "Yield >50%?", ha="center", va="center", fontsize=12, fontweight="bold")

# Add detailed descriptions
details = {
    (5, 16): "✓ Use high-throughput computational screening\n"
             "(e.g., DFT calculations from the Materials Project)\n"
             "to predict stable materials\n"
             "✓ Air stability screening\n"
             "✓ Thermodynamic stability verification\n"
             "✓ Precursor availability check",
    
    (5, 13.1): "✓ NLP extracts synthesis recipes from literature\n"
             "✓ ML models predict reaction temperatures\n based on historical data\n"
             "✓ Precursor combination optimization\n"
             "✓ Initial recipe generation",
    
    (5, 10.2): "✓ Automated powder handling\n"
             "✓ Precise temperature control\n"
             "✓ Multi-stage heating profile\n"
             "✓ Robotic sample transfer",
    
    (5, 7.2): "✓ CNN phase identification\n"
            "✓ Automated Rietveld refinement\n"
            "✓ Yield calculation\n"
            "✓ Phase purity assessment",
    
    (2.5, 2.6): "✓ Record synthesis parameters\n"
           "✓ Upload to Materials Project\n"
           "✓ Update global database\n"
           "✓ Validate computational predictions",
    
    (7.5, 2.6): "✓ Failure analysis (phase mismatch, reaction kinetics issues\n"
           "✓ ARROWS3 active learning optimizes reaction paths\n"
           "✓ Adjust precursor selection & temperature\n"
           "✓ Generate new experiments & retry synthesis"
}

for (x, y), text in details.items():
    ax.text(x, y, text, ha="center", va="center", fontsize=9, 
            bbox=dict(facecolor="white", edgecolor="gray", boxstyle="round,pad=0.2"))

# Add output arrows and labels for each section
output_labels = {
    (5, 17): "A list of target materials for synthesis",
    (5, 14): "Synthesis recipes (precursors, temperature, reaction conditions)",
    (5, 11): "Synthesized powder samples",
    (5, 8): "Phase composition and weight fractions of the synthesized samples",
    (7.5, 3.5): "Optimized synthesis recipes and improved success rates"
}

# Draw arrows to outputs and the word "Output" on the arrows (correct direction and adjust size/length)
for (x, y), label in output_labels.items():
    # Adjust the arrow start and end positions to move them more to the right
    ax.annotate(
        "", xy=(x + 4.0, y), xytext=(x + 2.5, y),  # Move arrow further to the right
        arrowprops=dict(arrowstyle="->", lw=2, color="black")
    )
    # Place label to the right of the arrow
    ax.text(x + 4.5, y, label, ha="left", va="center", fontsize=12, fontweight="bold", bbox=dict(facecolor="lightyellow", edgecolor="black", boxstyle="round,pad=0.3"))  # Lighter color for output boxes

# Add output labels
output_labels = {
    (3, 4): "Validated Material\n(Added to Database)",
    (7, 4): "Optimized Synthesis\nConditions"
}

for (x, y), text in output_labels.items():
    ax.text(x, y + 2, text, ha="center", va="bottom", fontsize=10, 
            fontweight="bold", color="darkblue")

arrow_path = [
    (7.5, 2),  # Starting point (bottom of the active learning box)
    (7.5, 1),  # Slightly shorter downward movement
    (0.05, 1),  # Shorter leftward movement
    (0.05, 14),  # Move up slightly
    (2.5, 14)     # Final adjustment to point towards the left side of "Synthesis Recipe Generation"
]

# Plot the path with straight lines and one arrow
for i in range(len(arrow_path) - 1):
    x_start, y_start = arrow_path[i]
    x_end, y_end = arrow_path[i+1]
    ax.annotate(
        "", xy=(x_end, y_end), xytext=(x_start, y_start),
        arrowprops=dict(arrowstyle="->", lw=2, color="red")
    )

text_position = (3.75, 0.6)  # Positioning the text below the arrow
ax.text(text_position[0], text_position[1], 
        "Iterative improvement until successful synthesis is achieved", 
        ha="center", va="center", fontsize=14, fontweight="bold", color="black") 

plt.show()
