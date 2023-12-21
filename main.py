import matplotlib.pyplot as plt
import numpy as np
import pandas as pds
import glob
# Liste des fichiers CSV à concaténer (vous pouvez ajuster cela selon vos besoins)
#chemin_dossier = 'normal/'
#pattern = '*.csv'
#chemin_fichiers = glob.glob(chemin_dossier + pattern)
#chemin_fichiers = chemin_fichiers[:1]
donneees = pds.read_csv('fusion/fusion0.csv')
#donneees = donneees.iloc[60:-100].reset_index(drop=True)
#donneees.to_csv('cut/cut11.csv', index=False)

#colonnes_a_normaliser = ['AccX [mg]', 'AccY [mg]', 'AccZ [mg]']
#donnees_norm = donneees.copy()

    # Normaliser les colonnes sélectionnées
#for colonne in colonnes_a_normaliser:
 #   min_val = np.min(donneees[colonne])
  #  max_val = np.max(donneees[colonne])
   # donnees_norm[colonne] = (donneees[colonne] - min_val) / (max_val - min_val)

#donnees_norm.to_csv('normal/normal11.csv', index=False)

# Initialiser un DataFrame pour stocker les données normalisées et concaténées
#donnees_concat = pds.DataFrame()

# Boucle sur tous les fichiers CSV
#for fichier in chemin_fichiers:
    # Lire le fichier CSV
 #   donnees = pds.read_csv(fichier)

    # Concaténer les données normalisées avec le DataFrame principal
  #  donnees_concat = pds.concat([donnees_concat,donnees], ignore_index=True)
   # donnees_concat = donnees_concat.sort_values(by='T [ms]').reset_index(drop=True)
    #donnees_concat['T [ms]'] = np.arange(0, len(donnees_concat) * 20, 20)

# Enregistrez les données concaténées dans un nouveau fichier CSV
#donnees_concat.to_csv('fusion/fusion0.csv', index=False)


temps = donneees['T [ms]'].to_numpy()
acceleration_x = donneees['AccX [mg]'].to_numpy()
acceleration_y = donneees['AccY [mg]'].to_numpy()
acceleration_z = donneees['AccZ [mg]'].to_numpy()
# Créer un gyroacceleration_z
# plt.figure(figsize=(15, 6))
# plt.subplot(2, 1, 1)
# plt.plot(donnees['T [ms]'], donnees['GyroX [mdps]'], label='AccX en fonction de T')
# plt.plot(donnees['T [ms]'], donnees['GyroY [mdps]'], label='AccY en fonction de T')
# plt.plot(donnees['T [ms]'], donnees['GyroZ [mdps]'], label='AccZ en fonction de T')

# plt.xlabel('Temps (T) en ms')
# plt.ylabel('Gyroscope en mdps')
# plt.title("Graphique de la l'acceleration de Z en fonction de T")
# plt.legend()
# plt.grid(True)

# Créer un accelero
# plt.subplot(4, 1, 4)
plt.figure(1)
plt.plot(temps, acceleration_x, label='AccX en fonction de T')
plt.plot(temps, acceleration_y, label='AccY en fonction de T')
plt.plot(temps, acceleration_z, label='AccZ en fonction de T')

plt.xlabel('Temps (T) en ms')
plt.ylabel('Accélération en mg')
plt.title("Graphique de la l'acceleration  en fonction de T")
plt.legend()
plt.grid(True)
plt.show()
