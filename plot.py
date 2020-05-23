import numpy as np
import matplotlib.pyplot as plt

err_train_8 = [1337 / 60000, 679 / 60000, 273 / 60000, 176 / 60000, 135 / 60000,
               55 / 60000, 40 / 60000, 28 / 60000, 13 / 60000, 12 / 60000,
               10 / 60000, 11 / 60000, 10 / 60000, 10 / 60000, 10 / 60000,
               10 / 60000, 10 / 60000, 10 / 60000, 10 / 60000, 10 / 60000]

err_test_8 = [240 / 10000, 158 / 10000, 102 / 10000, 100 / 10000, 97 / 10000,
              93 / 10000, 92 / 10000, 88 / 10000, 89 / 10000, 86 / 10000,
              90 / 10000, 90 / 10000, 91 / 10000, 92 / 10000, 93 / 10000,
              91 / 10000, 91 / 10000, 91 / 10000, 91 / 10000, 91 / 10000]

err_train_custom_16 = [1715 / 60000, 711 / 60000, 419 / 60000, 249 / 60000, 206 / 60000,
                       98 / 60000, 82 / 60000, 89 / 60000, 49 / 60000, 42 / 60000,
                       39 / 60000, 40 / 60000, 33 / 60000, 33 / 60000, 32 / 60000,
                       31 / 60000, 31 / 60000, 32 / 60000, 30 / 60000, 30 / 60000]

err_test_custom_16 = [269 / 10000, 117 / 10000, 95 / 10000, 88 / 10000, 92 / 10000,
                      62 / 10000, 72 / 10000, 65 / 10000, 72 / 10000, 70 / 10000,
                      69 / 10000, 69 / 10000, 70 / 10000, 69 / 10000, 70 / 10000,
                      71 / 10000, 70 / 10000, 71 / 10000, 72 / 10000, 71 / 10000]


epoches = 20
epoches = np.arange(1, epoches + 1)
plt.xlabel("epoches")
plt.ylabel("error rate")
plt.plot(epoches, err_train_8)
plt.plot(epoches, err_test_8)
plt.legend(["training data (batch size = 8)",
            "testing data (batch size = 8)"], loc = "upper right")
plt.xticks(range(1, 20 + 1))
plt.savefig("images/figure_batch_size_8.png")





