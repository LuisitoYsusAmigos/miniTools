import os
import re
from psd_tools import PSDImage

# Carpetas
INPUT_DIR = "psd"
OUTPUT_DIR = "img"

def clean_filename(name):
    """
    Limpia caracteres inválidos en Windows
    """
    if not name:
        return "layer"

    # Reemplazar caracteres inválidos
    name = re.sub(r'[<>:"/\\|?*]', '_', name)

    # Quitar espacios extremos
    name = name.strip()

    # Limitar longitud (evita errores largos)
    return name[:100] if name else "layer"


def export_layers(psd_path, output_folder, ext="png"):
    psd = PSDImage.open(psd_path)

    for i, layer in enumerate(psd.descendants()):
        # Saltar capas invisibles
        if not layer.is_visible():
            continue

        image = layer.composite()
        if image is None:
            continue

        # Limpiar nombre
        layer_name = clean_filename(layer.name)

        filename = f"{i}_{layer_name}.{ext}"
        output_path = os.path.join(output_folder, filename)

        try:
            image.save(output_path)
            print(f"Exportado: {output_path}")
        except Exception as e:
            print(f"Error en capa {i}: {e}")


def main():
    format_choice = input("¿Desea exportar las imágenes en formato WEB (webp) o PNG? (web/png): ").strip().lower()
    while format_choice not in ["web", "png"]:
        format_choice = input("Por favor, ingrese 'web' o 'png': ").strip().lower()

    ext = "webp" if format_choice == "web" else "png"
    folder_suffix = "WEB" if format_choice == "web" else "PNG"

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".psd"):
            psd_path = os.path.join(INPUT_DIR, file)

            # Nombre del PSD sin extensión
            psd_name = os.path.splitext(file)[0]

            # Carpeta por PSD
            folder_name = f"{clean_filename(psd_name)} {folder_suffix}"
            output_folder = os.path.join(OUTPUT_DIR, folder_name)
            os.makedirs(output_folder, exist_ok=True)

            print(f"\nProcesando: {file}")
            export_layers(psd_path, output_folder, ext)


if __name__ == "__main__":
    main()