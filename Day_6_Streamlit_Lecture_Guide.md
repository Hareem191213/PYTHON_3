# Day 6: Introduction to Streamlit - Lecture Guide

## What is Streamlit?
Streamlit is a Python framework that turns Python scripts into interactive web applications **without needing HTML, CSS, or JavaScript**. Perfect for data science dashboards!

---

## Step 0: Setting Up Python Environment (FIRST!)

### Create a Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv .venv

# Activate the environment
.venv\Scripts\activate

# You'll see (.venv) in your terminal prompt when active
```

**Mac/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate

# You'll see (.venv) in your terminal prompt when active
```

**What it does:** 
- Creates an isolated Python environment in a folder called `.venv`
- Keeps your project packages separate from system Python
- Prevents version conflicts between different projects

**Why use virtual environments?**
- Each project can have its own package versions
- Doesn't mess with system Python
- Easy to share requirements with others
- Professional best practice!

### Deactivate Environment (when done)
```bash
deactivate
```

---

## Step 1: Installation

**Make sure your virtual environment is activated first!** (You should see `(.venv)` in terminal)

```bash
pip install streamlit
```

**What it does:** Installs the Streamlit package in your Python environment.

### Check if Streamlit is installed:
```bash
streamlit --version
```

### Install other useful packages:
```bash
pip install pandas numpy matplotlib
```

---

## Step 2: Create Your First App

### Example 1: Hello World
Create a file `step1_hello.py`:

```python
import streamlit as st

st.write("Hello, World!")
```

**Run it:**
```bash
streamlit run step1_hello.py
```

**What happens:** 
- Opens a web browser at `http://localhost:8501`
- Displays "Hello, World!" on the page
- `st.write()` - The most basic Streamlit command that displays text, data, or almost anything

---

## Step 3: Adding a Title

### Example 2: Title and Header
```python
import streamlit as st

st.title("🪄 My First Dashboard")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is plain text")
```

**Commands Explained:**
- `st.title()` - Creates a large title (biggest text)
- `st.header()` - Creates a section header (medium-large text)
- `st.subheader()` - Creates a subsection header (medium text)
- `st.text()` - Displays plain text (fixed-width font)

---

## Step 4: Adding a Sidebar

### Example 3: Sidebar Basics
```python
import streamlit as st

st.title("🪄 My Dashboard")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("This is the sidebar")
st.sidebar.info("Sidebars are great for navigation and controls!")
```

**What it does:**
- `st.sidebar.___()` - Any Streamlit command with `.sidebar` appears in the left sidebar
- Keeps your main page clean and organized
- Great for navigation menus and input controls

---

## Step 5: User Inputs (Interactive Widgets)

### Example 4: Basic Inputs
```python
import streamlit as st

st.title("🪄 Interactive Dashboard")

# Text Input
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

# Number Input
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old")

# Slider
rating = st.slider("Rate this app:", 0, 10, 5)
st.write(f"You rated: {rating}/10")
```

**Commands Explained:**
- `st.text_input()` - Creates a text box for user input
- `st.number_input()` - Creates a number input with +/- buttons
  - `min_value`, `max_value` - Set limits
  - `value` - Sets default value
- `st.slider()` - Creates a slider (min, max, default)
- **Important:** The variable stores the user's input and updates automatically!

---

## Step 6: Buttons and Selectboxes

### Example 5: Interactive Controls
```python
import streamlit as st

st.title("🪄 Controls Demo")

# Button
if st.button("Click Me!"):
    st.write("Button was clicked! 🎉")

# Selectbox (Dropdown)
option = st.selectbox(
    "Choose a color:",
    ["Red", "Green", "Blue", "Yellow"]
)
st.write(f"You selected: {option}")

# Radio Buttons
choice = st.radio(
    "Pick one:",
    ["Option 1", "Option 2", "Option 3"]
)
st.write(f"You picked: {choice}")

# Checkbox
if st.checkbox("Show secret message"):
    st.write("🤫 This is the secret message!")
```

**Commands Explained:**
- `st.button()` - Creates a clickable button, returns `True` when clicked
- `st.selectbox()` - Creates a dropdown menu
- `st.radio()` - Creates radio buttons (single selection)
- `st.checkbox()` - Creates a checkbox, returns `True`/`False`

---

## Step 7: Displaying Data

### Example 6: Data Display
```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Data Display")

# Create sample data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
})

# Display DataFrame
st.write("Here's our data:")
st.dataframe(data)

# Display as table
st.table(data)

# Display metrics
st.metric(label="Total Students", value=3, delta=1)
```

**Commands Explained:**
- `st.dataframe()` - Interactive, scrollable table
- `st.table()` - Static table (no scrolling)
- `st.metric()` - Shows a metric with optional delta (change indicator)

---

## Step 8: Charts and Visualizations

### Example 7: Simple Charts
```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Charts Demo")

# Generate random data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Line Chart
st.subheader("Line Chart")
st.line_chart(chart_data)

# Bar Chart
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Area Chart
st.subheader("Area Chart")
st.area_chart(chart_data)
```

**Commands Explained:**
- `st.line_chart()` - Quick line chart
- `st.bar_chart()` - Quick bar chart
- `st.area_chart()` - Quick area chart
- **Note:** These are built-in simple charts. For more control, use matplotlib or plotly!

---

## Step 9: Using Matplotlib Charts

### Example 8: Matplotlib Integration
```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Matplotlib Charts")

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Display in Streamlit
st.pyplot(fig)
```

**Commands Explained:**
- `st.pyplot()` - Displays a matplotlib figure
- Create your matplotlib plot as normal, then pass `fig` to `st.pyplot()`

---

## Step 10: Columns and Layout

