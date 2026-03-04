import streamlit as st
from PIL import Image
import remover as rm
import io

title = st.title("Remove Bg")

upload_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

col1, col2 = st.columns(2)

if upload_file is not None:
    with col1:
        st.image(upload_file, caption="Original")
    
    format_choice = st.selectbox("Choose Format", ['PNG', 'WebP', 'JPG'])
    quality = st.slider("Quality", 10, 100, 50)
    
    if st.button("Remove Background"):
        result = rm.remove_background(upload_file)
        
        with col2:
            st.image(result, caption="Backgroud Removed")
        
        buf = io.BytesIO()
        save_format = 'JPEG' if format_choice == 'JPG' else format_choice
        
        if save_format == 'JPEG':
            result = result.convert('RGB')
        
        result.save(buf, format=save_format, quality= quality)
        
        st.download_button(
            label="Download",
            data=buf.getvalue(),
            file_name=f'Output.{format_choice.lower()}',
            mime=f'image/{"jpeg" if format_choice == "JPG" else format_choice.lower()}'
        )

