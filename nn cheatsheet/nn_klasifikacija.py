fashion_mnist = keras.datasets.fashion_mnist

# Funkcija vraca dva uredjena para kod kojih je prvi element niz
# slika, a drugi element niz labela za slike.
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
							 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
              
#pretprocesiranje slika 
train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
	plt.subplot(5,5,i+1)
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow(train_images[i], cmap=plt.cm.binary)
	plt.xlabel(class_names[train_labels[i]])
plt.show()

#tf.keras.layers.Flatten ce prosledjeni oblik podataka izravnati, odnosno u nasem slucaju ce dimenziju 28x28 pretvoriti u 784
#tf.keras.layers.Dense ce nam omoguciti da definisemo potpuno povezani sloj neurona sa njihovim tezinama i aktivacijama
#tf.keras.Sequential je objekat koji konstruisemo iz liste slojeva koji definisu arhitekturu nase mreze
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
#softmax = klasifikacija, sigmoid = regresija

print(train_labels.shape)
train_labels_cat = keras.utils.to_categorical(train_labels)
test_labels_cat = keras.utils.to_categorical(test_labels)
print(train_labels_cat.shape)

model.compile(optimizer='adam',
							loss=tf.keras.losses.CategoricalCrossentropy(),
							metrics=['accuracy'])

model.fit(train_images, train_labels_cat, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels_cat, verbose=2)
print('\nTest accuracy:', test_acc)

#prikaz predikcija, prvih 15 test slika, ispravni su obojeni plavom bojom a neispravni crvenom
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
	plt.subplot(num_rows, 2*num_cols, 2*i+1)
	plot_image(i, predictions[i], test_labels, test_images)
	plt.subplot(num_rows, 2*num_cols, 2*i+2)
	plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()
test
