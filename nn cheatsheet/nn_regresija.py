categorical_attributes = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
target_variable = ['class']

#Ucitati car.csv i iskoristi pandas metod describe
dataset = pd.read_csv('./car.csv')
dataset.describe()

#Kategoricke atribute enkodirati koristeci dummy enkodiranje
input_train_dataset = dataset.drop(axis=1, columns='class')
train_dataset = pd.get_dummies(input_train_dataset)

#Napravi skup y gde se nalazi ciljna promenljiva 'class'
y_input = dataset[['class']]
y_input['class'] = y_input['class'].map({'acc': 0, 'good': 1, 'unacc': 2, 'vgood': 3})
y = keras.utils.to_categorical(y_input, 4)

#Podeliti podatke na skup za obucavanje/trening i validaciju/test u razmeri 3:1.
train_dataset, test_dataset = model_selection.train_test_split(train_dataset, test_size = 0.25)
y_train, y_test = model_selection.train_test_split(y, test_size = 0.25)

#Napraviti potpuno povezano neuronsku mrezu koja ima jedan skriveni sloj sa 32 neurona.
model = keras.Sequential([
    keras.layers.Dense(32, input_dim=21, activation='relu'),
    keras.layers.Dense(4, activation='softmax')
])

#Obucavanje, br paketa 32, 10 epoha, za gresku kategoricka kros entropija, postaviti i podatke za validaciju
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer='adam',
    metrics=['accuracy'])

history = model.fit(train_dataset, y_train, epochs=10, batch_size=32, validation_data=(test_dataset, y_test), shuffle=True)

#Nacrtati zavisnost tacnosti od epohe i legendu
plt.plot(history.history['accuracy'], label = 'accuracy')
plt.plot(history.history['test_accuracy'], label = 'test_accuracy')
plt.ylim([0.5, 1])
plt.legend(['acc', 'test_acc'])
