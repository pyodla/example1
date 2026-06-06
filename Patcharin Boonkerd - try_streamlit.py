import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a simple Streamlit app.")
st.markdown("""You can add more components here, 
         such as charts, images, and interactive widgets.""")

st.button("Click me!")
st.text_input("Enter some text:")
st.checkbox("Check me!")
st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.multiselect("Select multiple options:", ["Option A", "Option B", "Option C"])
st.write("That's all for now. Enjoy using Streamlit!")

#----Exercise: Adding more components and interactivity----
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")


#------------------------------------------------------
st.divider()
st.write("This is a divider to separate sections.")
st.header("Separate columns layout")
col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1")
    st.button("Button in column 1")
with col2:    
    st.write("This is column 2")
    st.button("Button in column 2")
    
    
st.divider()
st.write("This is another divider to separate sections.")
st.header("Expander example")
with st.expander("Click to expand"):
    st.write("This content is hidden until you click the expander.")
    st.write("You can put any Streamlit components here, such as charts, images, or text.") 


st.divider()
st.write("Making tabs for better organization")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("This is content for Tab 1")
    st.button("Button in Tab 1")
with tab2:
    st.write("This is content for Tab 2")
    st.button("Button in Tab 2")
with tab3:
    st.write("This is content for Tab 3")
    st.button("Button in Tab 3")
    
st.divider()
st.write("Sidebar example")
st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar where you can add additional components.")
st.sidebar.button("Sidebar Button")
st.sidebar.text_input("Sidebar Text Input")
st.sidebar.checkbox("Sidebar Checkbox") 

