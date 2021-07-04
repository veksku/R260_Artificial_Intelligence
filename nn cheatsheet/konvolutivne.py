#jan1 2021

#Podela u razmeri 4:1
train_images = dataset.sample(frac=0.80, random_state=0)
test_images = dataset.drop(dataset_train.index)

train_images_label = train_images
test_images_label = test_images
#Poslednja slika u skupu obucavanja i prikazati labelu
plt.xticks([])
plt.yticks([])
plt.imshow(train_images[-1], cmap=plt.cm.binary)
plt.xlabel(class_names[train_images[-1]])
plt.show()

#Normalizacija piksela u skupovima za obucavanje i testiranje
train_images = train_images / 255.0
test_images = test_images / 255.0

#Definisati model:
#konv, 32, relu, 3x3
#agr, 2x2
#konv, 32, relu, 3x3
#agr, 2x2
#konv, 32, relu, 3x3
#flatten
#dropout sa 0.1
#potpuno povezan sloj sa 1024 neurona i relu
#potp povezan sloj sa 1 neuronom i sigmoidnom aktivaciom

model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape = (IMG_HEIGHT, IMG_WIDTH)),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape = (IMG_HEIGHT, IMG_WIDTH)),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape = (IMG_HEIGHT, IMG_WIDTH)),
    keras.layers.Flatten(),
    keras.layers.Dropout(0.1),
    keras.layers.Dense(1024, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

#Kompilacija
model.compile(optimizer='adam',
    loss=tf.keras.losses.BinaryCrossentropy(),
    metrics['accuracy'])

#Obucavanje, br paketa 64, epoha 20, obucavanje:validacija=4:1, kao.. koristiti validation_split
#alternativa: train_images_history, val_images_history = model_selection.train_test_split(train_images, test_size=0.20)
train_images_history = train_images.sample(frac=0.80, random_state=0)
val_images_history = train_images.drop(train_images_history.index)

history = model.fit(
    train_images_history, epochs=20, batch_size=64, validation_data = val_images_history
)

#Nacrtati kako se menjala tacnost kroz epohe nad podacima za obucavanje i validaciju
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_acc'], label='val_accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
#plt.ylim([0.5, 1]) lupio sam, ovo fakticki odredjuje da accuracy grafik bude od 0.5 do 1
plt.legend(loc='lower right')

#Evaluirati model nad podacima za testiranje
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)