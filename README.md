#Mine the Cure (Disease Predictor)

A basic but ongoing challenge in pharmaceutical development is the reliable identification of diseased patients and those who will respond to a given therapy. While efforts have been made to address these problems, most approaches have focused on improving accuracy rather than being cost-effective and/or scalable. As a result, the market is largely composed of many new diagnostic technologies with single-use applications, creating complexity. To consolidate, we focus on using one technology (“omics”) to build multiple predictive algorithms for medical states. Our algorithm development is fueled by mining public data repositories, leveraging a proprietary normalization technique, and then applying machine learning approaches to build life-changing diagnostics.  

Open data has revolutionized medicine by empowering the public and academics to collaboratively solve incredibly complicated diseases. However, an obvious and frustrating limitation in leveraging open data stems from the discordance of compiling data from different sources, platforms, and preparations. Consequently, many researchers often participate and form large consortiums to pool standardized data based on strict guidelines. However, due to long-term commitments and overwhelming costs in generating data, participation is not always ideal or welcome. To overcome this, I have engineered a technique that normalizes omics data regardless of its origin. Compared to standard techniques, my method performs 15x better when identifying the same samples across multiple datasets (up to 6, n = 878). Along with borrowing insights and resources from the cancer field, I leverage this tool to mine publicly available omics data sets, normalize them, and then generate machine trained algorithms to develop diagnostics for patients suffering from variety of neuropathologies (with little to no cost).


#Model Performance Results


###Algorithm: V20

```
Date:  2017-01-04

Function: Outputs the probability of various diseases given gene expression data
Cross-Platform Normalization Method: arysm
Sample Type:  Human Patient RNA Samples
Conditions Evaluated:  132

-----------Statistics------------

Train Size:  18427
Test Size:  6143
Validation Size: 6143

Bootstrapped Accuracy:  0.028
Train Accuracy:         0.978
Test Accuracy:          0.891
Validation Accuracy:    0.883

Bootstrapped Precision: 0.029
Train Precision:        0.981
Test Precision:         0.901
Validation Precision:   0.894

Notable Sample Sources: GTEx, TCGA, ADNI, CCLE, CGP, CLCGP, Genentech, ArrayExpress, Gene Expression Omnibus (GEO)

```

#Conditions

###*Blood Tissue*
  - ALS
  - Alzheimer's Disease
  - Autism
  - Bipolar Disorder
  - Huntington's Disease
  - Major Depressive Disorder
  - Mild Cognitive Impairment
  - Multiple Sclerosis
  - Parkinson's Disease
  - Schizophrenia
  - Stroke

###*Brain Tissue*
  - Alzheimer's Disease
  - Parkinson's Disease

###*Normal Tissue*
  - Adipose Tissue
  - Adrenal Gland
  - Blood Vessel
  - Bladder
  - Brain
  - Breast
  - Blood
  - Colon
  - Esophagus
  - Head and Neck Region
  - Heart
  - Kidney
  - Liver
  - Lung
  - Salivary Gland
  - Skin
  - Small Intestines
  - Spleen
  - Stomach
  - Testis
  - Thyroid
  - Uterus
  - Vagina

###*Cancer*
  - Adrenal Gland
  - Bladder
  - Blood (general, AML)
  - Brain (glioma)
  - Breast
  - Cervix
  - Colon
  - Endometrium
  - Esophagus
  - Eye
  - Head and Neck Region
  - Kidney
  - Liver
  - Lung (squamous, adenocarcinoma)
  - Ovary
  - Pancreas
  - Paraganglia
  - Prostate
  - Rectum
  - Skin
  - Soft Tissue/Bone
  - Stomach
  - Testis
  - Thymus
  - Thyroid
  - Uterus
