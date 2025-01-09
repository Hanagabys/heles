# ====================================
# 📊 11. Análisis de Importancia de Variables (Feature Importance)
# ====================================
import matplotlib.pyplot as plt
# Extraer la importancia de las variables del modelo optimizado
feature_importances = best_rf.feature_importances_
feature_names = X.columns
# Crear un DataFrame con los resultados
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importances
}).sort_values(by='Importance', ascending=False)
# Mostrar las 10 variables más importantes
print("\nImportancia de Variables (Top 10):")
print(importance_df.head(10))

# ====================================
# 📈 12. Gráfico de Correlación
# ====================================
import seaborn as sns
plt.figure(figsize=(12, 10))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Mapa de Correlación de Variables')
plt.show()
