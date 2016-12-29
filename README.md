# Mine the Cure

A basic but ongoing challenge in pharmaceutical development is the reliable identification of diseased patients and those who will respond to a given therapy. While efforts have been made to address these problems, most approaches have focused on improving accuracy rather than being cost-effective and/or scalable. As a result, the market is largely composed of many new diagnostic technologies with single-use applications, creating complexity. To consolidate, we focus on using one technology (“omics”) to build multiple predictive algorithms for medical states. Our algorithm development is fueled by mining public data repositories, leveraging a proprietary normalization technique, and then applying machine learning approaches to build life-changing diagnostics.  

Open data has revolutionized medicine by empowering the public and academics to collaboratively solve incredibly complicated diseases. However, an obvious and frustrating limitation in leveraging open data stems from the discordance of compiling data from different sources, platforms, and preparations. Consequently, many researchers often participate and form large consortiums to pool standardized data based on strict guidelines. However, due to long-term commitments and overwhelming costs in generating data, participation is not always ideal or welcome. To overcome this, I have engineered a technique that normalizes omics data regardless of its origin. Compared to standard techniques, my method performs 15x better when identifying the same samples across multiple datasets (up to 6, n = 878). Along with borrowing insights and resources from the cancer field, I leverage this tool to mine publically available omics data sets, normalize them, and then generate machine trained algorithms to develop diagnostics for patients suffering from varity of diseases including cancer and neuropathologies (with little to no cost).

==========================
Model Performance Results
==========================

Algorithm: V9

Sample Type: Human Patient Samples

Conditions Evaluated: 71

Train Sample Size: 18,631
Test Sample Size: 6,211
Validation Sample size: 6,211

Bootstrapped Accuracy (Random): 6.39%
Train Accuracy: 97.25%
Test Accuracy: 92.39%
Validation Accuracy: 92.18%

Avg. Test Precision: 95.24%
Avg. Validation Precision: 94.19%

Notable Sample Sources: GTeX, TCGA, ADNI, ArrayExpress, Gene Expression Omnibus (GEO)

==========================
       Conditions 
==========================


Blood Tissue
------------
ALS
Stroke
Multiple Sclerosis
Huntington's Disease
Parkinson's Disease
Schizophrenia
Major Depressive Disorder
Mild Cognitive Impairment
Alzheimer's Disease

Brain Tissue
-------------
Parkinson's Disease
Alzheimer's Disease

Normal Tissue
-------------
Brain
Adipose Tissue
Adrenal Gland
Blood Vessel
Bladder
Breast
Blood
Colon
Esophagus
Heart
Kidney
Liver
Lung
Salivary Gland
Skin
Small Intestines
Spleen
Stomach
Testis
Thyroid
Uterus
Vagina

Cancer
-------
Adrenal Gland
Bladder
Blood (general, AML)
Brain (glioma)
Breast
Cervix
Colon
Endometrium
Esophagus
Eye
Head and Neck Region
Kidney
Liver
Lung (squamous, adenocarcinoma)
Ovary
Pancreas
Paraganglia
Prostate
Rectum
Skin
Soft Tissue/Bone
Stomach
Testis
Thymus
Thyroid
Uterus




