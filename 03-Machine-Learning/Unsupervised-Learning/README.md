# 🔮 UNSUPERVISED LEARNING

> [!yellow] ⭐ **FIND HIDDEN PATTERNS IN DATA!**
> "The goal is to discover the hidden patterns and structures in the data without labels."
> 
> **Time to Complete:** 2-3 weeks  
> **Difficulty:** ⭐⭐⭐ Medium  
> **Interview Weight:** ⭐⭐⭐⭐ Very Important!

---

## 🗺️ UNSUPERVISED LEARNING ROADMAP

```mermaid
graph TD
    A[📊 Unlabeled Data] --> B[Clustering]
    A --> C[Dimensionality Reduction]
    A --> D[Anomaly Detection]
    
    B --> E[K-Means<br/>Hierarchical<br/>DBSCAN]
    C --> F[PCA<br/>t-SNE<br/>UMAP]
    D --> G[Isolation Forest<br/>One-Class SVM]
    
    E --> H[🎯 Customer Segments]
    F --> I[🎯 Visualization]
    G --> J[🎯 Fraud Detection]
    
    style A fill:#e1f5fe
    style B fill:#c8e6c9
    style C fill:#fff9c4
    style D fill:#ffcdd2
    style H fill:#ffd700
    style I fill:#ffd700
    style J fill:#ffd700
```

---

## 📚 TABLE OF CONTENTS

