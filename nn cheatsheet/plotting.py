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

#plotovanje train vs val grafika, konkretno se koristi mse ovde
plt.plot(history.epoch, history.history['mse'])
plt.plot(history.epoch, history.history['val_mse'])
plt.ylim([0, 12])
plt.legend(['Trening MSE', 'Validacioni MSE'])

#evaluacija modela ukoliko se ne koristi 'accuracy'
loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)
print("Testing set Mean Abs Error: {:5.2f} MPG".format(mae))
