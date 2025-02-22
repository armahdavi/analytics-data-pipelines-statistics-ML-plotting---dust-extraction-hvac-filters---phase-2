## Summary
This repository summarizes all the data pipeline codes, statistical and machine learning models, descriptive statistics, and plot visualizations from Phase 2 of Mahdavi & Siegel (2020) (AS&T)

Project Milestone: 2017 - 2020

Full-length article: https://www.tandfonline.com/doi/full/10.1080/02786826.2020.1774492

## The Hidden Story in Our Air Filters
HVAC filters play a dual role in our homes. Not only do they purify the air we breathe by trapping harmful particles, but they also act as silent samplers, collecting a record of these airborne contaminants. This makes HVAC filters a valuable tool for studying Indoor Air Quality (IAQ), Indoor Environmental Engineering, and Health by analyzing the dust samples they collect over the long term and gaining insights into the particles and contaminants we breathe.

This analysis technique is known as Filter Forensics. When combined with metadata from HVAC systems (airflow rate, runtime, filter efficiency), it allows for calculating long-term airborne particle concentrations (and particle-bound chemical and biological contaminants). This concentration data is crucial for exposure assessments in chronic health studies. This quantitative approach is termed "Quantitative Filter Forensics (QFF)".

Dust recovery from residential HVAC filters is a critical step in QFF. Efficient dust extraction significantly improves the accuracy of QFF estimations. Therefore, studying and optimizing this process is essential. Data analysis of extracted dust provides valuable insights for a better understanding of IAQ and the health effects of harmful contaminants.

## This Repository
This repository showcases the data pre-processing pipeline codes, statistical models, descriptive statistics, and visualizations I used in Phase 2 of the Mahdavi & Siegel (2020) (AS&T) paper. While the paper itself discusses the front-end results, this repository provides the underlying code that generates those results, allowing you to explore the analysis firsthand.

Phase 2 of this paper includes dust extraction data from HVAC filters naturally loaded in HVAC systems

The pre-processing and logical Python codes are provided in .py (originally written in Spyder), and data visualization, statistical models, and front-end calculations are provided in .ipynb (written in Jupyter) for a guided walk-through of the data pipeline process.
