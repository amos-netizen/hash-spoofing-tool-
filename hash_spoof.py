import hashlib
from PIL import Image
import random

def manipulate_image(image_path, target_hash_prefix):
    image = Image.open(image_path)  
    image_data = list(image.getdata()) 

    byte_array = bytearray() 
    for pixel in image_data:
        byte_array.extend(pixel[:3])  

    
    while True:
        current_hash = hashlib.sha512(byte_array).hexdigest()  
        if current_hash.startswith(target_hash_prefix[2:]): 
            break  
        
        
        idx = random.randint(0, len(byte_array) - 1)
        byte_array[idx] ^= 0x01  

    
    new_image = Image.new(image.mode, image.size)
    new_image.putdata([tuple(byte_array[i:i+3]) for i in range(0, len(byte_array), 3)])

    
    new_image.save('altered_image.png')

    return current_hash

if __name__ == "__main__":
    target_prefix = "0x24"  
    original_image_path = "original_image.jpg"  
    
    new_hash = manipulate_image(original_image_path, target_prefix)  
    print(f"New Image Hash: {new_hash}")
