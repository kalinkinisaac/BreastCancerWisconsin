from neural_network import SelectionTree, Tutorials
from random import randint
from database import db

FIELDS = ["identifier", "clump_thickness", "cell_size_uniformity", "cell_shape_uniformity", "marginal_adhesion",
          "single_epithelial_cell_size", "bare_nuclei", "bland_chromatin", "normal_nucleoli", "mitoses", "class"]

if not db.get_columns():
    db.create(FIELDS)
    db.load_data('data.txt')
    print('DataBase created!')
else:
    print('DataBase loaded!')


print("Network is building...")
st = SelectionTree(300)

print("Network is ready! Begin to test samples")

N = int(input('Number of iterations you wanna test: '))

error = 0

print('Beginning to select random samples...')

for i in range(N):
    sample_id = randint(500, 699)

    try:
        sample = Tutorials.get_sample(sample_id)
    except ValueError:
        i -= 1
        continue

    output = st.test(sample['inputs'])[0]
    answer = sample['answer'][0]
    error += (output - answer) ** 2

    print(f'Iteration #{i+1}: Sample {sample_id} --- network output: {output}, real answer: {answer}')

print(f"Accuracy: {100 - error*100 / N}%")