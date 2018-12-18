from neural_network import SelectionTree, Tutorials
from random import randint

print("Network is building...")
st = SelectionTree(300)

print("Network is ready! Test samples:")

N = 25  # Number of iterations
error = 0

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

    print(f'Sample {sample_id} --- network output: {output}, real answer: {answer}')

print(f"Average error: {error / 10}")