import io
import streamlit as st
import qrcode
import base64

def generate_qr_code(input_text, qr_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=qr_color, back_color="white")
    
    # Convertir la imagen a bytes
    img_byte_arr = io.BytesIO()
    qr_img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return img_byte_arr

def main():
    st.title("Generador de Códigos QR")

    # Input de texto o URL
    input_text = st.text_input("Ingrese el texto o URL para generar el código QR:")

    # Selector de color para el código QR
    qr_color = st.color_picker("Seleccione el color para el código QR:", "#000000") # Color negro por defecto

    if st.button("Generar QR"):
        if input_text:
            qr_img = generate_qr_code(input_text, qr_color)
            st.image(qr_img, caption="Código QR generado", use_column_width=True)
            st.markdown(get_image_download_link(qr_img), unsafe_allow_html=True)
        else:
            st.warning("Por favor, ingrese un texto o URL válido.")

def get_image_download_link(img_bytes):
    """
    Genera un enlace de descarga para la imagen.
    """
    encoded_img = base64.b64encode(img_bytes).decode()
    href = f'<a href="data:file/png;base64,{encoded_img}" download="codigo_qr.png">Descargar Código QR</a>'
    return href

if __name__ == "__main__":
    main()
