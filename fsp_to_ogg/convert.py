from fsb5 import FSB5
from pydub import AudioSegment
import subprocess
import os
import shutil
import glob

def convert_fsb5_to_ogg(input_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    base = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_folder, f"{base}.ogg")

    result = subprocess.run([
        "vgmstream-cli",
        "-o", output_path,
        input_path
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ Converted: {output_path}")
    else:
        print("❌ Error converting:", result.stderr)

# ใช้งาน
# convert_fsb5_to_ogg("C:/Github/minecraftsounds/fsp_to_ogg/sounds/sounds/block/amethyst/break1.fsb", "output_sounds")
if os.path.exists("../public/sound_bedrock"):
    shutil.rmtree("../public/sound_bedrock")
os.makedirs("../public/sound_bedrock", exist_ok=True)
for fsb5_file in glob.glob("./sounds/**/*.fsb", recursive=True):
    # convert_fsb5_to_ogg(fsb5_file, "output_sounds")
    print(fsb5_file)
    foner = os.path.dirname(fsb5_file).replace("./sounds\\", "")
    output_path = os.path.join("../public/sound_bedrock", foner)
    os.makedirs(output_path, exist_ok=True)
    convert_fsb5_to_ogg(fsb5_file, output_path)
