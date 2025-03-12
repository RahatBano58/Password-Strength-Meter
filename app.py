import streamlit as st
import random
import string

# Function to calculate password strength
def calculate_strength(password):
    length = len(password)
    if length < 8:
        return "🔴Weak"
    elif 8 <= length < 12:
        return "🟡Moderate"
    else:
        return "🟢Strong"

# Function to generate a random password
def generate_password(length, use_numbers, use_symbols):
    chars = string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Streamlit App Layout
st.markdown("<h1 style='text-align: center; color: white;'>🔐 Password Generator Tool</h1>", unsafe_allow_html=True)

# CSS to customize the UI and footer
st.markdown("""
    <style>
        div[data-testid="stSidebar"] {background-color: #2c2c2c;}
        h1 {background-color: #6c63ff; padding: 10px; border-radius: 10px;}
        .stButton button {background-color: #6c63ff; color: white; border-radius: 10px;}
        .stSlider {color: #6c63ff;}
         footer {
            position: fixed;
            bottom: 0;
            width: 45%;
            background-color: #6c63ff;
            color: black;
            text-align: center;
            padding: 20px;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 0 10px 0 rgba(0,0,0,0.1);
            box-sizing: border-box;
            border-top: 1px solid #2c2c2c;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 15px;
            margin-bottom: 20px;

        }
    </style>
""", unsafe_allow_html=True)

# Choose method for generating password
password_method = st.radio(
    "Choose your password method:", 
    ('🎲 Generate Password', '✍️ Enter Password')
)

if password_method == '🎲 Generate Password':
    length = st.slider('Password Length', 8, 32, 16)
    use_numbers = st.checkbox('🔢 Include Numbers', value=True)
    use_symbols = st.checkbox('💎 Include Symbols', value=True)
    
    if st.button('🎲 Generate Password'):
        generated_password = generate_password(length, use_numbers, use_symbols)
        st.success(f'🔐 Generated Password: {generated_password}')
        strength = calculate_strength(generated_password)
        st.info(f'💡 Password Strength: {strength}')

elif password_method == '✍️ Enter Password':
    entered_password = st.text_input('Enter your password', type='password')
    if entered_password:
        strength = calculate_strength(entered_password)
        st.info(f'💡 Password Strength: {strength}')

# Centered Footer with light pink background
st.markdown("""
    <footer>
        Made with ❤️ by Rahat Bano | 💻 Powered by Python & Streamlit
    </footer>
""", unsafe_allow_html=True)
