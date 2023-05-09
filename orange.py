import Orange



# Cargar los datos en Orange

data = Orange.data.Table("agriculture_data.csv")



# Realizar una exploración inicial de los datos

print(f"Number of instances: {len(data)}")

print(f"Number of attributes: {len(data.domain.attributes)}")

print(f"Attribute names: {data.domain.attributes}")

print(f"Class name: {data.domain.class_var}")

print(f"Class values: {data.domain.class_var.values}")



# Preprocesar los datos según sea necesario

# Ejemplo: eliminar valores atípicos

data = data.remove_outliers()



# Dividir los datos en conjuntos de entrenamiento y prueba

train_data, test_data = data.split_random(0.8)



# Construir el modelo de árbol de decisión CART utilizando los datos de entrenamiento

cart = Orange.classification.CARTLearner()

model = cart(train_data)



# Evaluar el rendimiento del modelo utilizando los datos de prueba

predictions = model(test_data)

accuracy = Orange.evaluation.Accuracy(predictions, test_data)

print(f"Accuracy: {accuracy}")



# Comparar con otros algoritmos de árbol de decisión

hunt = Orange.classification.HuntLearner()

model = hunt(train_data)

predictions = model(test_data)

accuracy =

id3 = Orange.classification.ID3Learner() model = id3(train_data) predictions = model(test_data) accuracy = Orange.evaluation.Accuracy(predictions, test_data) print(f"Accuracy with ID3: {accuracy}")

c45 = Orange.classification.C45Learner() model = c45(train_data) predictions = model(test_data) accuracy = Orange.evaluation.Accuracy(predictions, test_data) print(f"Accuracy with C4.5: {accuracy}")

sliq = Orange.classification.SLIQLearner() model = sliq(train_data) predictions = model(test_data) accuracy = Orange.evaluation.Accuracy(predictions, test_data) print(f"Accuracy with SLIQ: {accuracy}")

sprint = Orange.classification.SprintLearner() model = sprint(train_data) predictions = model(test_data) accuracy = Orange.evaluation.Accuracy(predictions, test_data) print(f"Accuracy with SPRINT: {accuracy}")

#Seleccionar el modelo con el mejor rendimiento y utilizarlo para realizar predicciones
best_model = cart # o cualquiera de los otros algoritmos, dependiendo del rendimiento

#Realizar predicciones sobre el rendimiento del cultivo en una finca específica
tomato_farm = [("cultivo", "tomate"), ("ubicación", "Almería"), ("tamaño", "pequeña"), ("fertilizantes", "si")] prediction = best_model(tomato_farm) print(f"Predicted yield for tomato farm: {prediction}")

#Identificar los principales factores que influyen en el rendimiento del cultivo
importances = Orange.evaluation.Importance(best_model, test_data) print(f"Importances of attributes: {importances}")

#Proporcionar recomendaciones para mejorar el rendimiento en el sector de la agricultura
if importances[0] > 0.5: print("Consider using a different type of cultivar to improve yield.") if importances[1] > 0.5: print("Consider changing the location of the farm to improve yield.") if importances[2] > 0.5: print("Consider expanding the size of

#Utilizar técnicas de validación cruzada para evaluar el rendimiento del modelo y minimizar el sesgo
scores = Orange.evaluation.CrossValidation(data, [cart], k=5) print(f"Cross-validation scores: {scores}") mean_score = sum(scores) / len(scores) print(f"Mean cross-validation score: {mean_score}")

#Utilizar técnicas de selección de características para seleccionar las variables más importantes y mejorar la capacidad del modelo de hacer predicciones precisas
selector = Orange.feature.selection.BestFeaturesLearner(model=cart, k=3) selected_data = selector(data) print(f"Selected attributes: {selected_data.domain.attributes}")

#Utilizar técnicas de ensamble, como el bosque aleatorio, para mejorar aún más el rendimiento del modelo
forest = Orange.ensemble.RandomForestLearner() model = forest(data) predictions = model(test_data) accuracy = Orange.evaluation.Accuracy(predictions, test_data) print(f"Accuracy with random forest: {accuracy}")

#Presentar los resultados del análisis en un informe, incluyendo gráficos y tablas que ilustren los hallazgos más importantes y las recomendaciones realizadas
Orange.visualization.boxplot(data, "yield", ["cultivo", "ubicación"]) Orange.visualization.scatterplot

#Utilizar el modelo para identificar los principales factores que influyen en el rendimiento del cultivo
#y proporcionar recomendaciones para mejorar el rendimiento en el sector de la agricultura
importances = model.importance print(f"Importances: {importances}")

#Identificar las variables con mayor importancia
most_important_vars = [data.domain.attributes[i] for i in range(len(importances)) if importances[i] == max(importances)] print(f"Most important variables: {most_important_vars}")

#Proporcionar recomendaciones basadas en los resultados del modelo y la importancia de cada variable
if "cultivo" in most_important_vars: print("Se recomienda seleccionar variedades de tomates que hayan demostrado tener altos rendimientos en el pasado.") if "ubicación" in most_important_vars: print("Se recomienda elegir una ubicación con condiciones climáticas favorables para el cultivo de tomates.") if "tamaño de la finca" in most_important_vars: print("Se recomienda utilizar un tamaño de finca adecuado para maximizar el rendimiento del cultivo.") if "fertilizantes" in most_important_vars: print("Se recomienda utilizar fertilizantes de alta calidad y en dosis adecuadas para mejorar el rendimiento del cultivo.")