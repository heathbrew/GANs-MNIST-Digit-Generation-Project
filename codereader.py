import nbformat

# Define the input .ipynb file and output .txt file names
input_notebook_file = '1.C1W1_Your_First_GAN.ipynb'
output_txt_file = 'output_code.txt'

# Open the .ipynb file and parse it
with open(input_notebook_file, 'r', encoding='utf-8') as notebook_file:
    notebook_content = nbformat.read(notebook_file, as_version=4)

# Extract code from code cells and write it to the output .txt file
with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    for cell in notebook_content.cells:
        if cell.cell_type == 'code':
            txt_file.write(f"# In [{cell.execution_count}]:\n")
            txt_file.write(cell.source)
            txt_file.write('\n\n')

print(f"Code cells extracted from {input_notebook_file} and saved to {output_txt_file}.")
