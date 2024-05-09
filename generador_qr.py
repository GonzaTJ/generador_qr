import qrcode
import streamlit as st

filename = "/imagenes/qr_code.png"

def generador_qr(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


#-------------- APP CON STREAMLIT-------------

st.set_page_config(page_title="Generador de QR",page_icon="",layout="centered")
st.title("Generador imagen QR")
url = st.text_input("Ingresa el URL para generar el QR:")

if st.button("Generar codigo QR"):
    generador_qr(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    download = st.download_button(label="Descargar QR", data = image_data, file_name = "imagen.png" )