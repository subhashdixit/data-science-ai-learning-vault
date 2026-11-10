"""
Generate high-quality images for ML concepts
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, make_regression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve, auc
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Create output directory
import os
os.makedirs('images/linear-regression', exist_ok=True)
os.makedirs('images/logistic-regression', exist_ok=True)
os.makedirs('images/decision-trees', exist_ok=True)
os.makedirs('images/random-forest', exist_ok=True)

print("Generating ML visualization images...")

# ============================================================================
# LINEAR REGRESSION IMAGES
# ============================================================================

# 1. Linear Regression - Basic Fit
np.random.seed(42)
X = np.linspace(0, 10, 50)
y = 2.5 * X + 5 + np.random.randn(50) * 3

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, s=50, label='Data Points')
plt.plot(X, 2.5*X + 5, 'r-', linewidth=2, label='Best Fit Line (y = 2.5x + 5)')
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.title('Linear Regression: Finding the Best Fit Line', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('images/linear-regression/01-basic-fit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Linear Regression: Basic fit")

# 2. MSE Visualization with Error Lines
plt.figure(figsize=(10, 6))
X_sample = X[:10]
y_sample = y[:10]
y_pred = 2.5*X_sample + 5

plt.scatter(X_sample, y_sample, alpha=0.8, s=80, label='Actual Values', color='blue', zorder=3)
plt.plot(X, 2.5*X + 5, 'r-', linewidth=2, label='Regression Line', zorder=2)

# Draw error lines
for i in range(len(X_sample)):
    plt.plot([X_sample[i], X_sample[i]], [y_sample[i], y_pred[i]],
             'k--', alpha=0.5, linewidth=1.5, zorder=1)

plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.title('Mean Squared Error (MSE): Measuring Vertical Distances', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.text(7, 10, 'MSE = Average of\nsquared distances', fontsize=11,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
plt.tight_layout()
plt.savefig('images/linear-regression/02-mse-visualization.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Linear Regression: MSE visualization")

# 3. Gradient Descent Path
theta_path = []
theta = np.array([-2.0, 0.5])
learning_rate = 0.1

for _ in range(50):
    theta_path.append(theta.copy())
    gradient = np.random.randn(2) * 0.5  # Simulated gradient
    theta = theta - learning_rate * gradient

theta_path = np.array(theta_path)

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(theta_path[:, 0], theta_path[:, 1], range(len(theta_path)),
         'b-', linewidth=2, alpha=0.7)
ax1.scatter(theta_path[0, 0], theta_path[0, 1], 0, c='green', s=100, label='Start')
ax1.scatter(theta_path[-1, 0], theta_path[-1, 1], len(theta_path)-1, c='red', s=100, label='End')
ax1.set_xlabel('Weight (w)', fontsize=11)
ax1.set_ylabel('Bias (b)', fontsize=11)
ax1.set_zlabel('Iteration', fontsize=11)
ax1.set_title('Gradient Descent Path', fontsize=12, fontweight='bold')
ax1.legend()

ax2 = fig.add_subplot(122)
loss_curve = np.exp(-np.linspace(0, 3, 50)) * 10 + np.random.randn(50) * 0.2
ax2.plot(loss_curve, linewidth=2, color='blue')
ax2.set_xlabel('Iteration', fontsize=12)
ax2.set_ylabel('Loss (MSE)', fontsize=12)
ax2.set_title('Loss Curve During Training', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/linear-regression/03-gradient-descent.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Linear Regression: Gradient descent")

# 4. Regularization Comparison (Ridge vs Lasso)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Ridge (L2)
lambdas = np.logspace(-3, 3, 50)
ridge_weights = np.exp(-lambdas/10)[:, np.newaxis] * np.random.randn(50, 5).cumsum(axis=0)
for i in range(5):
    axes[0].plot(lambdas, ridge_weights[:, i], linewidth=2, label=f'Feature {i+1}')
axes[0].set_xscale('log')
axes[0].set_xlabel('λ (Regularization Strength)', fontsize=12)
axes[0].set_ylabel('Weight Value', fontsize=12)
axes[0].set_title('Ridge (L2): Shrinks All Weights', fontsize=13, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)

# Lasso (L1)
lasso_weights = ridge_weights.copy()
for i in range(5):
    threshold_idx = np.random.randint(10, 30)
    lasso_weights[threshold_idx:, i] = 0

for i in range(5):
    axes[1].plot(lambdas, lasso_weights[:, i], linewidth=2, label=f'Feature {i+1}')
axes[1].set_xscale('log')
axes[1].set_xlabel('λ (Regularization Strength)', fontsize=12)
axes[1].set_ylabel('Weight Value', fontsize=12)
axes[1].set_title('Lasso (L1): Sets Some Weights to Zero', fontsize=13, fontweight='bold')
axes[1].legend(fontsize=10)
axes[1].grid(True, alpha=0.3)
axes[1].axhline(y=0, color='k', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('images/linear-regression/04-regularization.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Linear Regression: Regularization")

# ============================================================================
# LOGISTIC REGRESSION IMAGES
# ============================================================================

# 1. Sigmoid Function
z = np.linspace(-10, 10, 200)
sigmoid = 1 / (1 + np.exp(-z))

plt.figure(figsize=(10, 6))
plt.plot(z, sigmoid, linewidth=3, color='blue')
plt.axhline(y=0.5, color='red', linestyle='--', alpha=0.7, label='Decision Boundary (0.5)')
plt.axvline(x=0, color='red', linestyle='--', alpha=0.7)
plt.xlabel('z (Linear Combination)', fontsize=12)
plt.ylabel('σ(z) = Probability', fontsize=12)
plt.title('Sigmoid Function: Mapping Linear Output to Probability', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.text(-7, 0.9, 'σ(z) = 1 / (1 + e⁻ᶻ)', fontsize=13,
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
plt.ylim(-0.1, 1.1)
plt.tight_layout()
plt.savefig('images/logistic-regression/01-sigmoid-function.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Logistic Regression: Sigmoid function")

# 2. Decision Boundary
np.random.seed(42)
X1, y1 = make_classification(n_samples=200, n_features=2, n_redundant=0,
                             n_informative=2, n_clusters_per_class=1,
                             flip_y=0.1, class_sep=1.5)

model = LogisticRegression()
model.fit(X1, y1)

plt.figure(figsize=(10, 6))

# Plot decision boundary
x_min, x_max = X1[:, 0].min() - 1, X1[:, 0].max() + 1
y_min, y_max = X1[:, 1].min() - 1, X1[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))
Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, levels=20, cmap='RdYlBu', alpha=0.6)
plt.colorbar(label='P(Class 1)')
plt.scatter(X1[y1==0, 0], X1[y1==0, 1], c='blue', edgecolors='k', s=50, alpha=0.8, label='Class 0')
plt.scatter(X1[y1==1, 0], X1[y1==1, 1], c='red', edgecolors='k', s=50, alpha=0.8, label='Class 1')
plt.xlabel('Feature 1', fontsize=12)
plt.ylabel('Feature 2', fontsize=12)
plt.title('Logistic Regression: Decision Boundary', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('images/logistic-regression/02-decision-boundary.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Logistic Regression: Decision boundary")

# 3. Confusion Matrix
y_true = np.array([0, 0, 1, 1, 0, 1, 0, 1, 1, 0])
y_pred = np.array([0, 1, 1, 1, 0, 1, 0, 0, 1, 0])
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True,
            square=True, linewidths=2, linecolor='black',
            xticklabels=['Predicted 0', 'Predicted 1'],
            yticklabels=['Actual 0', 'Actual 1'],
            annot_kws={'fontsize': 16, 'fontweight': 'bold'})
plt.title('Confusion Matrix', fontsize=14, fontweight='bold')
plt.ylabel('True Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)

# Add labels
plt.text(0.5, 0.3, 'TN\nTrue Negative', ha='center', va='center', fontsize=10, color='darkblue')
plt.text(1.5, 0.3, 'FP\nFalse Positive', ha='center', va='center', fontsize=10, color='darkred')
plt.text(0.5, 1.3, 'FN\nFalse Negative', ha='center', va='center', fontsize=10, color='darkred')
plt.text(1.5, 1.3, 'TP\nTrue Positive', ha='center', va='center', fontsize=10, color='darkblue')

plt.tight_layout()
plt.savefig('images/logistic-regression/03-confusion-matrix.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Logistic Regression: Confusion matrix")

# 4. ROC Curve
np.random.seed(42)
y_true_roc = np.random.randint(0, 2, 100)
y_scores = np.random.rand(100)
fpr, tpr, _ = roc_curve(y_true_roc, y_scores)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, color='darkorange', lw=3, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier (AUC = 0.50)')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)', fontsize=12)
plt.ylabel('True Positive Rate (TPR)', fontsize=12)
plt.title('ROC Curve: Model Performance', fontsize=14, fontweight='bold')
plt.legend(loc="lower right", fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('images/logistic-regression/04-roc-curve.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Logistic Regression: ROC curve")

# ============================================================================
# DECISION TREES IMAGES
# ============================================================================

# 1. Simple Decision Tree Visualization
X_tree, y_tree = make_classification(n_samples=100, n_features=4, n_informative=3,
                                      n_redundant=0, random_state=42)
feature_names = ['Age', 'Income', 'Credit Score', 'Debt Ratio']

tree_model = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_model.fit(X_tree, y_tree)

plt.figure(figsize=(20, 10))
plot_tree(tree_model, feature_names=feature_names, class_names=['Reject', 'Approve'],
          filled=True, rounded=True, fontsize=10)
plt.title('Decision Tree Structure (Max Depth = 3)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('images/decision-trees/01-tree-structure.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Decision Trees: Tree structure")

# 2. Gini vs Entropy Impurity
p = np.linspace(0.01, 0.99, 100)
gini = 1 - (p**2 + (1-p)**2)
entropy = -(p * np.log2(p) + (1-p) * np.log2(1-p))

plt.figure(figsize=(10, 6))
plt.plot(p, gini, linewidth=3, label='Gini Impurity', color='blue')
plt.plot(p, entropy/2, linewidth=3, label='Entropy (scaled)', color='red')
plt.xlabel('Probability of Class 1', fontsize=12)
plt.ylabel('Impurity', fontsize=12)
plt.title('Gini vs Entropy: Impurity Measures', fontsize=14, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.axvline(x=0.5, color='green', linestyle='--', alpha=0.5, label='Maximum Impurity')
plt.tight_layout()
plt.savefig('images/decision-trees/02-gini-vs-entropy.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Decision Trees: Gini vs Entropy")

# 3. Overfitting Visualization
X_simple = np.linspace(0, 10, 50).reshape(-1, 1)
y_simple = np.sin(X_simple).ravel() + np.random.randn(50) * 0.2

tree_shallow = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_deep = DecisionTreeClassifier(max_depth=20, random_state=42)

# Convert to classification problem
y_class = (y_simple > 0).astype(int)
tree_shallow.fit(X_simple, y_class)
tree_deep.fit(X_simple, y_class)

X_test = np.linspace(0, 10, 200).reshape(-1, 1)
y_shallow = tree_shallow.predict(X_test)
y_deep = tree_deep.predict(X_test)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.scatter(X_simple, y_class, c=y_class, cmap='RdYlBu', s=50, edgecolors='k')
ax1.plot(X_test, y_shallow, 'g-', linewidth=2, label='Depth=3')
ax1.set_title('Shallow Tree: Good Generalization', fontsize=13, fontweight='bold')
ax1.set_xlabel('X', fontsize=11)
ax1.set_ylabel('Class', fontsize=11)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

ax2.scatter(X_simple, y_class, c=y_class, cmap='RdYlBu', s=50, edgecolors='k')
ax2.plot(X_test, y_deep, 'r-', linewidth=2, label='Depth=20 (Overfits!)')
ax2.set_title('Deep Tree: Overfitting', fontsize=13, fontweight='bold')
ax2.set_xlabel('X', fontsize=11)
ax2.set_ylabel('Class', fontsize=11)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/decision-trees/03-overfitting.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Decision Trees: Overfitting")

# 4. Feature Importance
feature_importance = tree_model.feature_importances_
indices = np.argsort(feature_importance)[::-1]

plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importance)), feature_importance[indices], color='steelblue', alpha=0.8)
plt.xticks(range(len(feature_importance)), [feature_names[i] for i in indices], fontsize=11)
plt.xlabel('Features', fontsize=12)
plt.ylabel('Importance', fontsize=12)
plt.title('Feature Importance in Decision Tree', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('images/decision-trees/04-feature-importance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Decision Trees: Feature importance")

# ============================================================================
# RANDOM FOREST IMAGES
# ============================================================================

# 1. Ensemble Concept
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Random Forest: Ensemble of Decision Trees', fontsize=16, fontweight='bold')

for idx, ax in enumerate(axes.flat[:6]):
    X_rf = np.random.rand(50, 1) * 10
    y_rf = (X_rf > 5).astype(int).ravel()

    # Bootstrap sample
    bootstrap_idx = np.random.choice(len(X_rf), size=len(X_rf), replace=True)
    X_boot = X_rf[bootstrap_idx]
    y_boot = y_rf[bootstrap_idx]

    tree = DecisionTreeClassifier(max_depth=3, random_state=idx)
    tree.fit(X_boot, y_boot)

    X_plot = np.linspace(0, 10, 100).reshape(-1, 1)
    y_plot = tree.predict(X_plot)

    ax.scatter(X_boot, y_boot, c=y_boot, cmap='RdYlBu', s=30, alpha=0.6)
    ax.plot(X_plot, y_plot, 'k-', linewidth=2, alpha=0.7)
    ax.set_title(f'Tree {idx+1}', fontsize=12)
    ax.set_ylim(-0.2, 1.2)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/random-forest/01-ensemble-concept.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Random Forest: Ensemble concept")

# 2. Bias-Variance Trade-off
n_trees = np.arange(1, 201, 5)
variance = 100 / n_trees + np.random.randn(len(n_trees)) * 2
bias = np.ones(len(n_trees)) * 20 + np.random.randn(len(n_trees)) * 1
total_error = bias + variance

plt.figure(figsize=(10, 6))
plt.plot(n_trees, bias, linewidth=2, label='Bias² (stays constant)', color='blue')
plt.plot(n_trees, variance, linewidth=2, label='Variance (decreases)', color='red')
plt.plot(n_trees, total_error, linewidth=3, label='Total Error', color='green', linestyle='--')
plt.xlabel('Number of Trees', fontsize=12)
plt.ylabel('Error', fontsize=12)
plt.title('Random Forest: Bias-Variance Trade-off', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.axvline(x=100, color='purple', linestyle=':', alpha=0.7, label='Sweet Spot (~100 trees)')
plt.tight_layout()
plt.savefig('images/random-forest/02-bias-variance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Random Forest: Bias-variance trade-off")

# 3. OOB Score Convergence
oob_scores = 0.5 + 0.4 * (1 - np.exp(-n_trees/50)) + np.random.randn(len(n_trees)) * 0.01

plt.figure(figsize=(10, 6))
plt.plot(n_trees, oob_scores, linewidth=3, color='green')
plt.axhline(y=0.90, color='red', linestyle='--', alpha=0.7, label='Target Accuracy')
plt.xlabel('Number of Trees', fontsize=12)
plt.ylabel('OOB Score (Accuracy)', fontsize=12)
plt.title('Out-of-Bag (OOB) Score Convergence', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.ylim(0.4, 1.0)
plt.text(150, 0.85, 'Diminishing\nreturns after\n~100 trees', fontsize=11,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
plt.tight_layout()
plt.savefig('images/random-forest/03-oob-convergence.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Random Forest: OOB convergence")

print("\n" + "="*60)
print("✅ All images generated successfully!")
print("="*60)
print(f"\nTotal images created: 16")
print("  - Linear Regression: 4 images")
print("  - Logistic Regression: 4 images")
print("  - Decision Trees: 4 images")
print("  - Random Forest: 3 images")
print("\nImages saved in:")
print("  • images/linear-regression/")
print("  • images/logistic-regression/")
print("  • images/decision-trees/")
print("  • images/random-forest/")
