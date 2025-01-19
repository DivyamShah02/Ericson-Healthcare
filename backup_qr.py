import os
import zipfile
import base64
import qrcode


def split_folder(folder_path, chunk_size_mb=20):
    """Split a folder into smaller chunks."""
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    chunks = []
    current_chunk = []
    current_size = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if current_size + file_size > chunk_size:
                chunks.append(current_chunk)
                current_chunk = []
                current_size = 0

            current_chunk.append(file_path)
            current_size += file_size

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def create_zip(files, zip_name):
    """Create a zip file from a list of files."""
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            arcname = os.path.relpath(file, os.path.commonpath(files))
            zipf.write(file, arcname)


def zip_to_base64(zip_path):
    """Convert a zip file to a Base64 string."""
    with open(zip_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()


def create_qr(base64_data, output_dir, chunk_index):
    """Generate multiple QR codes for large Base64 data."""
    max_qr_data_size = 2953  # Maximum characters for QR code version 40 (approx.)
    chunks = [base64_data[i:i + max_qr_data_size] for i in range(0, len(base64_data), max_qr_data_size)]

    for i, chunk in enumerate(chunks, start=1):
        qr = qrcode.QRCode(
            version=39,  # Max version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
        )
        qr.add_data(chunk)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        qr_file = os.path.join(output_dir, f'chunk_{chunk_index}_part_{i}.png')
        img.save(qr_file)
        print(f"QR Code saved: {qr_file}")


def process_folder(folder_path, output_dir, chunk_size_mb=20):
    """Process the folder and generate QR codes."""
    os.makedirs(output_dir, exist_ok=True)
    chunks = split_folder(folder_path, chunk_size_mb)

    for i, chunk in enumerate(chunks, start=1):
        zip_name = os.path.join(output_dir, f'chunk_{i}.zip')
        create_zip(chunk, zip_name)

        base64_data = zip_to_base64(zip_name)

        create_qr(base64_data, output_dir, i)

        print(f"Chunk {i}: QR codes generated.")


# Example usage
folder_path = r'C:\Users\Divyam Shah\OneDrive\Desktop\Dynamic Labz\Clients\Clients\Ericson Healthcare\Ericson-Healthcare\EricsonHealthcare'  # Replace with your folder path
output_dir = r'C:\Users\Divyam Shah\OneDrive\Desktop\Dynamic Labz\Clients\Clients\Ericson Healthcare\Ericson-Healthcare\test_backup'  # Replace with your output directory
process_folder(folder_path, output_dir, chunk_size_mb=20)