### Example 9: Multi-Column Layout
```python
import streamlit as st

st.title("📐 Layout Demo")

# Create 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("Content in first column")

with col2:
    st.header("Column 2")
    st.write("Content in second column")

with col3:
    st.header("Column 3")
    st.write("Content in third column")

# Different sized columns
left, right = st.columns([2, 1])  # Left is 2x wider

with left:
    st.write("This column is wider")

with right:
    st.write("Narrow column")
```

**Commands Explained:**
- `st.columns(n)` - Creates `n` equal-width columns
- `st.columns([2, 1])` - Creates columns with custom widths (ratio 2:1)
- `with col:` - Everything inside goes to that column

---

## Step 11: Containers and Expanders

### Example 10: Containers
```python
import streamlit as st

st.title("📦 Containers Demo")

# Expander (collapsible section)
with st.expander("Click to expand"):
    st.write("This content is hidden until you expand!")
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

# Container
with st.container():
    st.write("This is inside a container")
    st.write("Containers group content together")
```

**Commands Explained:**
- `st.expander()` - Creates a collapsible section
- `st.container()` - Groups content together

---

## Step 12: Complete Dashboard Example

### Example 11: Full Dashboard
```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="My Dashboard",
    page_icon="🪄",
    layout="wide"
)

# Title
st.title("🪄 Hareem's Complete Dashboard")
st.markdown("---")  # Horizontal line

# Sidebar
st.sidebar.title("📋 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Data Analysis", "Visualizations"])

# Main content based on selection
if page == "Home":
    st.header("🏠 Welcome!")
    st.write("This is a complete Streamlit dashboard example.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Users", "1,234", "+12%")
    col2.metric("Revenue", "$56,789", "+5%")
    col3.metric("Satisfaction", "4.8/5", "+0.2")

elif page == "Data Analysis":
    st.header("📊 Data Analysis")
    
    # Sample data
    data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [100, 150, 120, 180, 200],
        'Profit': [20, 30, 25, 40, 50]
    })
    
    st.dataframe(data)
    
    # User controls
    show_chart = st.checkbox("Show sales chart")
    if show_chart:
        st.bar_chart(data.set_index('Month')['Sales'])

elif page == "Visualizations":
    st.header("📈 Visualizations")
    
    # Interactive controls
    num_points = st.slider("Number of points:", 10, 100, 50)
    
    # Generate data
    x = np.linspace(0, 10, num_points)
    y = np.sin(x) * st.slider("Amplitude:", 1, 10, 5)
    
    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Dynamic Sine Wave")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Created with Streamlit 🎈")
```

**New Commands:**
- `st.set_page_config()` - Configures page settings (must be first command!)
  - `page_title` - Browser tab title
  - `page_icon` - Browser tab icon (emoji or image)
  - `layout="wide"` - Uses full screen width
- `st.markdown()` - Displays markdown text
- `st.caption()` - Small, light text (for footnotes)

---

## Quick Reference: Key Commands

### Text Display
- `st.write()` - Display anything
- `st.title()` - Page title
- `st.header()` - Section header
- `st.subheader()` - Subsection header
- `st.text()` - Plain text
- `st.markdown()` - Markdown text
- `st.caption()` - Small caption text

### User Input
- `st.button()` - Button
- `st.text_input()` - Text box
- `st.number_input()` - Number input
- `st.slider()` - Slider
- `st.selectbox()` - Dropdown
- `st.radio()` - Radio buttons
- `st.checkbox()` - Checkbox

### Data Display
- `st.dataframe()` - Interactive table
- `st.table()` - Static table
- `st.metric()` - Metric with delta

### Charts
- `st.line_chart()` - Line chart
- `st.bar_chart()` - Bar chart
- `st.area_chart()` - Area chart
- `st.pyplot()` - Matplotlib figure

### Layout
- `st.sidebar` - Sidebar
- `st.columns()` - Multiple columns
- `st.container()` - Container
- `st.expander()` - Collapsible section

### Other
- `st.set_page_config()` - Page configuration
- `st.info()` - Info box (blue)
- `st.success()` - Success box (green)
- `st.warning()` - Warning box (yellow)
- `st.error()` - Error box (red)

---

## Teaching Tips

1. **Start Simple**: Begin with `st.write()` and build up
2. **Live Coding**: Type code and save - Streamlit auto-refreshes!
3. **Experiment**: Change values and see immediate results
4. **Use Emojis**: Makes dashboards more engaging 🎨
5. **Check Documentation**: https://docs.streamlit.io

---

## Practice Exercise

**Build a dashboard that:**
1. Has a title with student's name
2. Has a sidebar with 3 navigation options
3. Shows different content based on sidebar selection
4. Includes at least one chart
5. Has user input (slider, text box, etc.)
6. Uses columns or expanders for layout

**Example structure in `streamlit.py` is ready to go!**

---

## Common Issues & Solutions

**Issue:** Dashboard doesn't update
- **Solution:** Streamlit auto-refreshes on file save. Check if file is saved!

**Issue:** Import error for streamlit
- **Solution:** 
  1. Make sure virtual environment is activated (see `(.venv)` in terminal)
  2. Run `pip install streamlit` in terminal

**Issue:** Browser doesn't open
- **Solution:** Manually open `http://localhost:8501`

**Issue:** Port already in use
- **Solution:** Close other Streamlit instances or use `streamlit run app.py --server.port 8502`

**Issue:** Command 'streamlit' not found
- **Solution:** Activate your virtual environment first: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)

**Issue:** Python not found
- **Solution:** Make sure Python is installed and added to PATH

---

## Next Steps
- Explore Streamlit components library
- Try st.plotly_chart() for interactive plots
- Learn about session state for complex apps
- Deploy on Streamlit Cloud (free!)
