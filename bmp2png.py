import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox


def convert_bmp_to_png_gui():
    # 创建 GUI 主窗口（隐藏）
    root = tk.Tk()
    root.withdraw()

    # 选择输入文件夹
    input_folder = filedialog.askdirectory(title="选择包含 BMP 文件的文件夹")
    if not input_folder:
        messagebox.showinfo("提示", "你没有选择输入文件夹")
        return

    # 选择输出文件夹
    output_folder = filedialog.askdirectory(title="选择 PNG 输出文件夹")
    if not output_folder:
        messagebox.showinfo("提示", "你没有选择输出文件夹")
        return

    # 计数器
    count = 0

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.bmp'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)

            try:
                with Image.open(input_path) as img:
                    img.save(output_path, format='PNG')
                count += 1
                print(f"✅ 转换成功: {filename}")
            except Exception as e:
                print(f"⚠️ 转换失败 {filename}: {e}")

    messagebox.showinfo("转换完成", f"共转换成功 {count} 张图片！\n输出目录：{output_folder}")


if __name__ == "__main__":
    convert_bmp_to_png_gui()
