# ------------------------------------------------------------------------------
#
#   Copyright 2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
import tensorflow as tf
import tensorflow_datasets as tfds

from colearn_keras.utils import normalize_img

n_rounds = 20
width = 28
height = 28
n_classes = 10
l_rate = 0.001
batch_size = 64

# Load the data
train_dataset, info = tfds.load('mnist', split='train', as_supervised=True, with_info=True)
n_train = info.splits['train'].num_examples
test_dataset = tfds.load('mnist', split='test', as_supervised=True)

train_dataset = train_dataset.map(normalize_img,
                                  num_parallel_calls=tf.data.experimental.AUTOTUNE)
train_dataset = train_dataset.shuffle(n_train)
train_dataset = train_dataset.batch(batch_size)

test_dataset = test_dataset.map(normalize_img,
                                num_parallel_calls=tf.data.experimental.AUTOTUNE)
test_dataset = test_dataset.batch(batch_size)

# Define the model
input_img = tf.keras.Input(shape=(width, height, 1), name="Input")
x = tf.keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same", name="Conv1_1")(input_img)
x = tf.keras.layers.BatchNormalization(name="bn1")(x)
x = tf.keras.layers.MaxPooling2D((2, 2), name="pool1")(x)
x = tf.keras.layers.Conv2D(128, (3, 3), activation="relu", padding="same", name="Conv2_1")(x)
x = tf.keras.layers.BatchNormalization(name="bn4")(x)
x = tf.keras.layers.MaxPooling2D((2, 2), name="pool2")(x)
x = tf.keras.layers.Flatten(name="flatten")(x)
x = tf.keras.layers.Dense(n_classes, activation="softmax", name="fc1")(x)
model = tf.keras.Model(inputs=input_img, outputs=x)

opt = tf.keras.optimizers.Adam(lr=l_rate)
model.compile(
    loss="sparse_categorical_crossentropy",
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
    optimizer=opt)

# Train and evaluate model
for round in range(n_rounds):
    model.fit(train_dataset, steps_per_epoch=40)
    result = model.evaluate(x=test_dataset, return_dict=True, steps=10)
    print(f"Performance at round {round} is {result}")