| # | Topic | Purpose | Link |
|---|-------|---------|------|
| 1 | **K-Means Clustering** | Group similar data | [[#1-k-means-clustering\|Jump]] |
| 2 | **Hierarchical Clustering** | Tree-based grouping | [[#2-hierarchical-clustering\|Jump]] |
| 3 | **DBSCAN** | Density-based clusters | [[#3-dbscan\|Jump]] |
| 4 | **PCA** | Reduce dimensions | [[#4-pca-principal-component-analysis\|Jump]] |
| 5 | **t-SNE & UMAP** | Visualization | [[#5-t-sne-and-umap\|Jump]] |
| 6 | **Anomaly Detection** | Find outliers | [[#6-anomaly-detection\|Jump]] |

---

## 1. K-MEANS CLUSTERING

> [!blue] 💙 **What is K-Means?**
> Groups data into K clusters by minimizing distance to cluster centers (centroids).

### How K-Means Works

```mermaid
graph TD
    A[Start: Random K centroids] --> B[Assign points to nearest centroid]
    B --> C[Recalculate centroids]
    C --> D{Centroids moved?}
    D -->|Yes| B
    D -->|No| E[Done! K clusters formed]
    
    style A fill:#e1f5fe
    style B fill:#c8e6c9
    style C fill:#fff9c4
    style E fill:#ffd700
```

### Visual Understanding

```
Step 1: Initialize K=3 random centroids
    ●     ●     ●
    
Step 2: Assign points to nearest centroid
    ● ○○    ● △△    ● ◇◇
    ○○       △△       ◇◇
    
Step 3: Move centroids to center of clusters
      ●       ●       ●
    ○○○     △△△     ◇◇◇
    ○○       △△       ◇◇
    
Step 4: Reassign & repeat until stable
```

> [!yellow] 💡 **How to Choose K?**

**The Elbow Method:**

```mermaid
graph LR
    A[Calculate WCSS<br/>for K=1 to 10] --> B[Plot K vs WCSS]
    B --> C[Find 'Elbow'<br/>where gain diminishes]
    C --> D[Optimal K!]
    
    style D fill:#ffd700
```

```
WCSS (Within-Cluster Sum of Squares):
Sum of squared distances from points to their centroid

Plot looks like an arm:
WCSS
  |
  |●
  |  ●
  |    ●← Elbow here! (K=3)
  |      ●
  |        ●●●●
  |_____________ K
    1 2 3 4 5 6 7
```

> [!green] ✅ **Real-World Applications**
> ```
> 1. CUSTOMER SEGMENTATION
>    - Group customers by behavior
>    - Target marketing campaigns
>    - Identify VIP customers
> 
> 2. IMAGE COMPRESSION
>    - Reduce colors in image
>    - K clusters = K colors
>    - Smaller file size
> 
> 3. DOCUMENT CLUSTERING
>    - Group similar articles
>    - News categorization
>    - Content recommendation
> 
> 4. ANOMALY DETECTION
>    - Points far from all centroids
>    - Fraud detection
>    - Quality control
> ```

> [!red] ⚠️ **Limitations of K-Means**
> ```
> ❌ Must specify K in advance
> ❌ Sensitive to outliers
> ❌ Assumes spherical clusters
> ❌ Sensitive to initialization
> ❌ Doesn't work well with:
>    - Non-spherical shapes
>    - Different sized clusters
>    - Different density clusters
> ```

---

## 2. HIERARCHICAL CLUSTERING

> [!blue] 💙 **What is Hierarchical Clustering?**
> Creates a tree (dendrogram) showing how clusters merge or split at different levels.

### Two Approaches

```mermaid
graph TD
    A[Hierarchical Clustering] --> B[Agglomerative<br/>Bottom-Up]
    A --> C[Divisive<br/>Top-Down]
    
    B --> D[Start: Each point = cluster<br/>Merge closest clusters<br/>Repeat until 1 cluster]
    C --> E[Start: All points = 1 cluster<br/>Split into sub-clusters<br/>Repeat until N clusters]
    
    style B fill:#c8e6c9
    style C fill:#fff9c4
```

### Dendrogram Visualization

```
Height = Distance when clusters merge

        |
     ___|___
    |       |
   _|_     _|_
  |   |   |   |
  A   B   C   D

Cut here → 2 clusters: {A,B} and {C,D}
Cut here → 3 clusters: {A}, {B,C,D}
         → 4 clusters: {A}, {B}, {C}, {D}
```

> [!yellow] 💡 **Linkage Methods**

```mermaid
graph TD
    A[How to measure<br/>cluster distance?] --> B[Single Linkage]
    A --> C[Complete Linkage]
    A --> D[Average Linkage]
    A --> E[Ward's Method]
    
    B --> F[Min distance<br/>between any two points]
    C --> G[Max distance<br/>between any two points]
    D --> H[Average distance<br/>between all pairs]
    E --> I[Minimize variance<br/>within clusters]
    
    style E fill:#c8e6c9
```

> [!green] ✅ **Advantages over K-Means**
> ```
> ✅ No need to specify K upfront
> ✅ Dendrogram shows cluster hierarchy
> ✅ Can cut at any level
> ✅ Deterministic (no random initialization)
> ✅ Works with any distance metric
> ✅ Better for non-spherical clusters
> ```

> [!red] ⚠️ **Disadvantages**
> ```
> ❌ Computationally expensive: O(n³)
> ❌ Not suitable for large datasets
> ❌ Sensitive to noise and outliers
> ❌ Once merged, cannot undo
> ```

---

## 3. DBSCAN

> [!blue] 💙 **What is DBSCAN?**
> Density-Based Spatial Clustering - finds clusters based on density, not distance!

**DBSCAN = Density-Based Spatial Clustering of Applications with Noise**

### Key Concepts

```mermaid
graph TD
    A[DBSCAN Parameters] --> B[ε epsilon<br/>Neighborhood radius]
    A --> C[minPts<br/>Min points in neighborhood]
    
    D[Point Types] --> E[Core Point<br/>≥minPts in ε-neighborhood]
    D --> F[Border Point<br/>In neighborhood of core point]
    D --> G[Noise Point<br/>Neither core nor border]
    
    style E fill:#c8e6c9
    style F fill:#fff9c4
    style G fill:#ffcdd2
```

### Visual Understanding

```
ε = radius, minPts = 4

Core points (●):     Border points (○):    Noise (×):
  ●●●●                  ○                     ×
  ●●●●                ●●●●
  ●●●●                ●●●●                   ×
  
Cluster 1            Cluster 2             Not in any cluster
```

### How DBSCAN Works

```mermaid
graph TD
    A[Pick unvisited point] --> B{Has ≥minPts<br/>in ε-radius?}
    B -->|Yes| C[Mark as Core Point<br/>Start new cluster]
    B -->|No| D{In neighborhood<br/>of core point?}
    D -->|Yes| E[Mark as Border Point]
    D -->|No| F[Mark as Noise]
    
    C --> G[Add all reachable points<br/>to cluster]
    G --> H[Expand cluster]
    
    style C fill:#c8e6c9
    style E fill:#fff9c4
    style F fill:#ffcdd2
```

> [!yellow] ⭐ **Why DBSCAN is Powerful**
> ```
> ✅ Doesn't require K (number of clusters)
> ✅ Finds arbitrarily shaped clusters
> ✅ Handles different sized clusters
> ✅ Identifies outliers as noise
> ✅ Robust to outliers
> ✅ Only 2 parameters (ε, minPts)
> ```

> [!green] ✅ **Real-World Use Cases**
> ```
> 1. GEOGRAPHIC CLUSTERING
>    - Crime hotspots
>    - Restaurant locations
>    - Disease outbreaks
> 
> 2. ANOMALY DETECTION
>    - Network intrusion
>    - Fraud detection
>    - Manufacturing defects
> 
> 3. IMAGE SEGMENTATION
>    - Object detection
>    - Medical imaging
>    - Satellite imagery
> ```

> [!red] ⚠️ **When DBSCAN Struggles**
> ```
> ❌ Clusters with varying densities
> ❌ High-dimensional data (curse of dimensionality)
> ❌ Choosing ε is tricky
> ❌ Sensitive to parameter values
> ```

---

## 4. PCA (PRINCIPAL COMPONENT ANALYSIS)

> [!blue] 💙 **What is PCA?**
> Reduces dimensions while preserving maximum variance in data.

### The Core Idea

```
Original Data: 100 features → PCA → 10 features
While keeping 95% of information!

How? Find directions (principal components) with most variance.
```

### Visual Understanding (3D → 2D)

```mermaid
graph LR
    A[3D Data Cloud] --> B[Find direction<br/>with most variance]
    B --> C[PC1:<br/>Maximum variance]
    C --> D[Find perpendicular direction<br/>with next most variance]
    D --> E[PC2:<br/>Second most variance]
    E --> F[Project onto PC1 & PC2<br/>Now 2D!]
    
    style A fill:#bbdefb
    style C fill:#c8e6c9
    style E fill:#fff9c4
    style F fill:#ffd700
```

```
Original 3D:              After PCA (2D):
    z                          PC2
    |                           |
    |  ●●●                      |  ●●
    | ●●●●                      | ●●●
    |●●●●                       |●●●
    |____x                      |____PC1
   /                           
  /y                           
  
Lost 1 dimension, kept 95% variance!
```

> [!yellow] 💡 **How Many Components to Keep?**

```mermaid
graph TD
    A[Scree Plot Method] --> B[Plot variance<br/>explained vs components]
    B --> C[Find elbow or<br/>cumulative 95%]
    
    D[Cumulative Variance] --> E[Keep components until<br/>cumulative ≥ 95%]
    
    style C fill:#ffd700
    style E fill:#ffd700
```

```
Variance Explained:
%
100|                  _____ Cumulative
 95|              ___/
 90|          ___/
   |      ___/
 50|   __/●  ← Elbow (keep 2-3 components)
   | _/
  0|●
   |_________________
    1  2  3  4  5  6
    Principal Components
```

> [!green] ✅ **When to Use PCA**
> ```
> ✅ High-dimensional data (100+ features)
> ✅ Features are correlated
> ✅ Visualization (reduce to 2D/3D)
> ✅ Speed up training
> ✅ Remove noise
> ✅ Overcome curse of dimensionality
> 
> Real Examples:
> - Image compression
> - Face recognition (Eigenfaces)
> - Gene expression analysis
> - Stock market analysis
> ```

> [!red] ⚠️ **PCA Limitations**
> ```
> ❌ Linear transformation only
> ❌ Assumes directions of max variance = important
> ❌ Principal components hard to interpret
> ❌ Sensitive to scale (must standardize first!)
> ❌ May lose important info in low-variance directions
> ```

### PCA vs Other Methods

```mermaid
graph TD
    A[Dimensionality<br/>Reduction] --> B[Linear]
    A --> C[Non-Linear]
    
    B --> D[PCA:<br/>Fast, interpretable]
    B --> E[LDA:<br/>Supervised, classification]
    
    C --> F[t-SNE:<br/>Visualization only]
    C --> G[UMAP:<br/>Faster, preserves structure]
    C --> H[Autoencoders:<br/>Deep learning]
    
    style D fill:#c8e6c9
    style F fill:#fff9c4
    style G fill:#bbdefb
```

---

## 5. t-SNE AND UMAP

> [!blue] 💙 **What are t-SNE and UMAP?**
> Non-linear dimensionality reduction for **visualization** (not for modeling!)

### t-SNE (t-Distributed Stochastic Neighbor Embedding)

```mermaid
graph LR
    A[High-D Data] --> B[Calculate pairwise<br/>similarities]
    B --> C[Map to 2D/3D<br/>preserving similarities]
    C --> D[Similar points<br/>stay close]
    
    style D fill:#ffd700
```

**Key Idea:** Similar points in high-D should be close in 2D

```
High-Dimensional:           t-SNE 2D:
Point A and B are close     A B  ← Still close!
   ●A  ●B                    
                            C    ← Far away
Point C is far              
      ●C
```

> [!yellow] ⭐ **t-SNE vs UMAP**

| Feature | t-SNE | UMAP |
|---------|-------|------|
| **Speed** | Slow (O(n²)) | Fast (O(n log n)) |
| **Large datasets** | ❌ Struggles | ✅ Handles well |
| **Preserves** | Local structure | Local + Global |
| **Deterministic** | ❌ Random | ✅ More stable |
| **Use for modeling** | ❌ No! | ⚠️ Maybe |
| **Best for** | Visualization | Visualization + preprocessing |

> [!green] ✅ **Amazing Use Cases**
> ```
> 1. VISUALIZE HIGH-D DATA
>    - 1000-D word embeddings → 2D plot
>    - See clusters and patterns
>    - Explore data structure
> 
> 2. MNIST DIGITS
>    - 784 pixels → 2D
>    - See digit clusters
>    - Understand what model sees
> 
> 3. SINGLE-CELL RNA
>    - 20,000 genes → 2D
>    - Identify cell types
>    - Discover new patterns
> 
> 4. DOCUMENT SIMILARITY
>    - Text embeddings → 2D
>    - See topic clusters
>    - Find similar documents
> ```

> [!red] ⚠️ **Important Warnings**
> ```
> ❌ DON'T use for feature engineering
> ❌ DON'T interpret distances quantitatively
> ❌ DON'T compare across different runs
> ❌ DON'T use as model input (use PCA instead)
> 
> ✅ DO use for visualization only
> ✅ DO try different perplexity values (t-SNE)
> ✅ DO standardize data first
> ✅ DO use UMAP for large datasets
> ```

---

## 6. ANOMALY DETECTION

> [!blue] 💙 **What is Anomaly Detection?**
> Finding rare items, events, or observations that differ significantly from the majority.

### Types of Anomalies

```mermaid
graph TD
    A[Anomaly Types] --> B[Point Anomaly]
    A --> C[Contextual Anomaly]
    A --> D[Collective Anomaly]
    
    B --> E[Single instance<br/>is abnormal<br/>Example: $1M transaction]
    C --> F[Normal in one context,<br/>abnormal in another<br/>Example: 30°C in winter]
    D --> G[Collection is abnormal<br/>Example: DDoS attack pattern]
    
    style B fill:#ffcdd2
    style C fill:#fff9c4
    style D fill:#e1bee7
```

### Methods Comparison

```mermaid
graph TD
    A[Anomaly Detection<br/>Methods] --> B[Statistical]
    A --> C[Distance-Based]
    A --> D[Density-Based]
    A --> E[Isolation-Based]
    
    B --> F[Z-score<br/>Assumes distribution]
    C --> G[K-NN<br/>Distance to neighbors]
    D --> H[LOF<br/>Local density]
    E --> I[Isolation Forest<br/>Easy to isolate]
    
    style I fill:#c8e6c9
```

### Isolation Forest Concept

```
Normal points: Hard to isolate (need many splits)
Anomalies: Easy to isolate (few splits needed)

Normal:                 Anomaly:
  ●●●                      ●
  ●●●                   ●●●●
  ●●●                   ●●●●
Split many times          ×  ← Easy to isolate!
to isolate one point
```

> [!green] ✅ **Real-World Applications**
> ```
> 1. FRAUD DETECTION
>    - Credit card transactions
>    - Insurance claims
>    - Account takeovers
> 
> 2. NETWORK SECURITY
>    - Intrusion detection
>    - DDoS attacks
>    - Malware detection
> 
> 3. MANUFACTURING
>    - Defect detection
>    - Equipment failure
>    - Quality control
> 
> 4. HEALTHCARE
>    - Disease outbreak
>    - Medical imaging
>    - Vital sign monitoring
> 
> 5. FINANCE
>    - Market manipulation
>    - Unusual trading patterns
>    - Money laundering
> ```

> [!yellow] 💡 **Choosing the Right Method**

| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| **Isolation Forest** | High-D data | Fast, scalable | Black box |
| **One-Class SVM** | Complex patterns | Flexible kernel | Slow, parameters |
| **LOF** | Density anomalies | Finds local outliers | Slow on large data |
| **Autoencoder** | Complex data | Deep learning power | Needs tuning |
| **Statistical** | Simple, Gaussian | Interpretable | Assumes distribution |

---

## 💎 INTERVIEW QUESTIONS

> [!yellow] 💎 **Q: K-Means vs Hierarchical Clustering - when to use which?**
> 
> **Perfect Answer:**
> 
> **Use K-Means when:**
> - Large datasets (>10,000 points)
> - Know approximate number of clusters
> - Clusters are spherical
> - Need fast results
> - Example: Customer segmentation
> 
> **Use Hierarchical when:**
> - Small to medium datasets
> - Don't know number of clusters
> - Need dendrogram visualization
> - Want to explore different K values
> - Clusters may have complex shapes
> - Example: Gene expression analysis
> 
> **Key Differences:**
> - K-Means: O(n) iterations | Hierarchical: O(n³)
> - K-Means: Need K upfront | Hierarchical: Cut dendrogram later
> - K-Means: Random start | Hierarchical: Deterministic
> - K-Means: Spherical clusters | Hierarchical: Any shape

> [!yellow] 💎 **Q: Explain curse of dimensionality**
> 
> **Perfect Answer:**
> "The curse of dimensionality refers to problems that arise when working with high-dimensional data:
> 
> **Problems:**
> 1. **Distance becomes meaningless**
>    - All points become equally distant
>    - Near and far lose meaning
> 
> 2. **Data becomes sparse**
>    - Points spread out in high-D space
>    - Need exponentially more data
> 
> 3. **Computation explodes**
>    - O(2^d) complexity
>    - Algorithms slow down
> 
> **Solutions:**
> - Feature selection (keep important features)
> - Dimensionality reduction (PCA, t-SNE)
> - Regularization
> - Domain knowledge (remove irrelevant features)
> 
> **Example:**
> - 1D: 10 points cover space well
> - 10D: Need 10^10 points for same coverage!
> - 100D: Distances all look the same"

> [!yellow] 💎 **Q: How do you evaluate clustering results?**
> 
> **Perfect Answer:**
> "Evaluating clustering is tricky since we don't have labels!
> 
> **Internal Metrics (no labels needed):**
> 
> 1. **Silhouette Score** (-1 to 1)
>    - Measures cluster cohesion & separation
>    - Higher is better
>    - >0.5 is good
> 
> 2. **Davies-Bouldin Index**
>    - Average similarity between clusters
>    - Lower is better
> 
> 3. **Calinski-Harabasz Score**
>    - Ratio of between-cluster to within-cluster variance
>    - Higher is better
> 
> **External Metrics (if labels available):**
> 
> 1. **Adjusted Rand Index (ARI)**
>    - Compare to ground truth
>    - 1 = perfect match
> 
> 2. **Normalized Mutual Information (NMI)**
>    - Information theoretic measure
> 
> **Business Metrics:**
> - Do clusters make business sense?
> - Can we action on them?
> - Do they align with domain knowledge?
> 
> **Best Practice:**
> - Use multiple metrics
> - Visualize clusters (t-SNE)
> - Validate with domain experts
> - A/B test in production"

---

**Tags:** #unsupervised-learning #clustering #dimensionality-reduction #anomaly-detection  
**Difficulty:** ⭐⭐⭐ Medium  
**Time to Master:** 2-3 weeks  
**Last Updated:** 2026-11-11
