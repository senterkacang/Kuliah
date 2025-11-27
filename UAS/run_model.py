import numpy as np
from network import Network

# Load model hasil training
net = Network.load("iris_nn_model.pkl")

def classify(meas):
    x = np.array(meas).reshape(4,1)
    output = net.feedforward(x)
    species = np.argmax(output)

    species_names = ["Species1", "Species2", "Species3"]
    return species_names[species], output

# =========================================================
# Contoh penggunaan:
# =========================================================
sample = [6.7, 3.0, 5.5, 2.2]
kelas, raw = classify(sample)

print("Input measurement:", sample)
print("Hasil klasifikasi:", kelas)
print("Output raw NN:", raw)
