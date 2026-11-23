
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit page configuration
st.set_page_config(
    page_title="Lab 9 | Chart Design",
    layout="wide"
)

# Updated sales dataset (6 branches)
data = pd.DataFrame({
    "Branch": [
        "Central",
        "Lakeside",
        "Riverside",
        "Hilltop",
        "Mountain",
        "Coastal"
    ],
    "Sales": [88, 94, 91, 97, 93, 85]
})

# Dashboard title
st.title("Designing a Clearer Bar Chart")

st.caption(
    "Data: Fictional practice values (2026) | "
    "Chart: Dania Adriana"
)

# Display dataset
with st.expander("View Sales Dataset"):
    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

# Select chart version
version = st.radio(
    "Choose a chart",
    ["Cluttered", "Improved"]
)

# Create chart
fig, ax = plt.subplots(figsize=(10, 5))

if version == "Cluttered":

    # Cluttered chart
    bars = ax.bar(
        data["Branch"],
        data["Sales"],
        color=[
            "#8FB9A8",
            "#D8B365",
            "#B2ABD2",
            "#5E3C99",
            "#80B1D3",
            "#E07A5F"
        ]
    )

    # Truncated axis
    ax.set_ylim(80, 100)

    # Excessive decoration
    ax.set_facecolor("#E8E8E8")

    ax.grid(
        True,
        color="white",
        linewidth=2
    )

    ax.set_title("BRANCH SALES PERFORMANCE!!!")

else:

    # Improved chart
    bars = ax.bar(
        data["Branch"],
        data["Sales"],
        color="#4C78A8"
    )

    # Highlight highest-performing branch
    for branch, bar in zip(data["Branch"], bars):
        if branch == "Hilltop":
            bar.set_color("#E07A3F")

    # Start vertical axis at zero
    ax.set_ylim(0, 105)
    ax.set_yticks(range(0, 101, 20))

    # Display sales values
    ax.bar_label(
        bars,
        fmt="%.0f",
        padding=3
    )

    # Descriptive title
    ax.set_title(
        "Hilltop Branch Recorded the Highest Sales"
    )

    # Simple gridlines
    ax.grid(
        axis="y",
        color="#DDDDDD",
        linewidth=0.7
    )

    ax.set_axisbelow(True)

    # Remove unnecessary borders
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# Axis labels
ax.set_xlabel("Branch")
ax.set_ylabel("Sales (units)")

# Improve spacing
plt.xticks(rotation=0)
fig.tight_layout()

# Display chart
st.pyplot(fig, clear_figure=True)

# Summary
st.subheader("Sales Summary")

highest = data.loc[data["Sales"].idxmax()]
lowest = data.loc[data["Sales"].idxmin()]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Highest Sales",
    f"{highest['Sales']} units"
)

col2.metric(
    "Lowest Sales",
    f"{lowest['Sales']} units"
)

col3.metric(
    "Number of Branches",
    len(data)
)

st.caption(
    "The improved chart uses a zero baseline "
    "to represent sales differences accurately."
)
