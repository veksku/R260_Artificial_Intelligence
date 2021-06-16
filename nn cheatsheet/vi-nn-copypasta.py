#pravi mrezu slika 5x5 u okviru 10,10
plt.figure(figsize=(10,10)) #okvir u koji ce se smestati slike
for i in range(25):
    plt.subplot(5,5,i+1) #5x5, treci parametar je uvek i+1
    plt.xticks([]) #sklanja crtice x ose
    plt.yticks([]) #sklanja crtice y ose
    plt.grid(False) #nmp, zapamti
    plt.imshow(train_images[i], cmap=plt.cm.binary) #smesta sliku train_images[i] cmap su neke boje
    plt.xlabel(class_names[train_labels[i]]) #fakticki se upise ime ispod slike, fazon je da je to ime x ose
plt.show()




#=======================================================================================================================
#primer 1:
#pretprocesiranje, unose se slike
train_images = train_images / 255.0
test_images = test_images / 255.0

#pravljenje modela, slike imaju flatten sloj
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), #input je slika 28x28
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax') #ovde je softmax jer se izlaz transformise u raspodelu vrvtnce
])

#da bi se kompajlirao model, moramo da konvertujemo labele u odgovarajuc format
keras.utils.to_categorical(train_labels)
keras.utils.to_categorical(test_labels)

model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy']) #uvek accuracy uz crossentropy

#trenira se model
model.fit(train_images, train_labels_cat, epochs=10)

#evaluacija modela na skupu za testiranje
test_loss, test_acc = model.evaluate(test_images,  test_labels_cat, verbose=2)

print('\nTest accuracy:', test_acc)

#koriscenje modela
predictions = model.predict(test_images) #test_images je zapravo input neki nad slikama

predictions[0] #daje niz vrednosti koje oznacavaju vrvtn pripadnosti slike jednoj klasi
ix = np.argmax(predictions[0]) #uzima najvecu vrednost iz predictions[0] - najverovatnija klasa

#ako trazimo klasu nad jednom slikom
img = test_images[1]
img = (np.expand_dims(img,0)) #potrebno za sledecu keras fju funkciju

predictions_single = model.predict(img) #keras.Model.predict




#=======================================================================================================================
#primer 2:
dataset = pd.read_csv()
dataset['Origin'] = dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})

#dummy enkodiranje
dataset = pd.get_dummies(dataset, prefix='', prefix_sep='') #ovo gore ce ubaci kao 3 nove kolone sa 0 ili 1

train_dataset = dataset.sample(frac=0.8,random_state=0) #80% u trening
test_dataset = dataset.drop(train_dataset.index) #ostatak u test, fora je da ce ovo dropne sve indexe u trainu
#popujemo ciljnu promenljivu iz podataka
train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')
#normalizujemo ostatak podataka
def norm(x):
  return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

#pravljenje modela
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1) #trazimo potrosnju, ne treba nam nikakva aktivaciona fja niti skaliranje
])

optimizer = tf.keras.optimizers.RMSprop(0.001)
model.compile(loss='mse', 
              optimizer=optimizer,
              metrics=['mae', 'mse'])

#koriscenje modela
example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
example_result

#obucavanje modela
EPOCHS = 1000
#history bitan za grafovanje kasnije
history = model.fit( 
  normed_train_data, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=1)
#crtanje
plt.plot(history.epoch, history.history['mse'])
plt.plot(history.epoch, history.history['val_mse'])
plt.ylim([0, 12])
plt.legend(['Trening MSE', 'Validacioni MSE'])

#evaluacija modela
loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} MPG".format(mae))




#=======================================================================================================================
#primer 3