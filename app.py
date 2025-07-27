import streamlit as st

st.set_page_config(page_title="Zavoryaf", layout="centered")

# Hero Section
st.markdown("""
    <h1 style='text-align: center; color: #ff7043;'>Home-Cooked Food, Delivered to Your Door</h1>
    <p style='text-align: center;'>Support local home chefs and enjoy fresh, tasty meals with Zavoryaf.</p>
    <div style='text-align: center; margin-top: 20px;'>
        <a href='https://wa.me/917671973258?text=Hi%2C%20I%20want%20to%20order%20from%20Zavoryaf' target='_blank'>
            <button style='background-color:#25D366; color:white; padding: 10px 20px; border:none; border-radius:5px;'>Order on WhatsApp</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# About Section
st.markdown("---")
st.subheader("About Zavoryaf")
st.write("""
Zavoryaf is a platform that connects hungry customers with talented home cooks in their community.
We believe in homemade goodness, supporting small kitchens, and making food personal again.
""")

# How It Works
st.markdown("---")
st.subheader("How It Works")
st.markdown("""
1. **Browse the Menu**  
2. **Order via WhatsApp**  
3. **Enjoy your Meal!**
""")

# Contact Section
st.markdown("---")
st.subheader("Contact Us")
st.write("""
📱 WhatsApp: +91 9876543210  
📧 Email: contact@zavoryaf.com  
📸 Instagram: [@zavoryaf](https://instagram.com/zavoryaf)
""")
