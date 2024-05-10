import streamlit as st
import qrcode

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

st.title("Generador de QR")

# Campo de texto para ingresar la URL
url = st.text_input("Ingrese la URL:")

# Botón para generar y descargar el QR
if st.button("Generar y Descargar QR"):
    if url:
        filename = st.text_input("Nombre del archivo (sin extensión):", value="qr_code")
        if filename:
            filename += ".png"
            generador_qr(url, filename)
            st.success("QR generado y descargado correctamente como '{}'.".format(filename))
        else:
            st.error("Ingrese un nombre de archivo válido.")
    else:
        st.error("Ingrese una URL.")